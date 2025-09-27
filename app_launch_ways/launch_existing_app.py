from appium import webdriver
from appium.options.android import UiAutomator2Options

options = UiAutomator2Options()

#options.set_capability('udid','RZ8W807X4RL')
options.set_capability('appPackage', 'io.appium.android.apis')
# options.set_capability('appActivity', 'io.appium.android.apis.ApiDemos')
options.app_activity = 'io.appium.android.apis.graphics.BitmapMesh'
options.avd = 'Pixel_9_Pro_XL'
options.avd_launch_timeout = 120000

server_url = 'http://127.0.0.1:4723'

appium_driver = webdriver.Remote(server_url, options=options)