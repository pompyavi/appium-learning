from appium import webdriver
from appium.options.common import AppiumOptions
from appium.options.ios import XCUITestOptions

options = XCUITestOptions()
options.udid = 'CE8E7991-0482-462C-B277-9B26ACD16CAC'
options.bundle_id = 'com.example.apple-samplecode.UICatalog'

server_url = 'http://127.0.0.1:4723'
driver = webdriver.Remote(server_url, options=options)

