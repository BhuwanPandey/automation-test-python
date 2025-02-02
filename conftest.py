import pytest

from src.driver import Driver


@pytest.fixture(scope="class")
def driver():
    driver = Driver().getAndroidDriver()
    return driver

