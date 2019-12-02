# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]
update
usage example
## [0.5] - 2019-01-12

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
