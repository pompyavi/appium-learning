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


if __name__ == '__main__':

    driver = create_session('android')
    driver.activate_app(app_id='io.appium.android.apis')

    wait = WebDriverWait(driver, timeout=10)
    views_locator = AppiumBy.ACCESSIBILITY_ID, 'Views'
    views_element = wait.until(EC.visibility_of_element_located(views_locator))
    views_element.click()

    can_scroll_more = True

    while can_scroll_more:
        can_scroll_more = driver.execute_script('mobile: scrollGesture',
                                                {
                                                      'left': 150,
                                                      'top': 400,
                                                      'width': 500,
                                                      'height': 900,
                                                    'direction': 'down',
                                                      'percent': 0.75
                                              })

    can_scroll_more = True
    while can_scroll_more:
        can_scroll_more = driver.execute_script('mobile: scrollGesture',
                                                {
                                                      'left': 150,
                                                      'top': 2800,
                                                      'width': 500,
                                                      'height': 900,
                                                    'direction': 'up',
                                                      'percent': 0.75
                                              })





