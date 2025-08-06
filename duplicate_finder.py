"""
Duplicate file finder.

This module provides utilities for scanning directories recursively,
computing file hashes and grouping files with identical content.  It
uses SHA‑256 for hashing and reads files in chunks to handle large
files efficiently.
"""
from __future__ import annotations

import hashlib
import os
from pathlib import Path
from typing import Dict, List, Iterable


def _file_hash(path: Path, chunk_size: int = 8192) -> str:
    """Compute the SHA‑256 hash of a file.

    The file is read in chunks to support large files without
    excessive memory usage.
    """
    sha256 = hashlib.sha256()
    with path.open("rb") as f:
        while True:
            chunk = f.read(chunk_size)
            if not chunk:
                break
            sha256.update(chunk)
    return sha256.hexdigest()


def _iter_files(paths: Iterable[Path]) -> Iterable[Path]:
    """Yield all files under the given directory paths (recursively)."""
    for base in paths:
        if base.is_file():
            yield base
        elif base.is_dir():
            for root, _, files in os.walk(base):
                for fname in files:
                    yield Path(root) / fname


def find_duplicates(paths: Iterable[str]) -> Dict[str, List[str]]:
    """Find duplicate files under the given paths.

    Parameters
    ----------
    paths: Iterable[str]
        One or more filesystem paths to scan.  Directories are
        traversed recursively; individual files are hashed directly.

    Returns
    -------
    Dict[str, List[str]]
        Mapping from SHA‑256 hash digest to a list of file paths that
        share that digest.  Only hashes with two or more files are
        included (i.e. actual duplicates).
    """
    hash_map: Dict[str, List[str]] = {}
    for f in _iter_files([Path(p) for p in paths]):
        try:
            h = _file_hash(f)
        except Exception:
            # Skip unreadable files
            continue
        hash_map.setdefault(h, []).append(str(f))
    # Filter out unique files
    return {h: files for h, files in hash_map.items() if len(files) > 1}
