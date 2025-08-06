# CleanSweep
![GitHub stars](https://img.shields.io/github/stars/vgudur-dev/clean-sweep?style=social) ![License](https://img.shields.io/badge/license-MIT-blue.svg)


CleanSweep is a cross‑platform, privacy‑focused utility that helps you declutter your digital life by finding duplicate files and identifying storage hogs. It runs locally and works on Windows, macOS and Linux without external dependencies.

## Why CleanSweep?

Our digital devices are overflowing with photos, videos and downloads. A survey of 2,000 Americans found that entertainment files like photos and videos take up the majority of digital storage and that three in five people hardly ever delete pictures from their smartphones【433264692552072†L62-L104】. Over half admit they’re storing more photos than ever【433264692552072†L62-L104】, leaving many camera rolls a mess【433264692552072†L88-L104】. Seventy percent of people wish they could see all their content in one place【433264692552072†L100-L104】. CleanSweep gives you the insight and tools to reclaim space and organise your files.

## Features

- **Duplicate Finder** – Recursively scan directories and group files with identical content using secure SHA‑256 hashing. You decide which copies to keep or delete.
- **Storage Reporter** – See the top N largest files on your system and a breakdown of storage usage by file extension.
- **Local and Private** – All scanning is performed locally on your machine; no data leaves your computer.
- **Pure Python & Cross‑Platform** – Runs on Windows, macOS and Linux with no external dependencies.
- **Extensible** – Built with a modular design so you can add perceptual image hashing, automated deletion with confirmation, or cloud integration.

## Installation

Clone this repository and run the CLI using Python 3.8 or newer:

```bash
git clone https://github.com/vgudur-dev/clean-sweep.git
cd clean-sweep
python -m clean_sweep.cli --help
```

An installable package and console script will be published soon.

## Quick Start

Find duplicate files in your Downloads and Pictures folders:

```bash
python -m clean_sweep.cli find-duplicates ~/Downloads ~/Pictures
```

Generate a storage report showing the 5 largest files and usage by extension:

```bash
python -m clean_sweep.cli report ~/Documents --top 5
```

The output lists the largest files first and summarises how many files and bytes are used by each extension. Use this information to decide what to archive or remove.

## How It Works

The duplicate finder reads each file in small chunks and computes a SHA‑256 digest. Files that produce the same digest are grouped together. The size reporter traverses the same directory tree, records file sizes and extensions, then aggregates statistics.

### Show Your Support

If CleanSweep saves you time and storage space, please give this repo a ⭐ star and share it with others. Every star helps raise awareness and keeps this project thriving!

## Contributing

Contributions are welcome! If you have ideas for new features or bug fixes, please open an issue or pull request. Star this repository to show your support and help others discover CleanSweep.

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
