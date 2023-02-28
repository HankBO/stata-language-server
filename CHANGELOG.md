# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog][keepachangelog],
and this project adheres to [Semantic Versioning][semver].

## [1.1.3]

- Dependency updates: need pygls 1.0.1, drop support for Python 3.6
- Changed settings loading method.

## [1.1.2]

- Fixed python version checking
- Updated illustration of python path referenced for this extension in README.md

## [1.1.1]

- Fixed python version checking

## [1.1.0]

- Fixed ineffect settings
- Added feature: taking effect instangly after changing a setting
- Added settings: `enableCompletion`, `enableDocstring`, `enableStyleChecking`
- Updated docstring reading with `lru_cache`
- Updated commands reading from one json file
- Other fixes

## [1.0.3]

- Updated images in README.md

## [1.0.2]

- Fixed node modules are not included

## [1.0.1]

- Fixed gif links in README.MD
- Changed package.json: use esbuild to bundle extension
- Updated .vscodeignore

## [1.0.0]

- Added feature: codestyle diagnostics
- Added Python installation checking
- Added automatic installation of pygls
- Added VSCode Settings: Max Line Length and Indent Space
- Added ThirdPartyNotices.txt, icon.png
- Updated README.md

## [0.2.1]

- Fixed package import name in /client;
- Fixed vscode version in package.json

## 0.2.0 - Aug, 28th, 2021

- Added Feature `Goto Definition`
- Upload all markdown docstring
- Added Gif demo images
- Updated README.md

## 0.1.0

- Initial Version

[keepachangelog]: https://keepachangelog.com/en/1.0.0/
[semver]: https://semver.org/spec/v2.0.0.html

[1.1.3]: https://github.com/HankBO/stata-language-server/compare/v1.1.2...v1.1.3
[1.1.2]: https://github.com/HankBO/stata-language-server/compare/v1.1.1...v1.1.2
[1.1.1]: https://github.com/HankBO/stata-language-server/compare/v1.1.0...v1.1.1
[1.1.0]: https://github.com/HankBO/stata-language-server/compare/v1.0.3...v1.1.0
[1.0.3]: https://github.com/HankBO/stata-language-server/compare/v1.0.2...v1.0.3
[1.0.2]: https://github.com/HankBO/stata-language-server/compare/v1.0.1...v1.0.2
[1.0.1]: https://github.com/HankBO/stata-language-server/compare/v1.0.0...v1.0.1
[1.0.0]: https://github.com/HankBO/stata-language-server/compare/v0.2.1...v1.0.0
[0.2.1]: https://github.com/HankBO/stata-language-server/compare/v0.2.0...v0.2.1
