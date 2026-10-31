# Briga de Estudante

A text-based fighting/RPG game about a student brawl, played in the console. My first real programming project, started in my first semester of Digital Games (Jogos Digitais) at Fatec, in 2013.

## History

- **Apr-May 2013**: versions v1 to v5-3, written in Python 3.
- **May-Oct 2013**: ported to Python 2 (`v2k` line, from 1-1 up to 1-99836) to build Windows executables with py2exe; save system (`Data/*.sabi`), menus and ASCII art.
- **Jan 2014**: v2k-1-998361, story script (`roteiro.txt`) and screenshots in `docs/screenshots/`.
- **Dec 2014**: start of a graphical remake with pygame (`pygame-remake/`), with tiles, character sprites and a map editor built on my `pyTreeBee` library.

The original files were versioned by filename (no git back then); this repository rebuilds that sequence as commits, dated from the original files.

## Author

Fernando Luiz Neme Chibli ([@fershibli](https://github.com/fershibli))

## Play in the browser

**[https://fershibli.github.io/briga-de-estudante/](https://fershibli.github.io/briga-de-estudante/)**

The browser version runs `web/game/briga_de_estudante.py` (a Python 3 port made with 2to3) on Pyodide inside an xterm.js terminal. `web/webrt.py` keeps the original behaviour: Python 2 integer division, blocking `input()`, `time.sleep`, the Windows `cls`/`color` commands and Windows-style paths. Published by `.github/workflows/pages.yml`.

## Releases

Builds are made by GitHub Actions (`.github/workflows/release.yml`) for macOS, Windows and Linux. Push a tag such as `v1.0` (or run the workflow by hand) and the zipped builds are attached to a GitHub release.

The game is Python 2.7, which GitHub runners no longer ship: Linux builds inside the official `python:2.7` Docker image, Windows installs it with Chocolatey, and macOS builds on an Intel runner (`macos-15-intel`) with the official installer (that job is allowed to fail). The macOS build is for Intel Macs.

To play from source: `python2.7 briga_de_estudante.py`.
