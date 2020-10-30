import os
import logging
from tion import TionApi, Breezer, Zone, MagicAir, Thermostat

logging.basicConfig(level=logging.DEBUG)

# initialization api with no saving auth information (for test only)
email = "chainstain@mail.ru"
password = "123242_tion"
api = TionApi(email, password, auth_fname=None)
magicair = api.get_devices(name_part="magic")[0]
breezer = api.get_devices(name_part="breezer")[0]
thermostat = api.get_devices(name_part="danfoss")[0]
print(f"--breezer: {breezer}")
print(f"--breezer: {breezer.zone.mode}")
print(f"--magicair: {magicair}")
print(f"--magicair: {magicair.co2}")
print(f"--thermostat: {thermostat}")
print(f"--thermostat: name {thermostat.name}")
print(f"--thermostat: temperature {thermostat.temperature}")
print(f"--thermostat: t_set {thermostat.t_set}")
#print(f"thermostat: {thermostat.t_set}")

#thermostat.t_set = 25
#assert thermostat.send() is True, "Failed to send thermostat data"
#print(f"--thermostat: temperature {thermostat.temperature}")
#print(f"--thermostat: t_set {thermostat.t_set}")
