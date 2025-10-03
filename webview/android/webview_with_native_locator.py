import time
from pathlib import Path
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

def create_android_session():
    options = UiAutomator2Options()
    options.avd = 'Pixel_9_Pro_XL'
    options.new_command_timeout = 3000

    server_url = 'http://127.0.0.1:4723'
    appium_driver = webdriver.Remote(server_url, options=options)

    return appium_driver

if __name__ == "__main__":
    driver = create_android_session()
    print("Appium driver initialized successfully.")
    driver.activate_app(app_id='io.appium.android.apis')

    wait = WebDriverWait(driver, 10)
    wait.until(ec.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Views'))).click()

    driver.execute_script('mobile: swipeGesture',
                          {
                              'left': 150,
                              'top': 400,
                              'width': 500,
                              'height': 1500,
                              'direction': 'up',
                              'percent': 0.75
                          })


    element = wait.until(ec.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'WebView2')))
    element.click()

    webview_ele = wait.until(ec.visibility_of_element_located((AppiumBy.XPATH, '//android.widget.TextView[@text = "This page is a Second Selenium sandbox"]')))
    webview_text = wait.until(ec.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'i_am_a_textbox')))

    webview_text.send_keys('Hello')
    print(webview_ele.text)



