import time

from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.options.ios import XCUITestOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def create_android_session():

    options = XCUITestOptions()
    options.browser_name = 'Safari'
    options.udid = 'CB89D8B8-A6F8-4F37-9AB4-917F75207931'
    options.new_command_timeout = 300
    options.simulator_startup_timeout = 300

    server_url = 'http://127.0.0.1:4723'
    driver = webdriver.Remote(options=options, command_executor=server_url)

    return driver

if __name__ == "__main__":
    driver = create_android_session()
    print("Appium driver initialized successfully.")

    driver.get('https://www.tesla.com/')
