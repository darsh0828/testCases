import time

from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.mobileby import MobileBy

desired_caps = dict(

    deviceName='Android',
    platfromName='Android',
    browseName='Chrome',
    automationName='UiAutomator2'

)

capabilities_option = UiAutomator2Options().load_capabilities(desired_caps)

driver = webdriver.Remote('http://127.0.0.1:4723', options=capabilities_option)

driver.get("http://google.com")
print(driver.title)
driver.find_element(MobileBy.XPATH,"//*[@name='q']").send_keys("Hello Appium !!!")
#driver.find_element_by_name("q").send_keys("Hello Appium !!!")

time.sleep(2)
driver.quit()
