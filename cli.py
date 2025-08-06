"""
CleanSweep CLI.

This command‑line interface exposes functions for finding duplicate
files and reporting disk usage statistics.  To see available
commands, run `python -m clean_sweep.cli --help` or the installed
console script `cleansweep`.
"""
from __future__ import annotations

import argparse
import json
import sys
from typing import List

from .duplicate_finder import find_duplicates
from .size_reporter import get_largest_files, summarize_by_extension


def _cmd_find_dupes(args: argparse.Namespace) -> None:
    dupes = find_duplicates(args.paths)
    if not dupes:
        print("No duplicates found.")
        return
    if args.json:
        print(json.dumps(dupes, indent=2))
    else:
        for digest, files in dupes.items():
            print(f"Hash: {digest}")
            for f in files:
                print(f"  {f}")
            print()


def _cmd_report(args: argparse.Namespace) -> None:
    largest = get_largest_files(args.paths, n=args.top)
    summary = summarize_by_extension(args.paths)
    print(f"Top {args.top} largest files:")
    for path, size in largest:
        print(f"  {size:10d} bytes – {path}")
    print("\nStorage usage by file extension:")
    # Sort by bytes descending
    for ext, info in sorted(summary.items(), key=lambda x: x[1]["bytes"], reverse=True):
        count = info["count"]
        bytes_ = info["bytes"]
        print(f"  {ext or '(no ext)'}: {count} files, {bytes_} bytes")


def main(argv: List[str] | None = None) -> None:
    parser = argparse.ArgumentParser(prog="cleansweep", description="CleanSweep CLI")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # find-duplicates command
    dup_parser = subparsers.add_parser("find-duplicates", help="Find duplicate files under given paths.")
    dup_parser.add_argument("paths", nargs="+", help="One or more files or directories to scan.")
    dup_parser.add_argument(
        "--json",
        action="store_true",
        help="Output duplicates as JSON mapping hashes to file lists.",
    )
    dup_parser.set_defaults(func=_cmd_find_dupes)

    # report command
    report_parser = subparsers.add_parser("report", help="Report storage usage and largest files.")
    report_parser.add_argument("paths", nargs="+", help="One or more files or directories to analyse.")
    report_parser.add_argument(
        "--top",
        type=int,
        default=10,
        help="Number of largest files to list (default 10).",
    )
    report_parser.set_defaults(func=_cmd_report)

    args = parser.parse_args(argv)
    args.func(args)


if __name__ == "__main__":
    main()
