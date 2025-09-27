import time
from pathlib import Path

from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.options.ios import XCUITestOptions
from appium.webdriver.common.appiumby import AppiumBy


def create_session(platform):

    if platform == 'android':

        options = UiAutomator2Options()

        app_location = Path(__file__).resolve().parents[1] / 'resources' / 'ApiDemos-debug.apk'
        options.app = str(app_location)
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

def basic_action_android(driver):
    print("Appium driver initialized successfully.")

    # content-description attribute
    text = AppiumBy.ACCESSIBILITY_ID, 'Views'
    text_element = driver.find_element(*text)
    print(text_element.text)
    text_element.click()

    list_element = driver.find_element(by=AppiumBy.ID, value='android:id/list')

    driver.execute_script("mobile: swipeGesture", {
        "elementId": list_element.id,
        "direction": "up",
        "percent": 0.75
        }
    )

    text_fields = AppiumBy.ACCESSIBILITY_ID, "TextFields"
    edit_text = AppiumBy.ID, "io.appium.android.apis:id/edit"

    text_field_element = driver.find_element(*text_fields)
    text_field_element.click()

    edit_text_element = driver.find_element(*edit_text)
    edit_text_element.send_keys("Hello World")
    time.sleep(2)
    print(edit_text_element.text)
    print(edit_text_element.get_attribute('text'))
    edit_text_element.clear()


def basic_ios_android(driver):
    print("Appium driver initialized successfully.")

    # content-description attribute
    text = AppiumBy.ACCESSIBILITY_ID, 'Text Fields'
    text_element = driver.find_element(*text)
    print(text_element.text)
    text_element.click()

    edit_text = AppiumBy.XPATH, '(//XCUIElementTypeTextField[@value="Placeholder text"])[1]'
    edit_text_element = driver.find_element(*edit_text)
    print(edit_text_element.text) # fetches value attribute
    edit_text_element.send_keys('testing')
    edit_text_element.clear()



if __name__ == "__main__":

    #basic_action_android(create_session('android'))
    basic_ios_android(create_session('ios'))




    #driver.quit()