from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
link = "https://suninjuly.github.io/execute_script.html"
browser.get(link)
x = browser.find_element(By.CSS_SELECTOR, "#input_value").text
print(x)
y = calc(x)
print(y)
y_element = browser.find_element(By.CSS_SELECTOR,'#answer')
y_element.send_keys(y)
button = browser.find_element(By.TAG_NAME, "button")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
checkbox = browser.find_element(By.ID,'robotCheckbox')
checkbox.click()
radiobutton = browser.find_element(By.XPATH,'//input[@id="robotsRule"]')
radiobutton.click()
button.click()
time.sleep(30)