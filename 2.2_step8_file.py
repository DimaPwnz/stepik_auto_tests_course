from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os


browser = webdriver.Chrome()
link = "http://suninjuly.github.io/file_input.html"
browser.get(link)
first_name = browser.find_element(By.XPATH, '//div/input[@name="firstname"]')
first_name.send_keys('Eleonora')
last_name = browser.find_element(By.XPATH, '//div/input[@name="lastname"]')
last_name.send_keys('Petrova')
email = browser.find_element(By.XPATH, '//div/input[@name="email"]')
email.send_keys('eleonoea@mail.ru')
element = browser.find_element(By.XPATH, '//input[@id="file"]')
current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла
element.send_keys(file_path)
button = browser.find_element(By.TAG_NAME, "button")
button.click()
time.sleep(30)