import time

from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.applicationstate import ApplicationState



def create_android_session():

    options = UiAutomator2Options()
    options.set_capability('uuid', 'emulator-5554')

    server_url = 'http://127.0.0.1:4723'
    driver = webdriver.Remote(options=options, command_executor=server_url)

    return driver

if __name__ == "__main__":
    driver = create_android_session()
    print("Appium driver initialized successfully.")

    driver.execute_script('mobile: activateApp',
                          {'appId': 'io.appium.android.apis'})
    time.sleep(2)
    #driver.terminate_app(app_id='io.appium.android.apis')
    driver.execute_script('mobile: terminateApp',
                          {'appId': 'io.appium.android.apis'})

    state = driver.execute_script('mobile: queryAppState',
                          {'appId': 'io.appium.android.apis'})

    print(f"App state: {state}") # 1 -> NOT_RUNNING
    print(ApplicationState.NOT_RUNNING == state)

    # NOT_INSTALLED = 0
    # NOT_RUNNING = 1
    # RUNNING_IN_BACKGROUND_SUSPENDED = 2
    # RUNNING_IN_BACKGROUND = 3
    # RUNNING_IN_FOREGROUND = 4