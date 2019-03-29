import pytest
import os
from tion import TionApi, Breezer, Zone, MagicAir


@pytest.fixture
def api() -> TionApi:
    email, password = os.environ.get("TION_AUTH").split(',')
    return TionApi(email, password)


@pytest.fixture
def zone(api: TionApi) -> Breezer:
    return api.get_zones(name_part="гостиная")[0]


@pytest.fixture
def breezer(api: TionApi) -> Breezer:
    return api.get_devices(name_part="breezer 3s")[0]


@pytest.fixture
def magicair(api: TionApi) -> MagicAir:
    return api.get_devices(name_part="magic")[0]
