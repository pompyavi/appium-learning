import time

from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.options.ios import XCUITestOptions


def create_ios_session():

    options = XCUITestOptions()
    options.set_capability('udid', 'CE8E7991-0482-462C-B277-9B26ACD16CAC')

    server_url = 'http://127.0.0.1:4723'
    driver = webdriver.Remote(options=options, command_executor=server_url)

    return driver

if __name__ == "__main__":
    driver = create_ios_session()
    print("Appium driver initialized successfully.")

    driver.execute_script('mobile: activateApp',
                          {'bundleId': 'com.example.apple-samplecode.UICatalog'})
    time.sleep(2)

    state = driver.execute_script('mobile: queryAppState',
                                  {'bundleId': 'com.example.apple-samplecode.UICatalog'})

    print(f"App state: {state}")  # 4 -> RUNNING_IN_FOREGROUND

    #driver.terminate_app(app_id='io.appium.android.apis')
    #driver.execute_script('mobile: backgroundApp',{'seconds':8}) # not using seconds args will keep the app in background indefinitely



    driver.background_app(seconds=-1)  # seconds param is mandatory, so we can use -1 to keep the app in background indefinitely
    # if a positive value is passed, the app will be in background for that many seconds and then will be brought back to foreground
    # During that time the script will be waiting till the app is brought to foreground

    time.sleep(5)

    state = driver.query_app_state(app_id='com.example.apple-samplecode.UICatalog')
    print(f"App state: {state}") # 2 -> RUNNING_IN_BACKGROUND_SUSPENDED

    time.sleep(5)

    state = driver.query_app_state(app_id='com.example.apple-samplecode.UICatalog')
    print(f"App state: {state}")  # 2 -> RUNNING_IN_BACKGROUND_SUSPENDED

