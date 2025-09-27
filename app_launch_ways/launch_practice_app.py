from pathlib import Path

from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.options.common import AppiumOptions
from appium.options.ios import XCUITestOptions


def create_session(platform):

    if platform == 'android':

        options = UiAutomator2Options()

        app_location = Path(__file__).resolve().parents[1] / 'resources' / 'ApiDemos-debug.apk'
        options.app = str(app_location)

        options.udid = 'RZ8W807X4RL'

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





create_session('ios')

