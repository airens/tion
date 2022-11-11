# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.28] - 2022-11-11
### Fixed
- Обновлена работа с 4S. Параметр `heater_enabled` теперь формируется из `heater_mode`
## [1.27] - 2022-11-10
### Fixed
- Для модели 4S теперь принудительно выставляется `heater_enabled`
- Добавлен скрипт для локальной инсталляции пакета
## [1.26] - 2022-11-10
### Fixed
- исправлена запись логов при ошибке обращения к серверам Tion
## [1.25] - 2021-10-08
### Added
- tion 4S support
## [1.23] - 2021-08-05
### Added
- ability to test some new breezer.send() data options with 'extra_data' param
- added support for 4S model ('heater_mode' parameter is now being sent)
## [1.22] - 2020-05-09
### Fixed
- breezer's valid property is now also checks data_valid  

## [1.21] - 2020-05-09
### Fixed
- issues of 1.20 version 

## [1.20] - 2020-05-09
### Added
- support for O2 breezer and, probably, other new models 

## [1.10] - 2020-05-09
### Added
- support for more than one base station

## [1.00] - 2020-05-09

### Braking changes
- `save_auth` parameter for TionApi replaced with `auth_fname`
### Fixed
- minor issues for correct tests passing
### Added
- the ability to set filename (and path) for auth file
- catching exception while writing auth file and test for it


## [0.71] - 2019-12-24

### Fixed
- bug when air source changed to `inside` after using `send()` function of `Breezer` in manual mode
### Added
- `Breezer` parameter `gate` (air source) now can be controled in `manual` zone mode

## [0.6] - 2019-12-02

### Changed
- `Breezer` parameter `is_on` now can't be set mannualy and calculated automatically depending on the speed
- all parameters of `Zone`, `MagicAir` and `Breezer`, that can't be changed, became `@property`

## [0.5] - 2019-12-01

### Added
- `min_update_interval` option for TionApi class
- `force` parameter for load() functions, which allows to get new data immediately regardless `min_update_interval` option
- verification for `zone_data` and `device_data` in `load()` functions to avoid exceptions if Tion server goes offline
- Breezer parameters:
  - heater_installed
  - t_min
  - t_max
  - speed_limit
- usage example as main() function

### Changed
- print replaced by `_LOGGER`
- `zone` objects in `Breezer` and `MagicAir` classes now `Zone` objects, not just raw data
- headers in `TionApi` now property, to update authorization after init
- new tests made from scratch
- canceled checking `__repr__()` and other hardly reachable places by coverage in tests
