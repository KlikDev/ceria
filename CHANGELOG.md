# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/)
and this project adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html).

<!-- insertion marker -->
## [0.11.2](https://github.com/pawamoy/ceria/releases/tag/0.11.2) - 2022-04-17

<small>[Compare with 0.11.1](https://github.com/pawamoy/ceria/compare/0.11.1...0.11.2)</small>

### Bug Fixes
- Don't crash when trying to compute a download's name ([c0cfbce](https://github.com/pawamoy/ceria/commit/c0cfbcee852c452e91e079f8f3be387918b3b919) by Timothée Mazzucotelli). [Issue #68](https://github.com/pawamoy/ceria/issues/68), [#103](https://github.com/pawamoy/ceria/issues/103)


## [0.11.1](https://github.com/pawamoy/ceria/releases/tag/0.11.1) - 2021-12-17

<small>[Compare with 0.11.0](https://github.com/pawamoy/ceria/compare/0.11.0...0.11.1)</small>

### Bug Fixes
- Fix checking arguments of add-torrent and add-metalink ([fa9ede5](https://github.com/pawamoy/ceria/commit/fa9ede5fcbeb8aa09e925e2ae213ae6548908ea7) by Timothée Mazzucotelli).


## [0.11.0](https://github.com/pawamoy/ceria/releases/tag/0.11.0) - 2021-12-17

<small>[Compare with 0.10.4](https://github.com/pawamoy/ceria/compare/0.10.4...0.11.0)</small>

### Features
- Support passing options and position from the command-line ([3ec3673](https://github.com/pawamoy/ceria/commit/3ec36732e3aebd298185ce125f1cb4c48f9b5e75) by jonnieey). [PR #93](https://github.com/pawamoy/ceria/pull/93)
- Support transparency (use default colors) ([ff35d2b](https://github.com/pawamoy/ceria/commit/ff35d2b572cac2a371550016d6d4b4863a635fbd) by blackCauldron7). [PR #84](https://github.com/pawamoy/ceria/pull/84)
- Support aria2c input files with options ([a603961](https://github.com/pawamoy/ceria/commit/a60396180d48c52cde384096ad8f2a592342f0b0) by jonnieey). [Issue #70](https://github.com/pawamoy/ceria/issues/70), [PR #91](https://github.com/pawamoy/ceria/pull/91)

### Code Refactoring
- Reorganize CLI commands ([3497d2b](https://github.com/pawamoy/ceria/commit/3497d2b219bea4017644d384c1df08298f364689) by Timothée Mazzucotelli).


## [0.10.4](https://github.com/pawamoy/ceria/releases/tag/0.10.4) - 2021-01-06

<small>[Compare with 0.10.3](https://github.com/pawamoy/ceria/compare/0.10.3...0.10.4)</small>

### Bug Fixes
- Always depend on appdirs (not only in tui extra) ([7f36a04](https://github.com/pawamoy/ceria/commit/7f36a04aaece28acf16a61fe7b87a5869aab3ac5) by Timothée Mazzucotelli).


## [0.10.3](https://github.com/pawamoy/ceria/releases/tag/0.10.3) - 2020-12-30

<small>[Compare with 0.10.2](https://github.com/pawamoy/ceria/compare/0.10.2...0.10.3)</small>

### Bug Fixes
- Add missing extra dependencies for tui group ([60f9e69](https://github.com/pawamoy/ceria/commit/60f9e696c3961b0e91c6bfd3b4ba816f0b7bd6cd) by Timothée Mazzucotelli).


## [0.10.2](https://github.com/pawamoy/ceria/releases/tag/0.10.2) - 2020-12-30

<small>[Compare with 0.10.1](https://github.com/pawamoy/ceria/compare/0.10.1...0.10.2)</small>

### Bug Fixes
- Add back missing commands aliases ([cd25e78](https://github.com/pawamoy/ceria/commit/cd25e787179055d6d6e271c1d64f61fef9c9cf4f) by Timothée Mazzucotelli).


## [0.10.1](https://github.com/pawamoy/ceria/releases/tag/0.10.1) - 2020-11-28

<small>[Compare with 0.10.0](https://github.com/pawamoy/ceria/compare/0.10.0...0.10.1)</small>

### Bug Fixes
- Fix missing toml dependency ([4d385f1](https://github.com/pawamoy/ceria/commit/4d385f1811c0eacfb3741ab958d59fe1b9b505f6) by Timothée Mazzucotelli).


## [0.10.0](https://github.com/pawamoy/ceria/releases/tag/0.10.0) - 2020-11-28

<small>[Compare with 0.9.1](https://github.com/pawamoy/ceria/compare/0.9.1...0.10.0)</small>

### Bug Fixes
- Security fix (requests vulnerability) ([17777c0](https://github.com/pawamoy/ceria/commit/17777c009912c2ac252f260842376039c321aca9) by Timothée Mazzucotelli).
- Fix TUI crashes when removing files for downloads without ([c066971](https://github.com/pawamoy/ceria/commit/c066971f13d6806e180473cf2fd15733fa7d9543) by jonnieey).
- Fix TUI crash when URI is longer than screen width ([dc1f11b](https://github.com/pawamoy/ceria/commit/dc1f11be5e74f9ae0e8fc9f8e77e689ad1c21ba5) by Jonnieey).

### Code Refactoring
- Use purge instead of autopurge in interface ([045b4d3](https://github.com/pawamoy/ceria/commit/045b4d34c039ce44e497a1fd545834a723cc8b9e) by Timothée Mazzucotelli).
- Various quality improvements ([e8aca77](https://github.com/pawamoy/ceria/commit/e8aca774243259152f7cce3ee9aea84502027d0e) by Timothée Mazzucotelli).
- Remove deprecated subcommands ([da9664c](https://github.com/pawamoy/ceria/commit/da9664c95286b11d0a506b5ff6e8f7b851add515) by Timothée Mazzucotelli).
- Move `add` command logic into API ([6f36116](https://github.com/pawamoy/ceria/commit/6f361163b73f7ac8d0a76308b14331383c8fecd7) by Timothée Mazzucotelli).

### Features
- Add new downloads from TUI (with the `a` key by default) ([052a0ae](https://github.com/pawamoy/ceria/commit/052a0aebe9da6e92eaea17ad64fa0ab747e069bb) by Jonnieey).
- Add user configuration ([f3512b7](https://github.com/pawamoy/ceria/commit/f3512b72504745ad7d0ade260ca08b3ddab65db5) by Jonnieey). References: [#60](https://github.com/pawamoy/ceria/issues/60), [#62](https://github.com/pawamoy/ceria/issues/62)
- Add `retry_downloads` API method ([77678f5](https://github.com/pawamoy/ceria/commit/77678f5717e3f5d8d9f8d3edb76935210a997072) by Jonnieey).


## [0.9.1](https://github.com/pawamoy/ceria/releases/tag/0.9.1) - 2020-05-14

<small>[Compare with 0.9.0](https://github.com/pawamoy/ceria/compare/0.9.0...0.9.1)</small>

### Bug Fixes
- Forbid version of `asciimatics` below 1.11.0 ([c305b9b](https://github.com/pawamoy/ceria/commit/c305b9b88cd9156ccad2dd5a5a1e7725c2b08ca3) by Timothée Mazzucotelli). References: [#57](https://github.com/pawamoy/ceria/issues/57)


## [0.9.0](https://github.com/pawamoy/ceria/releases/tag/0.9.0) - 2020-04-08

<small>[Compare with 0.8.1](https://github.com/pawamoy/ceria/compare/0.8.1...0.9.0)</small>

### Features
- Add a timeout to client's requests ([26bb0b6](https://github.com/pawamoy/ceria/commit/26bb0b67fc02f9e98dd25924cb4a885313fa43ff) by Timothée Mazzucotelli). Related issues/PRs: [#52](https://github.com/pawamoy/ceria/issues/52)
- Add the `is_torrent` property to `download` objects. ([0c7760e](https://github.com/pawamoy/ceria/commit/0c7760e768d1e26ae022d80d5722e923143dca33) by Timothée Mazzucotelli). Related issues/PRs: [#53](https://github.com/pawamoy/ceria/issues/53)
- `download.bittorrent` returns `none` if no "bittorrent" key present ([74106fe](https://github.com/pawamoy/ceria/commit/74106fe82ec4afecdccdf10a1f615ddab9712821) by Timothée Mazzucotelli). Related issues/PRs: [#53](https://github.com/pawamoy/ceria/issues/53)<br>
  **BREAKING CHANGE:** this could be a breaking change if your code does not check if `download.bittorrent` is an instance of `BitTorrent` before accessing its attributes.


## [0.8.1](https://github.com/pawamoy/ceria/releases/tag/0.8.1) - 2020-03-29

<small>[Compare with 0.8.0](https://github.com/pawamoy/ceria/compare/0.8.0...0.8.1)</small>

### Fixed
- Fix download `followed_by` not being reset properly when updating ([19510a7](https://github.com/pawamoy/ceria/commit/19510a7c4caca85356927f0bbb8e7292d8b1780c)).
  See [issue #51](https://github.com/pawamoy/ceria/issues/51).


## [0.8.0](https://github.com/pawamoy/ceria/releases/tag/0.8.0) - 2020-03-27

<small>[Compare with 0.7.1](https://github.com/pawamoy/ceria/compare/0.7.1...0.8.0)</small>

### Added
- Add a `live` property to `Download` ([98a8504](https://github.com/pawamoy/ceria/commit/98a850442a09d33c3a6e4d85e2d19fcc5dc0cb15)).
  See [issue #44](https://github.com/pawamoy/ceria/issues/44).

### Fixed
- Re-apply `pywal` color theme if any when screen is resized ([3e19deb](https://github.com/pawamoy/ceria/commit/3e19deb8eb6e9303fac01389486f92a8ce388be0)).


## [0.7.1](https://github.com/pawamoy/ceria/releases/tag/0.7.1) - 2020-01-18

<small>[Compare with 0.7.0](https://github.com/pawamoy/ceria/compare/0.7.0...0.7.1)</small>

### Fixed
- Fix Windows OSError when checking if path exists ([2a17c75](https://github.com/pawamoy/ceria/commit/2a17c75842cf38dc3b89b33de8a244a6f1a955c1)).
  See [issue #41](https://github.com/pawamoy/ceria/issues/41).


## [0.7.0](https://github.com/pawamoy/ceria/releases/tag/0.7.0) - 2019-12-14

<small>[Compare with 0.6.0](https://github.com/pawamoy/ceria/compare/0.6.0...0.7.0)</small>

### BREAKING CHANGES
- Set asciimatics dependency as optional (`ceria[tui]`) ([95a404c](https://github.com/pawamoy/ceria/commit/95a404c46d8a9666dc9d2d348b14ca376121a738)).
  **Starting at version 0.7.0, you need to install ceria with the `tui` extra if you want to use the interactive interface.**
  Example: `pip install ceria[tui]`.

### Removed
- Remove deprecated `purge` and `purge_all` methods from API ([6baf63c](https://github.com/pawamoy/ceria/commit/6baf63c7cbf70491e13d2622a52b053ed00f5b8d)).
- Remove deprecated `purge` CLI command ([8668c8d](https://github.com/pawamoy/ceria/commit/8668c8dfd58b038f4ba595f238c32561080f2537)).

### Misc
- Add makefile rule to bundle app with `pyinstaller` ([7eabbb4](https://github.com/pawamoy/ceria/commit/7eabbb4bcd06f47b685ee4009da903ea79b3f9c9)).


## [0.6.0](https://github.com/pawamoy/ceria/releases/tag/0.6.0) - 2019-10-20

<small>[Compare with 0.5.2](https://github.com/pawamoy/ceria/compare/0.5.2...0.6.0)</small>

### BREAKING CHANGES
- Default command when calling `ceria` without arguments is now `top` instead of `show`.

### Added
- Add command "add", and allow multiple parameters for "add-" commands ([12f8667](https://github.com/pawamoy/ceria/commit/12f866722ed20a90dcbaaf6627240974d29e3557)).
- Add `-f, --from-file FILE` option to `add` commands ([63a137d](https://github.com/pawamoy/ceria/commit/63a137dc51ee85ccfe461dd9c2be1c5a54a03c87)).
- Add a clean parameter to API.remove to delete aria2 control file ([d4b9a51](https://github.com/pawamoy/ceria/commit/d4b9a512134832f89d538df9d0d6cc2b6c81050c)).

### Changed
- Commands add-magnet, add-torrent and add-metalink are now called add-magnets, add-torrents and add-metalinks.
  Previous names are added as aliases to maintain backward compatibility.
  
### Deprecated
- Functions `cli.subcommand_add_magnet`, `cli.subcommand_add_torrent` or `cli.subcommand_add_metalink`
  are deprecated in favor of their pluralized names,
  `cli.subcommand_add_magnets`, `cli.subcommand_add_torrents` or `cli.subcommand_add_metalinks`,
  and will be removed in version 0.9.0.

### Fixed
- Always force remove files when removing download ([7283a15](https://github.com/pawamoy/ceria/commit/7283a15cbea37e01403c2b7a56208cae1bfa57e7)).
- Don't try to fetch download when GID is None ([8970385](https://github.com/pawamoy/ceria/commit/89703859f1a4d8aa3fefe8097f1390155f74395d)).


## [0.5.2](https://github.com/pawamoy/ceria/releases/tag/0.5.2) - 2019-10-15

<small>[Compare with 0.5.1](https://github.com/pawamoy/ceria/compare/0.5.1...0.5.2)</small>

### Fixed
- Don't crash when trying to remove a single file ([14114c1](https://github.com/pawamoy/ceria/commit/14114c1fdb4a7de6ca4d24e488151a7b6864bb94)).


## [0.5.1](https://github.com/pawamoy/ceria/releases/tag/0.5.1) - 2019-10-15

<small>[Compare with 0.5.0](https://github.com/pawamoy/ceria/compare/0.5.0...0.5.1)</small>

### Fixed
- Fix interface exit (oops) ([ca4adc5](https://github.com/pawamoy/ceria/commit/ca4adc5a8c3d195131f65b6799fd9d3b7eb4491b)).


## [0.5.0](https://github.com/pawamoy/ceria/releases/tag/0.5.0) - 2019-10-15

<small>[Compare with 0.4.0](https://github.com/pawamoy/ceria/compare/0.4.0...0.5.0)</small>

### BREAKING CHANGES
- Commands finishing with `-all` were removed. Use their equivalent with the `-a` or `--all` option.
  Example: `ceria pause-all` becomes `ceria pause --all`.

### Added
- Add log path global option ([7103e0b](https://github.com/pawamoy/ceria/commit/7103e0b32656e8209d6c4c6d3f3f95f41eb75148)).

### Fixed
- Interface does not crash anymore when trying to remove a completed/failed download ([157e137](https://github.com/pawamoy/ceria/commit/157e137730e49c4e290e34371dfbd5fc464491db)).
  See issue [GH-31](https://github.com/pawamoy/ceria/issues/31).
- Run extra arguments-checks for aliases as well ([cb70dae](https://github.com/pawamoy/ceria/commit/cb70dae023997d3b2df789bb101678936a56fe31)).
  See issue [GH-15](https://github.com/pawamoy/ceria/issues/15).


## [0.4.0](https://github.com/pawamoy/ceria/releases/tag/0.4.0) - 2019-10-13

<small>[Compare with 0.3.0](https://github.com/pawamoy/ceria/compare/0.3.0...0.4.0)</small>

### Added
- Add interactive interface (top command) (last commit: [d8a2db2](https://github.com/pawamoy/ceria/commit/d8a2db2b2dba19c42056dbdb854cc6fc1a0b8efc)).
  Run the interactive interface with `ceria top`. Hit "h" to show help.
  The interface is not finished, but I'm releasing it now to get early feedback.
- API: add option to remove files as well when removing downloads ([981dcc0](https://github.com/pawamoy/ceria/commit/981dcc015f8baef5b3d2f0230b27376f482442fa)).

### Fixed
- Fix Download.move_up method (it was doing the inverse) ([96a287a](https://github.com/pawamoy/ceria/commit/96a287ab4e563c27ffb56afbccc8901c02e4a9f2)).

## [0.3.0](https://github.com/pawamoy/ceria/releases/tag/0.3.0) - 2019-10-11

<small>[Compare with 0.2.5](https://github.com/pawamoy/ceria/compare/0.2.5...0.3.0)</small>

### Added
- Add listen subcommand ([09195ae](https://github.com/pawamoy/ceria/commit/09195aeb0146d8e3f4108c8fc7b7548485d1417b)).
- Implement notifications listener ([33ee9ae](https://github.com/pawamoy/ceria/commit/33ee9ae72811a18b4430e5ff163e1df113b209af)).
- Provide function to enable/configure logger ([8620a09](https://github.com/pawamoy/ceria/commit/8620a0928cdb9def7c661baf819eb4aea8d085c9)).

### Fixed
- Fix API pause_all and resume_all methods ([0bf2209](https://github.com/pawamoy/ceria/commit/0bf2209553e138387d2597900f2a182275bd0fa5)).
  See issue [GH-24](https://github.com/pawamoy/ceria/issues/24).


## [0.2.5](https://github.com/pawamoy/ceria/releases/tag/0.2.5) - 2019-08-09

<small>[Compare with 0.2.4](https://github.com/pawamoy/ceria/compare/0.2.4...0.2.5)</small>

### Fixed
- Use path for name when download is metadata ([d18af50](https://github.com/pawamoy/ceria/commit/d18af5033d93fbc94b3c9d85e2fbb9e320328747)).


## [0.2.4](https://github.com/pawamoy/ceria/releases/tag/0.2.4) - 2019-08-09

<small>[Compare with 0.2.3](https://github.com/pawamoy/ceria/compare/0.2.3...0.2.4)</small>

### Fixed
- Don't cause exception when download name is not ready ([604a0ab](https://github.com/pawamoy/ceria/commit/604a0abb4db3acd6f061449b9667c44861b8843e)).


## [0.2.3](https://github.com/pawamoy/ceria/releases/tag/0.2.3) - 2019-08-08

<small>[Compare with 0.2.2](https://github.com/pawamoy/ceria/compare/0.2.2...0.2.3)</small>

### Added
- Add some aliases ([14ef63a](https://github.com/pawamoy/ceria/commit/14ef63afb39b60ee88201857520efd1dc350d410)).
- Add file moving and purge ability to Download class ([08d129a](https://github.com/pawamoy/ceria/commit/08d129a429874fde313f45720bfd44cfb7ee1b49)).
- Add move/copy files methods to API ([e1d3994](https://github.com/pawamoy/ceria/commit/e1d3994ed7969ba8a54edb3fe6bbf5cc2e1deb99)).
- Combine -all commands to normal ones, with -a, --all option, keep old ones as deprecated ([e5d287c](https://github.com/pawamoy/ceria/commit/e5d287c7dfaaffa6c2999d261744f09c7806b5ce) and [939402f](https://github.com/pawamoy/ceria/commit/939402f62539ef97aea2ffa2db1cc93b48f68d20)).
- Improve exceptions handling with `loguru` ([e0ded18](https://github.com/pawamoy/ceria/commit/e0ded18c50945f9706bd34e4d021f4ebe030a043)).

### Fixed
- Cast return value in get method with argument ([5ee651a](https://github.com/pawamoy/ceria/commit/5ee651a17e28502903103959bf1b7b9abd71eb60)).
- Fix Download.name and always initialize struct arguments to empty dictionaries ([874deb9](https://github.com/pawamoy/ceria/commit/874deb98b0e61f1c5e115253974ca525ba313fdf)).
- Pass exceptions when download result cannot be removed ([9a7659e](https://github.com/pawamoy/ceria/commit/9a7659e6763173b90f94b0711a65e43aec047c9c)).


## [0.2.2](https://github.com/pawamoy/ceria/releases/tag/0.2.2) - 2019-02-21

<small>[Compare with 0.2.1](https://github.com/pawamoy/ceria/compare/0.2.1...0.2.2)</small>

### Documented
- Add configuration documentation ([9525743](https://github.com/pawamoy/ceria/commit/952574341e55d53e6d5657d33cc4f47ffdb1f14e)).
- Add information in README ([840c4b5](https://github.com/pawamoy/ceria/commit/840c4b5b56470d9966370c184e7af7f8b6a85da0)).
- Add credits ([6900eb2](https://github.com/pawamoy/ceria/commit/6900eb2d596dea2244601969014442e42b2393c2)).

### Fixed
- Fix format of secret in params ([e01fd9c](https://github.com/pawamoy/ceria/commit/e01fd9cd6af257cbc0feb5248ce86b1177d7151e)).
- Print warning when connection to remote fails ([57287fb](https://github.com/pawamoy/ceria/commit/57287fb5ed0436925aea6f75baebdae58907467d)).


## [0.2.1](https://github.com/pawamoy/ceria/releases/tag/0.2.1) - 2019-01-23

<small>[Compare with 0.2.0](https://github.com/pawamoy/ceria/compare/0.2.0...0.2.1)</small>

### Fixed
- Fix commands not being mapped properly ([f9a0b29](https://github.com/pawamoy/ceria/commit/f9a0b29e51520d94494367fccf2486da4c377f3a)).


## [0.2.0](https://github.com/pawamoy/ceria/releases/tag/0.2.0) - 2019-01-23

<small>[Compare with 0.1.7](https://github.com/pawamoy/ceria/compare/0.1.7...0.2.0)</small>

Version 0.2.0 adds subcommands to the CLI tool. The package now also provides documentation and tests.
Various improvements and fixes. Status is still alpha, things might break!

### Added
- Add subcommands to CLI ([93821cc](https://github.com/pawamoy/ceria/commit/93821cc672e062554c3aa508e8dc490aab73c518)).

### Fixed
- Fix Download following API refactor ([37f3b71](https://github.com/pawamoy/ceria/commit/37f3b71ad261b73846855c57f6fb97ff373c6550)).
- Fix encoding torrent content to base64/utf-8 ([a17eb92](https://github.com/pawamoy/ceria/commit/a17eb92a6050b0dd007b74d47fb13cb6ecc21b8a)).


## [0.1.7](https://github.com/pawamoy/ceria/releases/tag/0.1.7) - 2018-12-29

<small>[Compare with 0.1.6](https://github.com/pawamoy/ceria/compare/0.1.6...0.1.7)</small>

### Fixed
- Fix specifier for Python version (allow 3.6+) ([f451df9](https://github.com/pawamoy/ceria/commit/f451df91ac76430543a990816019324acfbc67bb)).
  See issue [GH-1](https://github.com/pawamoy/ceria/issues/1).


## [0.1.6](https://github.com/pawamoy/ceria/releases/tag/0.1.6) - 2018-12-26

<small>[Compare with 0.1.5](https://github.com/pawamoy/ceria/compare/0.1.5...0.1.6)</small>

### Added
- Add methods to Download to improve usability ([5fe4649](https://github.com/pawamoy/ceria/commit/5fe4649d81eb8101e99e34145fe137284397dbe6)).
- Add refetch method for download objects ([c87e752](https://github.com/pawamoy/ceria/commit/c87e7521987a5d24d180fe7aabf0d850d05bb0c2)).
- Add upload speed to display ([5c8be6c](https://github.com/pawamoy/ceria/commit/5c8be6cda8951b5b4b959404a0c3999b5f71d522)).

### Misc
- Handle return code and exceptions better ([14f47f8](https://github.com/pawamoy/ceria/commit/14f47f83b29eab547b64010de1e14366e13b2072)).
- Improve JSONRPC errors messages, use defaults ([a3692dc](https://github.com/pawamoy/ceria/commit/a3692dce1ae76ed02f8f635a53a47bf513726b48)).
- Write documentation ([f5c9ffd](https://github.com/pawamoy/ceria/commit/f5c9ffd3fb0b1094d90979b278f7e1990178d07f)).


## [0.1.5](https://github.com/pawamoy/ceria/releases/tag/0.1.5) - 2018-12-20

<small>[Compare with 0.1.4](https://github.com/pawamoy/ceria/compare/0.1.4...0.1.5)</small>

### Misc
- Improve basic display ([84ae386](https://github.com/pawamoy/ceria/commit/84ae386de0115d4b8ea49b5f5053262ee78aa175)).


## [0.1.4](https://github.com/pawamoy/ceria/releases/tag/0.1.4) - 2018-12-20

<small>[Compare with 0.1.3](https://github.com/pawamoy/ceria/compare/0.1.3...0.1.4)</small>

### Added
- Add download speed and eta to display ([1dd23bc](https://github.com/pawamoy/ceria/commit/1dd23bcc927a1c8c3bd1ce7fbb83bdf65703fbe4)).

### Fixed
- Fix error handling in client.post ([7f9e8aa](https://github.com/pawamoy/ceria/commit/7f9e8aa4f00a5c96755726d5d5521caf96339000)).

### Misc
- Use dynamic get/set attr for options ([fa0b962](https://github.com/pawamoy/ceria/commit/fa0b96277175c5267f1e7ed27c8143cb4f65ef14)).
- Use properties ([6efe3a6](https://github.com/pawamoy/ceria/commit/6efe3a6774878a0ab2fbdfb6f70991841e006fcb)).


## [0.1.3](https://github.com/pawamoy/ceria/releases/tag/0.1.3) - 2018-12-17

<small>[Compare with 0.1.0](https://github.com/pawamoy/ceria/compare/0.1.0...0.1.3)</small>

### Misc
- Various tweaks and improvements for packaging the application.


## [0.1.0](https://github.com/pawamoy/ceria/releases/tag/0.1.0) - 2018-12-17

<small>[Compare with first commit](https://github.com/pawamoy/ceria/compare/878497bb3eacfdd6e385e33470a4b99d2df3d3bd...0.1.0)</small>

### Added
- Add pyproject.toml for black configuration ([dacb85e](https://github.com/pawamoy/ceria/commit/dacb85e3c9b0e94f4816f8be5cfc501693c4e35a)).
- Add README ([683086c](https://github.com/pawamoy/ceria/commit/683086c32e0411cef0996f17df7ed31a60cbdb12)).

### Misc
- Package with Poetry! ([648d0a5](https://github.com/pawamoy/ceria/commit/648d0a5b3c68d3a06b5a0f7957b5861e42d7279d)).
- Hello Git(Hub|Lab) ([878497b](https://github.com/pawamoy/ceria/commit/878497bb3eacfdd6e385e33470a4b99d2df3d3bd)).
