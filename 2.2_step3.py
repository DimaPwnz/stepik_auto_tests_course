from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time
from selenium.webdriver.support.ui import Select



link = "https://suninjuly.github.io/selects1.html"

browser = webdriver.Chrome()
browser.get(link)
num1 =  browser.find_element(By.ID,"num1").text
num2 = browser.find_element(By.ID,'num2').text
print(num1)
print(num2)
sum = int(num1) + int(num2)
print (sum)
select = Select (browser.find_element(By.TAG_NAME,'select'))
select.select_by_value(str(sum)) # ищем элемент с текстом "Python"
submit = browser.find_element(By.XPATH,'//button')
submit.click()
time.sleep(30)