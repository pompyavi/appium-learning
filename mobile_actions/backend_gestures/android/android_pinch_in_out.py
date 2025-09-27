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
        options.app_package = 'com.google.android.apps.maps'
        options.app_activity = 'com.google.android.maps.MapsActivity'

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
    time.sleep(2)
    skip = driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@text="SKIP"]')
    skip.click()

    time.sleep(4)

    driver.execute_script('mobile: pinchOpenGesture',
                          {
                              'left': 300,
                              'top': 560,
                              'width': 400,
                              'height': 320,
                              'percent': 0.75
                          })
    time.sleep(2)
    driver.execute_script('mobile: pinchCloseGesture',
                          {
                              'left': 300,
                              'top': 560,
                              'width': 400,
                              'height': 320,
                              'percent': 0.75
                          })




