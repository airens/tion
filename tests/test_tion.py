from tion import TionApi, Breezer, Zone, MagicAir, main
import copy
from time import sleep


zone_prev: Zone = None
breezer_prev: Breezer = None


TESTS_DELAY = 1


def test_api_init_no_saved_auth(api_no_saved_auth: TionApi):
    assert api_no_saved_auth.authorization, "Authorisation failed!"
    assert api_no_saved_auth._data, "No data got!"
    sleep(TESTS_DELAY)  # let the server "rest"


def test_tion_api_bad_auth_fname(api_bad_auth_fname: TionApi):
    assert api_bad_auth_fname.get_data(force=True) is True, "Should've get data!"
    sleep(TESTS_DELAY)  # let the server "rest"


def test_api_init(api: TionApi):
    assert api.authorization, "Authorisation failed!"
    assert api._data, "No data got!!"
    sleep(TESTS_DELAY)  # let the server "rest"


def test_api_repr(api: TionApi):
    assert repr(api)


def test_tion_api_need_new_auth(api: TionApi):
    api.authorization = ""
    assert api.get_data(force=True) is True, "New auth should've received!"
    sleep(TESTS_DELAY)  # let the server "rest"


def test_tion_api_wait_for_task_returns_false_on_timeout_0_6(api: TionApi):
    assert api.wait_for_task("asdf", max_time=0.6) is False, "Must return False on timeout!"
    sleep(TESTS_DELAY)  # let the server "rest"


def test_tion_api_wait_for_task_returns_false_on_bad_task_id(api: TionApi):
    assert api.wait_for_task("asdf") is False, "Must return False on lack of bad task_id!"
    sleep(TESTS_DELAY)  # let the server "rest"


def test_zone_init(zone: Zone):
    global zone_prev
    zone_prev = copy.deepcopy(zone)  # save previous zone state
    assert zone.valid, "Data not loaded properly!"
    sleep(TESTS_DELAY)  # let the server "rest"


def test_zone_load(zone: Zone):
    assert zone.load() is True, "Failed to load zone data!"
    sleep(TESTS_DELAY)  # let the server "rest"


def test_zone_properties_and_repr(zone: Zone):
    assert zone.guid == zone._guid
    assert zone.name == zone._name
    assert repr(zone)


def test_zone_not_send_if_not_valid(zone: Zone):
    zone._guid = None
    assert zone.send() is False, "Should'nt have sent not valid zone!"
    sleep(TESTS_DELAY)  # let the server "rest"


def test_zone_mode_send(zone: Zone):
    new_mode = "auto" if zone.mode == "manual" else "manual"
    zone.mode = new_mode
    zone.send()
    assert zone.mode == new_mode, "Failed to set zone mode!"
    sleep(TESTS_DELAY)  # let the server "rest"


def test_zone_co2_send(zone: Zone):
    new_co2 = 900 if zone.target_co2 != 900 else 901
    zone.target_co2 = new_co2
    zone.send()
    assert zone.target_co2 == new_co2, "Failed to set target co2!"
    sleep(TESTS_DELAY)  # let the server "rest"


def test_breezer_init(breezer: Breezer):
    global breezer_prev
    breezer_prev = copy.deepcopy(breezer)  # save previous zone state
    assert breezer.valid, "Data not loaded properly!"
    sleep(TESTS_DELAY)  # let the server "rest"


def test_breezer_properties_and_repr(breezer: Breezer):
    assert breezer.name == breezer._name
    assert breezer.guid == breezer._guid
    assert breezer.t_in == breezer._t_in
    assert breezer.t_out == breezer._t_out
    assert breezer.filter_need_replace == breezer._filter_need_replace
    assert breezer.data_valid == breezer._data_valid
    assert breezer.is_on == breezer._is_on
    assert breezer.heater_installed == breezer._heater_installed
    assert breezer.t_min == breezer._t_min
    assert breezer.t_max == breezer._t_max
    assert breezer.speed_limit == breezer._speed_limit
    assert repr(breezer)


def test_breezer_not_send_if_not_valid(breezer: Breezer):
    breezer._guid = None
    assert breezer.send() is False, "Should'nt have sent not valid breezer!"
    sleep(TESTS_DELAY)  # let the server "rest"


def test_breezer_load(breezer: Breezer):
    assert breezer.load() is True, "Failed to load breezer data!"
    sleep(TESTS_DELAY)  # let the server "rest"


def test_breezer_manual_send_heater_enabled(breezer_manual: Breezer):
    new_heater_enabled = True if not breezer_manual.heater_enabled else False
    breezer_manual.heater_enabled = new_heater_enabled
    breezer_manual.send()
    sleep(TESTS_DELAY)  # let the server "rest"


def test_breezer_manual_send_t_set(breezer_manual: Breezer):
    new_t_set = 15 if breezer_manual.t_set != 15 else 14
    breezer_manual.t_set = new_t_set
    assert breezer_manual.t_set == new_t_set, "Failed to set breezer t_set!"
    sleep(TESTS_DELAY)  # let the server "rest"


def test_breezer_manual_send_speed(breezer_manual: Breezer):
    new_speed = 1 if breezer_manual.speed != 1 else 2
    breezer_manual.speed = new_speed
    breezer_manual.send()
    assert breezer_manual.speed == new_speed, "Failed to set breezer speed!"
    sleep(TESTS_DELAY)  # let the server "rest"


def test_breezer_auto_send_speed_max_set(breezer_auto: Breezer):
    new_speed_max_set = breezer_auto.speed_limit if breezer_auto.speed_max_set != breezer_auto.speed_limit \
        else breezer_auto.speed_limit - 1
    breezer_auto.speed_max_set = new_speed_max_set
    breezer_auto.send()
    assert breezer_auto.speed_max_set == new_speed_max_set, "Failed to set breezer speed_max_set!"
    sleep(TESTS_DELAY)  # let the server "rest"


def test_breezer_auto_send_speed_min_set(breezer_auto: Breezer):
    new_speed_min_set = 1 if breezer_auto.speed_min_set != 1 else 2
    breezer_auto.speed_min_set = new_speed_min_set
    breezer_auto.send()
    assert breezer_auto.speed_min_set == new_speed_min_set, "Failed to set breezer speed_min_set!"
    sleep(TESTS_DELAY)  # let the server "rest"


def test_breezer_manual_send_gate(breezer_manual: Breezer):
    new_gate = 0 if breezer_manual.gate != 0 else 2
    breezer_manual.gate = new_gate
    breezer_manual.send()
    assert breezer_manual.gate == new_gate, "Failed to set breezer gate!"
    sleep(TESTS_DELAY)  # let the server "rest"


def test_magicair_init(magicair: MagicAir):
    assert magicair.valid, "Data not loaded properly!"
    sleep(TESTS_DELAY)  # let the server "rest"


def test_magicair_properties_and_repr(magicair: MagicAir):
    assert magicair.name == magicair._name
    assert magicair.guid == magicair._guid
    assert magicair.co2 == magicair._co2
    assert magicair.temperature == magicair._temperature
    assert magicair.humidity == magicair._humidity
    assert repr(magicair)


def test_magicair_load(magicair: MagicAir):
    assert magicair.load()
    sleep(TESTS_DELAY)  # let the server "rest"


def test_example():
    main()


def test_restore_breezer():
    assert breezer_prev.send(), "Failed to send previous breezer parameters!"  # return to prev values
    sleep(TESTS_DELAY)  # let the server "rest"


def test_restore_zone():
    assert zone_prev.send(), "Failed to send previous zone parameters!"  # return to prev values
    sleep(TESTS_DELAY)  # let the server "rest"
