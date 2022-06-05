from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("E:\PycharmProjects\Selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F")
# emailbox=driver.find_element(By.XPATH, "//input[@id='Email']")
# emailbox.clear()
# emailbox.send_keys("abc@gmail.com")
#
#
# print("result of text:", emailbox.text)
# print("result of get_attribute():", emailbox.get_attribute('value'))

button=driver.find_element(By.XPATH, "//button[normalize-space()='Log in']")
print("result of text:", button.text)
print("result of get_attribute():", button.get_attribute('value'))
print("result of get_attribute():", button.get_attribute('type'))
