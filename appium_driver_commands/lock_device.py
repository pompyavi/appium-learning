import time

from appium import webdriver
from appium.options.android import UiAutomator2Options


def create_android_session():

    options = UiAutomator2Options()
    options.set_capability('uuid', 'RZ8W807X4RL')
    options.unlock_type = 'pin'
    options.unlock_key = '1234'
    server_url = 'http://127.0.0.1:4723'
    driver = webdriver.Remote(options=options, command_executor=server_url)

    return driver

if __name__ == "__main__":
    driver = create_android_session()
    print("Appium driver initialized successfully.")

    driver.activate_app(app_id='io.appium.android.apis')
    #time.sleep(5)
    driver.lock(-1)  # Lock the device for 5 seconds
    print(driver.is_locked())
    time.sleep(5)
    driver.unlock()