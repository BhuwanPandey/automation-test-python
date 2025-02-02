import pytest

from src.swaglab import SwagLab


class TestLoginLogout:

    @pytest.fixture(autouse=True)
    def set_driver(self, driver):
        self.driver = driver
    
    @pytest.mark.order(1)
    def test_login(self):
        credentials = {
            "username":'standard_user',
            "password":'secret_sauce'
        }
        hasproducttext = SwagLab(self.driver).login(credentials)
        assert hasproducttext , "Not able to Login"
    
    @pytest.mark.order(-1)
    def test_logout(self):
        is_logintbn = SwagLab(self.driver).logout()
        assert is_logintbn , "Not able to  Logout"
