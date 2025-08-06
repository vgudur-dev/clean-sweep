# CleanSweep

![CleanSweep illustration](assets/cleansweep-illustration.png)

**CleanSweep** is an open‑source digital housekeeping utility that
helps you identify duplicate files, report space hogs and regain
control of your storage.  It runs locally, respects your privacy and
works across Windows, macOS and Linux.  With just a few commands you
can discover identical photos and videos, find the biggest files
cluttering your disk and understand how different file types consume
space.

## Why CleanSweep?

Our devices have become digital attics.  A survey of 2,000 Americans
found that entertainment files like photos and videos occupy the
majority of digital storage and that **three in five people hardly
ever delete pictures from their smartphones**【433264692552072†L62-L104】.  Six in ten say
they’ve become more reliant on technology for work and socialising
since the pandemic【433264692552072†L62-L104】, and 56 % admit they’ve been storing even
more photos on their devices【433264692552072†L62-L104】.  The result?  **Two‑thirds of
Americans say their camera roll is a mess**【433264692552072†L88-L104】, and 70 % wish they
could see all of their content in one place【433264692552072†L100-L104】.  With digital
clutter piling up across multiple devices, it’s easy to run out of
space, lose track of important files and pay for unnecessary cloud
storage.

CleanSweep provides a simple, transparent way to declutter your
digital life.  Unlike proprietary cleaners that hide what they do or
advertise aggressively, CleanSweep is fully open source.  You can
inspect the code, trust that your data stays on your machine and
customise the behaviour to fit your needs.

## Features

- **Duplicate Finder** – Recursively scan directories to identify
  files with identical contents using SHA‑256 hashes.  CleanSweep
  groups duplicates together and presents them in a clear report.  You
  decide which copies to keep or remove.
- **Storage Reporter** – Generate reports of the largest files on
  your system and see how storage usage breaks down by file extension.
  Find out if 4K videos, ISO images or old archives are hogging your
  disk.
- **Privacy‑Preserving** – All scanning happens locally.  CleanSweep
  never uploads your files or metadata anywhere.
- **Cross‑Platform & Lightweight** – Written in pure Python, it runs on
  Windows, macOS and Linux without external dependencies.  There is
  nothing to install beyond Python itself.
- **Extensible** – The modular architecture makes it easy to add
  actions like automated deletion (with confirmation), duplicate
  photo detection based on perceptual hashing or integration with
  cloud storage providers.

## Installation

Clone the repository and run CleanSweep using Python 3.8 or newer:

```bash
git clone https://github.com/yourusername/clean_sweep.git
cd clean_sweep
python -m clean_sweep.cli --help
```

To install as a package with a console script (future work):

```bash
pip install clean-sweep
```

## Quick Start

Find duplicate files in your Downloads and Pictures folders:

```bash
python -m clean_sweep.cli find-duplicates ~/Downloads ~/Pictures
```

Generate a storage report showing the 5 largest files and usage by
extension:

```bash
python -m clean_sweep.cli report ~/Documents --top 5
```

The output lists the largest files first, followed by a summary of
file counts and cumulative sizes by extension.  Use this information
to decide which files to archive or delete.
# CleanSweep

![CleanSweep illustration](assets/cleansweep-illustration.png)

**CleanSweep** is an open‑source digital housekeeping utility that
helps you identify duplicate files, report space hogs and regain
control of your storage.  It runs locally, respects your privacy and
works across Windows, macOS and Linux.  With just a few commands you
can discover identical photos and videos, find the biggest files
cluttering your disk and understand how different file types consume
space.

## Why CleanSweep?

Our devices have become digital attics.  A survey of 2,000 Americans
found that entertainment files like photos and videos occupy the
majority of digital storage and that **three in five people hardly
ever delete pictures from their smartphones**【433264692552072†L62-L104】.  Six in ten say
they’ve become more reliant on technology for work and socialising
since the pandemic【433264692552072†L62-L104】, and 56 % admit they’ve been storing even
more photos on their devices【433264692552072†L62-L104】.  The result?  **Two‑thirds of
Americans say their camera roll is a mess**【433264692552072†L88-L104】, and 70 % wish they
could see all of their content in one place【433264692552072†L100-L104】.  With digital
clutter piling up across multiple devices, it’s easy to run out of
space, lose track of important files and pay for unnecessary cloud
storage.

