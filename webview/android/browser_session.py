import time

from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def create_android_session():

    options = UiAutomator2Options()
    options.set_capability('platformName', 'Android')
    options.set_capability('automationName', 'UiAutomator2')
    options.set_capability('avd', 'Pixel_9_Pro_XL')
    options.set_capability('browserName', 'Chrome')
    options.chromedriver_executable = '/Users/poulomimitra/PycharmProjects/appium-learning/resources/chromedriver-mac-arm64/chromedriver'

    server_url = 'http://127.0.0.1:4723'
    driver = webdriver.Remote(options=options, command_executor=server_url)

    return driver

if __name__ == "__main__":
    driver = create_android_session()
    print("Appium driver initialized successfully.")

    driver.get('https://www.tesla.com/')
