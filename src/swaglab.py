from locators.locators import SwagLabLocators
from src.base import BasePage


class SwagLab(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def login(self, credentials):
        username = credentials["username"]
        password = credentials["password"]
        self.fill_text(SwagLabLocators.username_loc, username)
        self.fill_text(SwagLabLocators.password_loc, password)
        self.click(SwagLabLocators.loginbtn_loc)
        has_producttext = self.is_elem_displayed(SwagLabLocators.producttext_loc)
        return has_producttext

    def logout(self):
        self.click(SwagLabLocators.hammerbar_loc)
        self.click(SwagLabLocators.logoutbtn_loc)
        is_loginbtn = self.is_elem_displayed(SwagLabLocators.loginbtn_loc)
        return is_loginbtn

    def addtocart(self):
        self.click(SwagLabLocators.addtocart_loc)
        cartview = self.is_elem(SwagLabLocators.cartwithquantity_loc)
        return cartview

    def place_order(self, records):
        firstname = records["firstname"]
        lastname = records["lastname"]
        zipcode = records["zipcode"]
        self.click(SwagLabLocators.viewcart_loc)
        self.click(SwagLabLocators.checkout_loc)
        self.fill_text(SwagLabLocators.firstname_loc, firstname)
        self.fill_text(SwagLabLocators.lastname_loc, lastname)
        self.fill_text(SwagLabLocators.zipcode_loc, zipcode)
        self.click(SwagLabLocators.continuebtn_loc)
        self.click(SwagLabLocators.finish_loc)
        has_thankyou = self.is_elem_displayed(SwagLabLocators.thankyou_loc)
        return has_thankyou
