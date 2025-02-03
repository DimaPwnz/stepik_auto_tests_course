from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/redirect_accept.html"
browser.get(link)
button = browser.find_element(By.XPATH,'//button')
button.click()
new_window = browser.window_handles[1]
browser.switch_to.window(new_window)
x = browser.find_element(By.XPATH,'//span[@id="input_value"]').text
y = calc(x)
y_element = browser.find_element(By.CSS_SELECTOR,'#answer')
y_element.send_keys(y)
submit = browser.find_element(By.XPATH,'//button')
submit.click()
time.sleep(30)