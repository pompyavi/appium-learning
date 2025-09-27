from appium import webdriver
from appium.options.android import UiAutomator2Options
from pathlib import Path

app_location = Path(__file__).resolve().parents[1] / 'resources' / 'ApiDemos-debug.apk'
print(app_location)
options = UiAutomator2Options()

options.avd = 'Pixel_9_Pro_XL'
options.avd_launch_timeout = 120000

# have to convert to string because appium expects a string. We can't pass a Path object.
options.set_capability('app', str(app_location))
server_url = 'http://127.0.0.1:4723'

appium_driver = webdriver.Remote(server_url, options=options)