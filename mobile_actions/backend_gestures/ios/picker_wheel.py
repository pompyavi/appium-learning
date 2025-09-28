import time
from pathlib import Path

from appium import webdriver
from appium.options.ios import XCUITestOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


def init_appium_driver():
    options = XCUITestOptions()
    app_location = Path(__file__).resolve().parents[3] / 'resources' / 'UIKitCatalog-iphonesimulator.app'
    options.app = str(app_location)
    #options.udid = '1E43896F-F5AD-40B7-B9D0-850002A281D2'
    options.udid = '35170BBA-9D23-44E3-A82C-7853A12EEDC6'
    options.new_command_timeout = 3000

    server_url = 'http://127.0.0.1:4723'
    appium_driver = webdriver.Remote(server_url, options=options)

    return appium_driver


if __name__ == '__main__':

    driver = init_appium_driver()
    element = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Picker View')
    element.click()

    red = AppiumBy.IOS_PREDICATE, 'name == "Red color component value"'
    green = AppiumBy.IOS_PREDICATE, 'name == "Green color component value"'
    blue = AppiumBy.IOS_PREDICATE, 'name == "Blue color component value"'

    red_element = driver.find_element(*red)
    green_element = driver.find_element(*green)
    blue_element = driver.find_element(*blue)

    while red_element.text != '105':
        driver.execute_script('mobile: selectPickerWheelValue', {
            'elementId': red_element.id,
            'order': 'next',
            'offset': 0.15,
        })

    while green_element.text != '190':
        driver.execute_script('mobile: selectPickerWheelValue', {
            'elementId': green_element.id,
            'order': 'previous',
            'offset': 0.15,
        })
