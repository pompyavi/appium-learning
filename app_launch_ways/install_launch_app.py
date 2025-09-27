from appium import webdriver
from appium.options.android import UiAutomator2Options
from pathlib import Path

app_location = Path(__file__).resolve().parents[1] / 'resources' / 'ApiDemos-debug.apk'
print(app_location)
options = UiAutomator2Options()

options.set_capability('udid','RZ8W807X4RL')

# have to convert to string because appium expects a string. We can't pass a Path object.
options.set_capability('app', str(app_location))
'''
The way it works is it basically installs the application and then it reads the manifest XML to retrieve
the app package and the app activity, and then it uses that information to launch your application.

But in some cases, what might happen is that APM fails to retrieve the app package and app activity
from the manifest XML.

So in such cases, apart from providing the app desired capability, you might also be able to provide
the app package and the app activity.
'''

server_url = 'http://127.0.0.1:4723'

appium_driver = webdriver.Remote(server_url, options=options)