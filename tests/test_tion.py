from tion import TionApi, Breezer, Zone, MagicAir
import copy
from time import sleep


def test_api_init(api: TionApi):
    assert api.authorization, "Authorisation failed!"
    assert api._data, "No data got!!"


# def test_api_getting_data_interval(api: TionApi):
#     api.get_data()
#     time1 = api._data.connection.last_packet_time
#     api.get_data()
#     time2 = api._data.connection.last_packet_time
#     assert time1 == time2, "Api must update data no more than once per second!"
#     sleep(2)
#     api.get_data()
#     time3 = api._data.connection.last_packet_time
#     assert time3 > time2, "Api must update data once per second!"


def test_zone_init(zone: Zone):
    assert zone.valid, "Data not loaded properly!"


def test_zone_send(zone: Zone):
    zone_prev = copy.deepcopy(zone)
    zone.mode = "auto" if zone.mode == "manual" else "manual"
    zone.target_co2 = 900 if zone.target_co2 != 900 else 901
    zone.send()
    sleep(3)  # wait for update
    zone.load()
    assert zone.mode != zone_prev.mode, "Failed to set zone mode!"
    assert zone.mode != zone_prev.target_co2, "Failed to set zone mode!"
    zone_prev.send()  # return to prev values
    sleep(3)
    zone.load()
    assert zone_prev.mode == zone.mode, "Failed to return mode to previous value!"
    assert zone_prev.target_co2 == zone.target_co2, "Failed to return co2 to previous value!"


def test_breezer_init(breezer: Breezer):
    assert breezer.valid, "Data not loaded properly!"


def test_breezer_manual_send(breezer: Breezer, zone: Zone):
    zone_mode_prev = zone.mode
    if zone.mode != "manual":
        zone.mode = "manual"
        zone.send()
        sleep(3)
    breezer_prev = copy.deepcopy(breezer)
    breezer.is_on = True if not breezer.is_on else False
    breezer.heater_enabled = True if not breezer.heater_enabled else False
    breezer.t_set = 15 if breezer.t_set != 15 else 14
    breezer.speed = 1 if breezer.speed != 1 else 2
    breezer.send()
    sleep(3)  # wait for update
    breezer.load()
    assert breezer.is_on != breezer_prev.is_on, "Failed to set breezer is_on!"
    assert breezer.heater_enabled != breezer_prev.heater_enabled, "Failed to set breezer heater_enabled!"
    assert breezer.t_set != breezer_prev.t_set, "Failed to set breezer t_set!"
    assert breezer.speed != breezer_prev.speed, "Failed to set breezer speed!"
    breezer_prev.send()  # return to prev values
    sleep(3)
    breezer.load()
    assert breezer.is_on == breezer_prev.is_on, "Failed to set breezer is_on!"
    assert breezer.heater_enabled == breezer_prev.heater_enabled, "Failed to set breezer heater_enabled!"
    assert breezer.t_set == breezer_prev.t_set, "Failed to set breezer t_set!"
    assert breezer.speed == breezer_prev.speed, "Failed to set breezer speed!"
    if zone.mode != zone_mode_prev:
        zone.mode = zone_mode_prev
        zone.send()
        sleep(3)


def test_breezer_auto_send(breezer: Breezer, zone: Zone):
    zone_mode_prev = zone.mode
    if zone.mode != "auto":
        zone.mode = "auto"
        zone.send()
        sleep(3)
    breezer_prev = copy.deepcopy(breezer)
    breezer.speed_max_set = 6 if breezer.speed_max_set != 6 else 5
    breezer.speed_min_set = 0 if breezer.speed_min_set != 0 else 1
    breezer.send()
    sleep(3)  # wait for update
    breezer.load()
    assert breezer.speed_max_set != breezer_prev.speed_max_set, "Failed to set breezer speed_max_set!"
    assert breezer.speed_min_set != breezer_prev.speed_min_set, "Failed to set breezer speed_min_set!"
    breezer_prev.send()  # return to prev values
    sleep(3)
    breezer.load()
    assert breezer.speed_max_set == breezer_prev.speed_max_set, "Failed to set breezer speed_max_set!"
    assert breezer.speed_min_set == breezer_prev.speed_min_set, "Failed to set breezer speed_min_set!"
    if zone.mode != zone_mode_prev:
        zone.mode = zone_mode_prev
        zone.send()
        sleep(3)


def test_magicair_init(magicair: MagicAir):
    assert magicair.valid, "Data not loaded properly!"
