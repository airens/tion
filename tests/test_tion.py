from tion import TionApi, BreezerParams
from tion.tion import Tion
from time import sleep

def test_init(tion: TionApi):
    assert tion.authorization, "authorization must be set!"
    assert tion.headers, "headers must be set!"


saved_params = {}


def test_get_data(data: Tion):
    assert data.zones[1].devices[0].data.co2, "Failed to get co2!"
    assert data.zones[1].devices[0].data.temperature, "Failed to get temperature!"
    assert data.zones[1].devices[0].data.humidity, "Failed to get humidity!"
    saved_params["mode"] = data.zones[1].mode.current
    saved_params["co2_set"] = data.zones[1].mode.auto_set.co2
    saved_params["is_on"] = data.zones[1].devices[1].data.is_on
    saved_params["heater_enabled"] = data.zones[1].devices[1].data.heater_enabled
    saved_params["t_set"] = data.zones[1].devices[1].data.t_set
    saved_params["speed"] = data.zones[1].devices[1].data.speed
    saved_params["speed_min_set"] = data.zones[1].devices[1].data.speed_min_set
    saved_params["speed_max_set"] = data.zones[1].devices[1].data.speed_max_set

def return_prev_params(tion, data):
    tion.set_auto_mode(data.zones[1], saved_params["mode"], saved_params["co2_set"])
    params = BreezerParams()
    params.is_on = saved_params["is_on"]
    params.heater_enabled = saved_params["heater_enabled"]
    params.t_set = saved_params["t_set"]
    params.speed = saved_params["speed"]
    params.speed_min_set = saved_params["speed_min_set"]
    params.speed_max_set = saved_params["speed_max_set"]

    tion.set_breezer_params(data.zones[1].devices[1], params)


def test_set(tion: TionApi, data: Tion):
    new_mode = "manual" if saved_params["mode"] == "auto" else "auto"
    new_co2 = 600 if saved_params["co2_set"] != 600 else 700
    new_min_speed = 0 if saved_params["speed_min_set"] > 0 else 1
    new_max_speed = 6 if saved_params["speed_max_set"] < 6 else 5
    new_is_on = False if saved_params["is_on"] else True
    new_heater_enabled = False if saved_params["heater_enabled"] else True
    new_t_set = 15 if saved_params["heater_enabled"] != 15 else 20
    new_speed = 3 if saved_params["speed"] != 3 else 2
    tion.set_auto_mode(data.zones[1], True if new_mode == "auto" else False, new_co2)
    params = BreezerParams()
    params.is_on = new_is_on
    params.heater_enabled = new_heater_enabled
    params.t_set = new_t_set
    params.speed = new_speed
    params.speed_max_set = new_max_speed
    params.speed_min_set = new_min_speed
    tion.set_breezer_params(data.zones[1].devices[1], params)
    sleep(2)
    data = tion.get_data()
    assert new_mode == data.zones[1].mode.current, "Failed to set auto mode!"
    assert new_is_on == data.zones[1].devices[1].data.is_on, "Failed to set is_on!"
    assert new_heater_enabled == data.zones[1].devices[1].data.heater_enabled, "Failed to set heater_enabled!"
    assert new_t_set == data.zones[1].devices[1].data.t_set, "Failed to set t_set!"
    assert new_speed == data.zones[1].devices[1].data.speed, "Failed to set speed!"
    assert new_min_speed == data.zones[1].devices[1].data.speed_min_set, "Failed to set speed_min_set!"
    assert new_max_speed == data.zones[1].devices[1].data.speed_max_set, "Failed to set speed_max_set!"
    return_prev_params(tion, data)
