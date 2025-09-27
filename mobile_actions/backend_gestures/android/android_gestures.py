import time
from pathlib import Path

from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.options.ios import XCUITestOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def create_session(platform):

    if platform == 'android':

        options = UiAutomator2Options()
        options.avd = 'Pixel_9_Pro_XL'

        #options.udid = 'RZ8W807X4RL'

    else:

        options = XCUITestOptions()

        app_location = Path(__file__).resolve().parents[1] / 'resources' / 'UIKitCatalog-iphonesimulator.app'
        options.app = str(app_location)
        options.udid = '1E43896F-F5AD-40B7-B9D0-850002A281D2'
        #options.device_name = 'iPhone 16e'
        # options.simulator_startup_timeout

    server_url = 'http://127.0.0.1:4723'
    driver = webdriver.Remote(server_url, options=options)
    return driver

def long_click_gesture(driver):
    driver.activate_app(app_id='io.appium.android.apis')

    wait = WebDriverWait(driver, timeout=10)
    views_locator = AppiumBy.ACCESSIBILITY_ID, 'Views'
    views_element = wait.until(EC.visibility_of_element_located(views_locator))
    views_element.click()

    dd_locator = AppiumBy.ACCESSIBILITY_ID, 'Drag and Drop'
    dd_element = driver.find_element(*dd_locator)
    dd_element.click()

    dot1_locator = AppiumBy.ID, 'io.appium.android.apis:id/drag_dot_1'
    dot1_element = driver.find_element(*dot1_locator)

    driver.execute_script('mobile: longClickGesture',
                          {
                              'elementId': dot1_element.id,
                              'duration': 1000
                          })

def click_gesture(driver):
    driver.activate_app(app_id='io.appium.android.apis')

    wait = WebDriverWait(driver, timeout=10)
    views_locator = AppiumBy.ACCESSIBILITY_ID, 'Views'
    views_element = wait.until(EC.visibility_of_element_located(views_locator))

    driver.execute_script('mobile: clickGesture',
                          {
                              'elementId': views_element.id,
                          })

def drag_drop_gesture(driver):
    driver.activate_app(app_id='io.appium.android.apis')

    wait = WebDriverWait(driver, timeout=10)
    views_locator = AppiumBy.ACCESSIBILITY_ID, 'Views'
    views_element = wait.until(EC.visibility_of_element_located(views_locator))
    views_element.click()

    dd_locator = AppiumBy.ACCESSIBILITY_ID, 'Drag and Drop'
    dd_element = driver.find_element(*dd_locator)
    dd_element.click()


    dot1_locator = AppiumBy.ID, 'io.appium.android.apis:id/drag_dot_1'
    dot1_element = driver.find_element(*dot1_locator)

    dot2_locator = AppiumBy.ID, 'io.appium.android.apis:id/drag_dot_2'
    dot2_element = driver.find_element(*dot2_locator)

    dot_2_rect = dot2_element.rect

    print(dot_2_rect)
    print(dot2_element.location)
    endX = dot_2_rect['x'] + (dot_2_rect['width'] // 2)
    endY = dot_2_rect['y'] + (dot_2_rect['height'] // 2)


    driver.execute_script('mobile: dragGesture',
                          {
                              'elementId': dot1_element.id,
                              'endX': endX,
                              'endY': endY,
                              'speed': 2000
                          })

if __name__ == '__main__':

    driver = create_session('android')
    #long_click_gesture(driver)
    drag_drop_gesture(driver)




