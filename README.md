# Tion Api
This package provides API to control Tion breezer
## Usage:
```python
import os
import logging
from tion import TionApi, Breezer, Zone, MagicAir

logging.basicConfig(level=logging.INFO)

# initialization api
email, password = os.environ.get("TION_AUTH").split(',')
api = TionApi(email, password, save_auth=False)
# getting current co2 level from magicair
magicair = api.get_devices(name_part="magic")[0]
print(f"magicair.co2: {magicair.co2}")
# getting breezer
breezer = api.get_devices(name_part="breezer")[0]
# setting manual mode for breezer zone
breezer.zone.mode = "manual"
assert breezer.zone.send() is True, "Failed to send zone data"
print(f"breezer.zone.mode: {breezer.zone.mode}")
# setting breezer speed manually
breezer.speed = 3
assert breezer.send() is True, "Failed to send breezer data"
print(f"breezer.is_on: {breezer.is_on} breezer.speed: {breezer.speed}")
# setting air source to outside
breezer.gate = 2
assert breezer.send() is True, "Failed to send breezer data"
print(f"breezer.is_on: {breezer.is_on} breezer.speed: {breezer.speed} breezer.gate: {breezer.gate}")
# setting auto mode for breezer's zone
breezer.zone.mode = "auto"
assert breezer.zone.send() is True, "Failed to send zone data"
print(f"breezer.zone.mode: {breezer.zone.mode}")
# setting breezer minimum speed to 3 and maximum to 6
breezer.speed_min_set = 3
breezer.speed_max_set = 6
assert breezer.send() is True, "Failed to send breezer data"
print(f"breezer.speed_min_set: {breezer.speed_min_set} breezer.speed_max_set: {breezer.speed_max_set}")
```
