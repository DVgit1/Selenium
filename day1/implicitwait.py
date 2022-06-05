from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("E:\PycharmProjects\Selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
#driver.implicitly_wait(10) #seconds      #implicit wait

driver.get("https://www.google.com/")
driver.maximize_window()
driver.find_element(By.XPATH, "//*[@id='L2AGLb']/div").click()
driver.find_element(By.NAME, "q").send_keys("Selenium")
driver.find_element(By.NAME, "q").submit()
driver.find_element(By.XPATH, "//h3[text()='Selenium']").click()