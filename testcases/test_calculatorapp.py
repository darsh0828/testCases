import time

from appium import webdriver
from appium.options.android import UiAutomator2Options
from selenium.webdriver.common.by import By

desired_cap = {}
desired_cap['platformName'] = 'Android'
desired_cap['deviceName'] = 'Android'
desired_cap['appPackage'] = 'com.sec.android.app.popupcalculator'
desired_cap['appActivity'] = '.Calculator'

capabilities_option = UiAutomator2Options().load_capabilities(desired_cap)
driver = webdriver.Remote('http://127.0.0.1:4723', options=capabilities_option)
driver.implicitly_wait(5)

driver.find_element(By.ID, 'com.sec.android.app.popupcalculator:id/calc_keypad_btn_02').click()
driver.find_element(By.ID, 'com.sec.android.app.popupcalculator:id/calc_keypad_btn_add').click()
driver.find_element(By.ID, 'com.sec.android.app.popupcalculator:id/calc_keypad_btn_04').click()
driver.find_element(By.ID, 'com.sec.android.app.popupcalculator:id/calc_keypad_btn_equal').click()
result = driver.find_element(By.ID, 'com.sec.android.app.popupcalculator:id/calc_edt_formula').text
print(result)
assert int(result) == 6
time.sleep(2)
driver.quit()
