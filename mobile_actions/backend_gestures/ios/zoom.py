import time
from pathlib import Path

from appium import webdriver
from appium.options.ios import XCUITestOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec



def init_appium_driver():
    options = XCUITestOptions()
    options.bundle_id = 'com.apple.Maps'
    #options.udid = '1E43896F-F5AD-40B7-B9D0-850002A281D2'
    options.udid = '35170BBA-9D23-44E3-A82C-7853A12EEDC6'
    options.new_command_timeout = 3000

    server_url = 'http://127.0.0.1:4723'
    appium_driver = webdriver.Remote(server_url, options=options)

    return appium_driver

if __name__ == '__main__':

    driver = init_appium_driver()
    time.sleep(2)

    driver.execute_script('mobile: tap', {
        'x': 195,
        'y': 475
    })

    driver.execute_script('mobile: tap', {
        'x': 195,
        'y': 63
    })

    driver.execute_script('mobile: pinch', {
        'scale': 15,
        'velocity': 2.2
    })

    element = driver.find_element(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeOther[`name == "ControlContainerViewController.OverlayView"`]')
    driver.execute_script('mobile: pinch', {
        'elementId': element.id,
        'scale': 0.5,
        'velocity': -2.2
    })

