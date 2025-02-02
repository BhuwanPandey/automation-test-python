from appium.webdriver.common.appiumby import AppiumBy


class SwagLabLocators:
    username_loc = (
        AppiumBy.XPATH,
        '//android.widget.EditText[@content-desc="test-Username"]',
    )
    password_loc = (
        AppiumBy.XPATH,
        '//android.widget.EditText[@content-desc="test-Password"]',
    )
    loginbtn_loc = (AppiumBy.XPATH, '//android.widget.TextView[@text="LOGIN"]')
    producttext_loc = (AppiumBy.XPATH, '//android.widget.TextView[@text="PRODUCTS"]')
    hammerbar_loc = (
        AppiumBy.XPATH,
        '//android.view.ViewGroup[@content-desc="test-Menu"]/android.view.ViewGroup/android.widget.ImageView',
    )
    logoutbtn_loc = (AppiumBy.XPATH, '//android.widget.TextView[@text="LOGOUT"]')
    addtocart_loc = (
        AppiumBy.XPATH,
        '(//android.widget.TextView[@text="ADD TO CART"])[1]',
    )
    viewcart_loc = (
        AppiumBy.XPATH,
        '//android.view.ViewGroup[@content-desc="test-Cart"]/android.view.ViewGroup/android.widget.ImageView',
    )
    cartwithquantity_loc = (AppiumBy.XPATH, '//android.widget.TextView[@text="1"]')
    checkout_loc = (AppiumBy.XPATH, '//android.widget.TextView[@text="CHECKOUT"]')
    firstname_loc = (
        AppiumBy.XPATH,
        '//android.widget.EditText[@content-desc="test-First Name"]',
    )
    lastname_loc = (
        AppiumBy.XPATH,
        '//android.widget.EditText[@content-desc="test-Last Name"]',
    )
    zipcode_loc = (
        AppiumBy.XPATH,
        '//android.widget.EditText[@content-desc="test-Zip/Postal Code"]',
    )
    continuebtn_loc = (AppiumBy.XPATH, '//android.widget.TextView[@text="CONTINUE"]')
    finish_loc = (AppiumBy.XPATH, '//android.widget.TextView[@text="FINISH"]')
    thankyou_loc = (
        AppiumBy.XPATH,
        '//android.widget.TextView[@text="THANK YOU FOR YOU ORDER"]',
    )
