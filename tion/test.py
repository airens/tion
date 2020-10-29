import os
import logging
from tion import TionApi, Breezer, Zone, MagicAir, Thermostat

logging.basicConfig(level=logging.DEBUG)

# initialization api with no saving auth information (for test only)
email = "chainstain@mail.ru"
password = "123242_tion"
api = TionApi(email, password, auth_fname=None)
# getting current co2 level from magicair
magicair = api.get_devices(name_part="magic")[0]
print(f"magicair.co2: {magicair.co2}")
# getting breezer
#breezer = api.get_devices(name_part="breezer")[0]
#print(f"breezer: {breezer}")
#print(f"breezer: {breezer.zone.mode}")
thermostat = api.get_devices(name_part="danfoss")[0]
print(f"thermostat: {thermostat}")
print(f"thermostat: {thermostat.temperature}")
#print(f"thermostat: {thermostat.t_set}")
