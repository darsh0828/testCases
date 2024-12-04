import time

from appium import webdriver
from appium.options.android import UiAutomator2Options
from selenium.webdriver.common.by import By

desired_caps = dict(


    deviceName='Android',
    platformName='Android',
    appPackage='com.samsung.android.dialer',
    appActivity='.DialtactsActivity'

)

capabilities_option = UiAutomator2Options().load_capabilities(desired_caps)

driver = webdriver.Remote('http://127.0.0.1:4723', options=capabilities_option)

driver.find_element(By.ID, 'com.samsung.android.dialer:id/three').click()
driver.find_element(By.ID,'com.samsung.android.dialer:id/six').click()
driver.find_element(By.ID,'com.samsung.android.dialer:id/one').click()
driver.find_element(By.ID,'com.samsung.android.dialer:id/two').click()
driver.find_element(By.ID,'com.samsung.android.dialer:id/two').click()
driver.find_element(By.ID,'com.samsung.android.dialer:id/eight').click()
driver.find_element(By.ID,'com.samsung.android.dialer:id/five').click()
driver.find_element(By.ID,'com.samsung.android.dialer:id/one').click()
driver.find_element(By.ID,'com.samsung.android.dialer:id/five').click()
driver.find_element(By.ID,'com.samsung.android.dialer:id/six').click()


driver.find_element(By.ID,'com.samsung.android.dialer:id/dialButton').click()


time.sleep(2)
driver.quit()
