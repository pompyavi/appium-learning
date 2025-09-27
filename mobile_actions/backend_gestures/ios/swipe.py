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

    wait = WebDriverWait(driver, 10)
    element = wait.until(ec.visibility_of_element_located(
        (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeTable')))

    driver.execute_script('mobile: swipe', {
        'elementId': element.id,
        'direction': 'up'
    })