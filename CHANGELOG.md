# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.9.0]

### Added
- getChangelog()
- !changelog command

## [0.8.5] - 2023-04-11

### Deprecated
- Command online() replaced with status()

### Changed
- Formatted main.py using Black formatter

### Bugfixes
- Removed all log messages containing variables (may not be callable?)

## [0.8.4] - 2023-04-11

### Changed
- Temporarily disable automatic versioning due to possible bug(s)

### Bugfixes
- Removed most log messages to attempt to alleviate error(s)

## [0.8.3] - 2023-04-11

### Added
- .vscode settings directory to .gitignore

## [0.8.2] - 2023-04-11

### Added
- Logging support for many (all?) commands

## [0.8.1] - 2023-04-11

### Fixed
- Semantic version now increments automatically (from this file)

### Added
- getVer() function to source the semantic version info from CHANGELOG.md

## [0.8.0] - 2023-04-11

### Added
- requirements.txt
- Content to README.md

### Changed
- Edited CHANGELOG.md for formatting

## [0.7.7] - 2023-04-11

### Added
- CHANGELOG.md

### Changed
- Updated .gitignore
