from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("E:\PycharmProjects\Selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://www.facebook.com/")
driver.maximize_window()

#tag & id
#driver.find_element(By.CSS_SELECTOR, "input#email").send_keys("abc")
#driver.find_element(By.CSS_SELECTOR, "#email").send_keys("abc")

#tag & class
driver.find_element(By.CSS_SELECTOR, "input.inputtext").send_keys("abc@gmail.com")