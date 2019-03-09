# Tion Api
This package provides API to control Tion breezer
## Getting authorization code:
- Go to <https://magicair.tion.ru/dashboard/overview>
- Login if needed
- Enter *Debug mode* (usually F12) in browser
- Open *Network* tab and change some parameter of your breezer via web-interface
- Look into header of request and copy *Authorization* field 
## Usage:
```python
# initialization
tion = TionApi({auth_code})
# getting current CO2 data from MagicAir
data = tion.get_data()
print(data.zones[1].devices[0].data.co2)
# manual mode for zone 1:
tion.set_auto_mode(data.zones[1], False)
breezer_params = BreezerParams()
breezer_params.is_on = True
breezer_params.speed = 1
breezer_params.heater_enabled = True
breezer_params.t_set = 20  # set temperature for heater
tion.set_breezer_params(data.zones[1].devices[1], breezer_params)
# auto mode with CO2 level 600
tion.set_auto_mode(data.zones[1], True, 600)
# cnanging speed range to 1-4 in auto mode
breezer_params = BreezerParams()
breezer_params.speed_min_set = 1
breezer_params.speed_max_set = 4
tion.set_breezer_params(data.zones[1].devices[1], breezer_params)
```
