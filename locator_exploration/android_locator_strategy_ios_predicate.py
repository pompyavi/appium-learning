from pathlib import Path

from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.options.ios import XCUITestOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By


def init_appium_driver():
    options = XCUITestOptions()
    app_location = Path(__file__).resolve().parents[1] / 'resources' / 'UIKitCatalog-iphonesimulator.app'
    options.app = str(app_location)
    options.udid = '1E43896F-F5AD-40B7-B9D0-850002A281D2'
    options.new_command_timeout = 3000

    server_url = 'http://127.0.0.1:4723'
    appium_driver = webdriver.Remote(server_url, options=options)

    return appium_driver

if __name__ == "__main__":
    driver = init_appium_driver()
    print("Appium driver initialized successfully.")

    print('==================================================')

    print('Finding element with Predicate')
    element = driver.find_element(by=AppiumBy.IOS_PREDICATE, value="label == 'Text View' AND accessible == TRUE")
    print(f'{element.text=}')
    print(f'{element.get_attribute('name')=}')

    #driver.quit()