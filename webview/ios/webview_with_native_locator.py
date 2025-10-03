import time
from pathlib import Path
from appium import webdriver
from appium.options.ios import XCUITestOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

def create_ios_session():
    options = XCUITestOptions()
    options.udid = '35170BBA-9D23-44E3-A82C-7853A12EEDC6'
    options.new_command_timeout = 3000

    server_url = 'http://127.0.0.1:4723'
    appium_driver = webdriver.Remote(server_url, options=options)

    return appium_driver

if __name__ == "__main__":
    driver = create_ios_session()
    print("Appium driver initialized successfully.")

    app_path = Path(__file__).resolve().parents[2] / 'resources' / 'UIKitCatalog-iphonesimulator.app'
    driver.install_app(app_path=str(app_path))
    driver.activate_app(app_id='com.example.apple-samplecode.UICatalog')

    driver.execute_script('mobile: scroll',
                          {
                              'direction': 'down'
                          })

    wait = WebDriverWait(driver, 10)
    wait.until(ec.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Web View'))).click()

    element = wait.until(ec.visibility_of_element_located(
        (AppiumBy.IOS_PREDICATE, 'name == "This is HTML content inside a WKWebView."')))

    print(element.text)
    print(element.get_attribute('label'))


