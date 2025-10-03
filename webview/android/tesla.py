from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

def android_browser_session():
    options = UiAutomator2Options()
    options.browser_name = 'Chrome'
    options.platform_name = 'Android'
    options.automation_name = 'UiAutomator2'
    options.avd = 'Pixel_9_Pro_XL'
    options.new_command_timeout = 3000
    options.auto_grant_permissions = True
    options.chromedriver_executable = '/Users/poulomimitra/PycharmProjects/appium-learning/resources/chromedriver-mac-arm64/chromedriver'


    server_url = 'http://127.0.0.1:4723'
    driver = webdriver.Remote(options=options, command_executor=server_url)

    return driver

if __name__ == "__main__":
    driver = android_browser_session()
    print("Appium driver initialized successfully.")

    wait = WebDriverWait(driver, 10)

    driver.get('https://www.tesla.com/')
    print(f'Page title: {driver.title}')

    menu_button = wait.until(expected_conditions.element_to_be_clickable((By.XPATH, '//span[text()="Menu"]')))
    menu_button.click()
    print(f'Page title: {driver.title}')

    vehicles = wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "//span[text()='Vehicles']")))
    vehicles.click()
    print(f'Page title: {driver.title}')

    model_y_order = wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "//h3[text()='Model Y']/following-sibling::div/a[2]")))
    model_y_order.click()
    print(f'Page title: {driver.title}')

    print(f'Page title: {driver.title}')
    print(f'Available contexts: {driver.contexts}')
    print(f'Current context: {driver.current_context}')

    driver.switch_to.context('NATIVE_APP')
    print(f'Current context: {driver.current_context}')
    allow = wait.until(expected_conditions.element_to_be_clickable((AppiumBy.ID, 'com.android.chrome:id/positive_button')))
    allow.click()

    driver.switch_to.context('CHROMIUM')
    order_now = wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "//button[text()='Order Now']")))
    order_now.click()

    order_card = wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "//button[text()='Order with Card']")))
    actions = ActionChains(driver)
    actions.click(order_card).perform()
    name = wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "//input[contains(@name, 'Name')]")))
    name.send_keys("Testing")


