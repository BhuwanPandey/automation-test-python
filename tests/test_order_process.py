import pytest

from src.swaglab import SwagLab


class TestPlaceOrder:
    
    @pytest.fixture(autouse=True)
    def set_driver(self, driver):
        self.driver = driver

    def test_add_cart(self):
        elem = SwagLab(self.driver).addtocart()
        assert elem and str(elem.text) == '1', 'Not Added to Cart'

    def test_place_order(self):
        records = {
            'firstname':'bhuwan',
            'lastname':'pandey',
            'zipcode':12345
        }
        has_thankyou = SwagLab(self.driver).place_order(records)
        assert has_thankyou , "Ordered Successfull!"