CleanSweep provides a simple, transparent way to declutter your
digital life.  Unlike proprietary cleaners that hide what they do or
advertise aggressively, CleanSweep is fully open source.  You can
inspect the code, trust that your data stays on your machine and
customise the behaviour to fit your needs.

## Features

- **Duplicate Finder** – Recursively scan directories to identify
  files with identical contents using SHA‑256 hashes.  CleanSweep
  groups duplicates together and presents them in a clear report.  You
  decide which copies to keep or remove.
- **Storage Reporter** – Generate reports of the largest files on
  your system and see how storage usage breaks down by file extension.
  Find out if 4K videos, ISO images or old archives are hogging your
  disk.
- **Privacy‑Preserving** – All scanning happens locally.  CleanSweep
  never uploads your files or metadata anywhere.
- **Cross‑Platform & Lightweight** – Written in pure Python, it runs on
  Windows, macOS and Linux without external dependencies.  There is
  nothing to install beyond Python itself.
- **Extensible** – The modular architecture makes it easy to add
  actions like automated deletion (with confirmation), duplicate
  photo detection based on perceptual hashing or integration with
  cloud storage providers.

## Installation

Clone the repository and run CleanSweep using Python 3.8 or newer:

```bash
git clone https://github.com/yourusername/clean_sweep.git
cd clean_sweep
python -m clean_sweep.cli --help
```

To install as a package with a console script (future work):

```bash
pip install clean-sweep
```

## Quick Start

Find duplicate files in your Downloads and Pictures folders:

```bash
python -m clean_sweep.cli find-duplicates ~/Downloads ~/Pictures
```

Generate a storage report showing the 5 largest files and usage by
extension:

```bash
python -m clean_sweep.cli report ~/Documents --top 5
```

The output lists the largest files first, followed by a summary of
file counts and cumulative sizes by extension.  Use this information
to decide which files to archive or delete.

## How It Works

CleanSweep’s duplicate finder computes a cryptographic hash for every
file it scans.  Files that produce the same SHA‑256 digest are
grouped together.  Reading files in small chunks minimises memory
usage and allows hashing of large videos and disk images.  The size
reporter traverses the same directory tree, records each file’s size
and extension and then aggregates the data to produce both the
“largest files” list and the “by extension” summary.

## Roadmap

1. **Interactive Duplicate Removal** – Add an optional prompt to
   delete duplicates after review.
2. **Perceptual Image Hashing** – Detect visually similar photos even
   when file contents differ (e.g. different resolutions).
3. **Cross‑Device Indexing** – Build a catalogue of files across
   multiple devices and present them in one unified view.
4. **Graphical UI** – Provide a desktop application for users who
   prefer a graphical interface.

## License

This project is released under the [Apache 2.0 license](../LICENSE).

---

*Digital clutter is a universal problem.  Surveys show that most
people rarely delete old photos and videos【433264692552072†L62-L104】, leading to messy
camera rolls and wasted storage【433264692552072†L88-L104】.  CleanSweep gives you the
tools to see what’s consuming your space and take back control.*
## How It Works

CleanSweep’s duplicate finder computes a cryptographic hash for every
file it scans.  Files that produce the same SHA‑256 digest are
grouped together.  Reading files in small chunks minimises memory
usage and allows hashing of large videos and disk images.  The size
reporter traverses the same directory tree, records each file’s size
and extension and then aggregates the data to produce both the
“largest files” list and the “by extension” summary.

## Roadmap

1. **Interactive Duplicate Removal** – Add an optional prompt to
   delete duplicates after review.
2. **Perceptual Image Hashing** – Detect visually similar photos even
   when file contents differ (e.g. different resolutions).
3. **Cross‑Device Indexing** – Build a catalogue of files across
   multiple devices and present them in one unified view.
4. **Graphical UI** – Provide a desktop application for users who
   prefer a graphical interface.

## License

This project is released under the [Apache 2.0 license](../LICENSE).

---

*Digital clutter is a universal problem.  Surveys show that most
people rarely delete old photos and videos【433264692552072†L62-L104】, leading to messy
camera rolls and wasted storage【433264692552072†L88-L104】.  CleanSweep gives you the
tools to see what’s consuming your space and take back control.*
