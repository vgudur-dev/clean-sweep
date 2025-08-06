"""
CleanSweep
==========

CleanSweep is a digital housekeeping toolkit designed to help you
recover space and organize your files.  It provides functions to
identify duplicate files, report storage usage and highlight the
largest files consuming your disk.  The CLI exposes commands for
finding duplicates and generating size reports.

This package is intended to be run on your local machine and does not
send any information over the network.  It’s free, open source and
works on Linux, macOS and Windows.
"""

from .duplicate_finder import find_duplicates  # noqa: F401
from .size_reporter import get_largest_files, summarize_by_extension  # noqa: F401
