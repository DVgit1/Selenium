import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("E:\PycharmProjects\Selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()
driver.find_element(By.XPATH, "//*[@id='footer']/div[1]/a").click()

time.sleep(3)
#driver.close() #close() single browser window
driver.quit()  #close() multiple browser windows