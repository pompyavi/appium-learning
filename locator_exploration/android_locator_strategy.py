from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By


def init_appium_driver():
    options = UiAutomator2Options()
    options.set_capability('platformName', 'Android')
    options.set_capability('automationName', 'UiAutomator2')
    options.set_capability('uuid', 'RZ8W807X4RL')
    options.set_capability('appPackage', 'io.appium.android.apis')
    options.set_capability('appActivity', 'io.appium.android.apis.ApiDemos')
    options.new_command_timeout = 3000

    server_url = 'http://127.0.0.1:4723'
    appium_driver = webdriver.Remote(server_url, options=options)

    return appium_driver

if __name__ == "__main__":
    driver = init_appium_driver()
    print("Appium driver initialized successfully.")

    print('==================================================')

    # Using different locator strategies to find elements

    # content-description attribute
    print('Finding element with ACCESSIBILITY_ID')
    element = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Accessibility')
    print(f'{element.text=}')
    print(f'{element.get_attribute('class')=}')

    print('==================================================')

    # resource-id attribute
    print('Finding element with ID')
    element = driver.find_element(by=AppiumBy.ID, value='android:id/text1')
    print(f'{element.get_attribute('content-desc')=}')

    print('==================================================')

    print('Finding element with XPATH')
    element = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@content-desc="Animation"]')
    print(element.get_attribute('content-desc'))
    print(element.text)

    print('==================================================')

    print('Finding element with CLASS_NAME')
    element = driver.find_elements(by=AppiumBy.CLASS_NAME, value='android.widget.TextView')[0]
    print(element.get_attribute('content-desc'))
    print(element.text)

    print('==================================================')

    print('Finding element with NAME')
    element = driver.find_element(by=By.NAME, value='Chronometer')#InvalidSelectorError: Locator Strategy 'name' is not supported for this session
    print(element.get_attribute('content-desc'))
    print(element.text)


    #driver.quit()