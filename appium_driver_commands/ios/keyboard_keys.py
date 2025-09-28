import time
from pathlib import Path

from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.options.ios import XCUITestOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def create_ios_session():
    options = XCUITestOptions()
    options.udid = '35170BBA-9D23-44E3-A82C-7853A12EEDC6'
    options.new_command_timeout = 3000

    server_url = 'http://127.0.0.1:4723'
    appium_driver = webdriver.Remote(server_url, options=options)

    return appium_driver

if __name__ == "__main__":
    driver = create_ios_session()
    print("Appium driver initialized successfully.")

    app_path = Path(__file__).resolve().parents[2] / 'resources' / 'UIKitCatalog-iphonesimulator.app'
    driver.install_app(app_path=str(app_path))
    driver.activate_app(app_id='com.example.apple-samplecode.UICatalog')
    time.sleep(5)

    driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Text Fields').click()

    driver.find_element(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeTextField[`value == "Placeholder text"`][1]').click()
    print(driver.is_keyboard_shown())

    driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'q').click()
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'w').click()
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'e').click()
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'r').click()
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, 't').click()
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'y').click()
    driver.hide_keyboard()
    print(driver.is_keyboard_shown())

    time.sleep(2)

    driver.execute_script('mobile: pressButton',
                          {
                              'name': 'home'
                          })

