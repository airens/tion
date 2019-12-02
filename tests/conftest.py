import pytest
import os
from tion import TionApi, Breezer, Zone, MagicAir


@pytest.fixture
def api_no_saved_auth() -> TionApi:
    email, password = os.environ.get("TION_AUTH").split(',')
    return TionApi(email, password, save_auth=False)


@pytest.fixture
def api() -> TionApi:
    email, password = os.environ.get("TION_AUTH").split(',')
    return TionApi(email, password)


@pytest.fixture
def zone(api: TionApi) -> Zone:
    return api.get_zones(name_part="гостиная")[0]

@pytest.fixture
def breezer(api: TionApi) -> Breezer:
    return api.get_devices(name_part="breezer 3s")[0]


@pytest.fixture
def breezer_manual(breezer: Breezer) -> Breezer:
    breezer.zone.mode = "manual"
    breezer.zone.send()
    assert breezer.zone.mode == "manual", "Couldn't set breezer zone mode to manual!"
    return breezer


@pytest.fixture
def breezer_auto(breezer: Breezer) -> Breezer:
    breezer.zone.mode = "auto"
    breezer.zone.send()
    assert breezer.zone.mode == "auto", "Couldn't set breezer zone mode to auto!"
    return breezer


@pytest.fixture
def magicair(api: TionApi) -> MagicAir:
    return api.get_devices(name_part="magic")[0]
