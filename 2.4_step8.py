from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 5 секунд, пока цена не станет 100 $
button = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element ((By.ID, "price"),'100')
    )
book = browser.find_element(By.ID,'book')
book.click()
x = browser.find_element(By.XPATH,'//span[@id="input_value"]').text
y = calc(x)
y_element = browser.find_element(By.CSS_SELECTOR,'#answer')
y_element.send_keys(y)
submit = browser.find_element(By.XPATH,'//button[@id="solve"]')
submit.click()
#message = browser.find_element(By.ID, "verify_message")
time.sleep(30)
#assert "successful" in message.text