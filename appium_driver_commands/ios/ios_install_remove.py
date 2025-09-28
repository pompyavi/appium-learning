import time
from pathlib import Path

from appium import webdriver
from appium.options.ios import XCUITestOptions

options = XCUITestOptions()
options.udid = '35170BBA-9D23-44E3-A82C-7853A12EEDC6'
options.new_command_timeout = 3000

server_url = 'http://127.0.0.1:4723'
appium_driver = webdriver.Remote(server_url, options=options)

app_path = Path(__file__).resolve().parents[2] / 'resources' / 'UIKitCatalog-iphonesimulator.app'
appium_driver.install_app(app_path=str(app_path))
appium_driver.activate_app(app_id='com.example.apple-samplecode.UICatalog')
time.sleep(5)
appium_driver.terminate_app(app_id='com.example.apple-samplecode.UICatalog')
state = appium_driver.query_app_state(app_id='com.example.apple-samplecode.UICatalog')
print(state)
time.sleep(5)

appium_driver.remove_app(app_id='com.example.apple-samplecode.UICatalog')
time.sleep(10)
state = appium_driver.query_app_state(app_id='com.example.apple-samplecode.UICatalog')
print(state)

print(f'is app installed: {appium_driver.is_app_installed(bundle_id='com.example.apple-samplecode.UICatalog')}')
