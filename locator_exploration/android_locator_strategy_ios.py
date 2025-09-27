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

    # Using different locator strategies to find elements

    # accessibility id. If not set it is same as name. Name gets value from label. label is same as static text
    print('Finding element with ACCESSIBILITY_ID')
    element = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Activity Indicators')
    print(f'{element.text=}')
    print(f'{element.get_attribute('name')=}')

    print('==================================================')

    # name attribute
    print('Finding element with ID')
    element = driver.find_element(by=AppiumBy.ID, value='Alert Views')
    print(f'{element.get_attribute('value')=}')

    print('==================================================')

    print('Finding element with XPATH')
    element = driver.find_element(by=AppiumBy.XPATH, value='//XCUIElementTypeStaticText[@name="Page Control"]')
    print(element.get_attribute('label'))
    print(element.text)

    print('==================================================')

    # Type attribute
    print('Finding element with CLASS_NAME')
    element = driver.find_elements(by=AppiumBy.CLASS_NAME, value='XCUIElementTypeStaticText')[10]
    print(element.get_attribute('name'))
    print(element.text)

    print('==================================================')

    # name works with iOS
    print('Finding element with NAME')
    element = driver.find_element(by=AppiumBy.NAME, value='Stack Views')#InvalidSelectorError: Locator Strategy 'name' is not supported for this session
    print(element.get_attribute('traits'))
    print(element.text)


    #driver.quit()