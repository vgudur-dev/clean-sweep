"""
Duplicate file detection utilities.

This module provides functions to scan directories for duplicate files
based on their contents using cryptographic hashes. It reads files in
chunks to handle large files efficiently.
"""
from __future__ import annotations

import hashlib
import os
from pathlib import Path
from typing import Iterable, Dict, List


def _file_hash(path: Path, chunk_size: int = 1024 * 1024) -> str:
    """Return the SHA-256 digest of the given file."""
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(chunk_size), b""):
            h.update(chunk)
    return h.hexdigest()


def _iter_files(paths: Iterable[Path]) -> Iterable[Path]:
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
        One or more filesystem paths to scan. Directories are
        traversed recursively; individual files are hashed directly.

    Returns
    -------
    Dict[str, List[str]]
        Mapping from SHA-256 hash digest to a list of file paths that
        share that digest. Only hashes with two or more files are
        included (i.e. actual duplicates).
    """
    hash_map: Dict[str, List[str]] = {}
    for f in _iter_files([Path(p) for p in paths]):
        try:
            digest = _file_hash(f)
        except Exception:
            # Skip unreadable files
            continue
        hash_map.setdefault(digest, []).append(str(f))
    # Filter out unique files
    return {h: files for h, files in hash_map.items() if len(files) > 1}
