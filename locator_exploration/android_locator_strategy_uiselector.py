from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy


def init_appium_driver():
    options = UiAutomator2Options()
    options.set_capability('platformName', 'Android')
    options.set_capability('automationName', 'UiAutomator2')
    options.set_capability('uuid', 'RZ8W807X4RL')
    options.set_capability('appPackage', 'io.appium.android.apis')
    options.set_capability('appActivity', 'io.appium.android.apis.ApiDemos')

    server_url = 'http://127.0.0.1:4723'
    appium_driver = webdriver.Remote(server_url, options=options)

    return appium_driver

if __name__ == "__main__":
    driver = init_appium_driver()
    print("Appium driver initialized successfully.")

    # description -> content-desc
    # https://code2test.com/appium-tutorial/how-to-use-uiselector-in-appium/
    element = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value='new UiSelector().description("Accessibility")')
    print(element.text)
    print(element.get_attribute('class'))



    #driver.quit()