import pytest
import os
from tion import TionApi, BreezerParams
from tion.tion import Tion


@pytest.fixture
def tion() -> TionApi:
    auth_code = os.environ.get("TION_AUTH")
    return TionApi(auth_code)

@pytest.fixture
def data(tion: TionApi) -> Tion:
    return tion.get_data()