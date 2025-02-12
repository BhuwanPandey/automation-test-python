import pytest

from slack import slack_notify
from src.driver import Driver


@pytest.fixture(scope="class")
def driver():
    driver = Driver().getAndroidDriver()
    return driver

def pytest_runtest_makereport(item, call):
    if call.when == "call":
        if call.excinfo is not None:
            test_name = item.name
            error_msg = str(call.excinfo.value)
            slack_notify(f"TestFail : /n {test_name} -- {error_msg}")

