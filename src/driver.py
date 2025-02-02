import os

from appium import webdriver
from appium.options.common.base import AppiumOptions


class Driver:
    def getAndroidDriver(self):
        options = AppiumOptions()
        current_dir = os.path.dirname(os.path.abspath(__file__))
        apk_path = os.path.join(current_dir, "sample.apk")
        options.load_capabilities(
            {
                "platformName": "Android",
                "appium:automationName": "uiautomator2",
                "appium:deviceName": "Android",
                "appium:app": apk_path,
                "appium:noReset": True,
                "appium:newCommandTimeout": 600,
                "appium:appWaitActivity": "com.swaglabsmobileapp.*",
            }
        )
        app_driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
        return app_driver
