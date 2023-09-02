import pytest

from piplinetest.log import setup_logger


@pytest.fixture(scope="session", autouse=True)
def setup_piplne_testlogger():
    setup_logger()
