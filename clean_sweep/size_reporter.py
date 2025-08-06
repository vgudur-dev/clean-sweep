"""
Storage reporting utilities.

This module provides helper functions to identify the largest files in
a set of directories and to summarise storage usage by file
extension. It is designed to support digital cleaning tasks like
finding space hogs and understanding which file types dominate your
storage.
"""
from __future__ import annotations

import os
from pathlib import Path
from typing import Iterable, List, Tuple, Dict


def _iter_files(paths: Iterable[Path]) -> Iterable[Path]:
    for base in paths:
        if base.is_file():
            yield base
        elif base.is_dir():
            for root, _, files in os.walk(base):
                for fname in files:
                    yield Path(root) / fname


def get_largest_files(paths: Iterable[str], n: int = 10) -> List[Tuple[str, int]]:
    """Return the N largest files under the given paths.

    Parameters
    ----------
    paths: Iterable[str]
        Directories and/or files to scan.
    n: int
        Number of top files to return.

    Returns
    -------
    List[Tuple[str, int]]
        A list of (file_path, size_bytes) tuples sorted by size
        descending.
    """
    sizes: List[Tuple[str, int]] = []
    for f in _iter_files([Path(p) for p in paths]):
        try:
            sz = f.stat().st_size
        except Exception:
            continue
        sizes.append((str(f), sz))
    sizes.sort(key=lambda x: x[1], reverse=True)
    return sizes[:n]


def summarize_by_extension(paths: Iterable[str]) -> Dict[str, Dict[str, int]]:
    """Summarise storage usage by file extension.

    Parameters
    ----------
    paths: Iterable[str]
        Directories and/or files to scan.

    Returns
    -------
    Dict[str, Dict[str, int]]
        Mapping of file extension to a dict with keys 'count' and 'bytes'
        indicating the number of files and total size.
    """
    summary: Dict[str, Dict[str, int]] = {}
    for f in _iter_files([Path(p) for p in paths]):
        try:
            ext = f.suffix.lower() or "(no ext)"
            sz = f.stat().st_size
        except Exception:
            continue
        info = summary.setdefault(ext, {"count": 0, "bytes": 0})
        info["count"] += 1
        info["bytes"] += sz
    return summary
