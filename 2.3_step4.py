from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/alert_accept.html"
browser.get(link)
button = browser.find_element(By.XPATH,'//div/button')
button.click()
alert = browser.switch_to.alert
alert.accept()
x = browser.find_element(By.XPATH,'//span[@id="input_value"]').text
y = calc(x)
y_element = browser.find_element(By.CSS_SELECTOR,'#answer')
y_element.send_keys(y)
submit = browser.find_element(By.XPATH,'//button')
submit.click()
time.sleep(30)