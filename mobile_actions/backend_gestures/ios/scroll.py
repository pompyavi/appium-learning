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

def scroll_into_view(): # not working
    driver = init_appium_driver()

    time.sleep(5)

    element = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Web View')
    driver.execute_script('mobile: scrollToElement', {
        'elementId': element.id,
        #'direction': 'down',
        #'toVisible': True
    })

def scroll_down():
    driver = init_appium_driver()

    driver.execute_script('mobile: scroll', {
        'direction': 'down'
    })

def scroll_down_parent_element():
    driver = init_appium_driver()
    element = driver.find_element(AppiumBy.IOS_PREDICATE, 'type == "XCUIElementTypeTable"') # element have bounds to scroll
    driver.execute_script('mobile: scroll', {
        'elementId': element.id,
        'direction': 'down'
    })

def scroll_down_parent_child_element():
    driver = init_appium_driver()
    element = driver.find_element(AppiumBy.IOS_PREDICATE, 'type == "XCUIElementTypeTable"') # element have bounds to scroll
    driver.execute_script('mobile: scroll', {
        'elementId': element.id,
        'predicateString': 'name == "Web View"'
    })

if __name__ == '__main__':
    scroll_down_parent_child_element()