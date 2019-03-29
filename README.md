# Tion Api
This package provides API to control Tion breezer
## Usage:
```python
import os
from time import sleep
from tion import TionApi, Breezer, Zone, MagicAir
# initialization api
email, password = os.environ.get("TION_AUTH").split(',')
api = TionApi(email, password)
# getting current co2 level from magicair
magicair = api.get_devices(name_part="magic")[0]
print(magicair.co2)
sleep(3)
# setting manual mode for zone Гостиная
zone = api.get_zones(name_part="Гостиная")[0]
zone.mode = "manual"
zone.send()
sleep(3)
zone.load()
assert zone.mode == "manual"  # making sure that mode is set correctly
# turning off breezer
breezer = api.get_devices(name_part="breezer")[0]
breezer.is_on = False
breezer.send()
sleep(3)
breezer.load()
assert zone.mode == "manual"  # making sure that mode is set correctly
# setting auto mode for zone Гостиная
zone.mode = "auto"
zone.send()
sleep(3)
zone.load()
assert zone.mode == "auto"
# setting breezer minimum speed to 3 and maximum to 6
breezer.speed_min_set = 3
breezer.speed_max_set = 6
breezer.send()
sleep(3)
breezer.load()
assert breezer.speed_min_set == 3
```
