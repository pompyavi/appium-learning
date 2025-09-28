import time

from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def create_android_session():

    options = UiAutomator2Options()
    options.set_capability('uuid', 'emulator-5554')
    options.avd = 'Pixel_9_Pro_XL'

    server_url = 'http://127.0.0.1:4723'
    driver = webdriver.Remote(options=options, command_executor=server_url)

    return driver

if __name__ == "__main__":
    driver = create_android_session()
    print("Appium driver initialized successfully.")

    driver.execute_script('mobile: activateApp',
                          {'appId': 'io.appium.android.apis'})

    wait = WebDriverWait(driver, 10)



    views = wait.until(expected_conditions.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, 'Views')))
    views.click()

    list_ele = driver.find_element(AppiumBy.ID, 'android:id/list')

    driver.execute_script('mobile: swipeGesture',
                          {
                                'elementId': list_ele.id,
                                'direction': 'up',
                                'percent': 0.75
                          })

    textfield = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'TextFields')
    textfield.click()

    editText = driver.find_element(AppiumBy.ID, 'io.appium.android.apis:id/edit')
    editText.click()

    print(driver.is_keyboard_shown())

    driver.press_keycode(keycode=30)
    driver.press_keycode(keycode=187) #app switch key

    #driver.hide_keyboard()

