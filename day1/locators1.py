from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


serv_obj = Service("E:\PycharmProjects\Selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()  # maximize browser window
#driver.find_element(By.NAME,"q").send_keys("Digital Storm VANQUISH 3 Custom Performance PC")
# driver.find_element(By.class, "button-1 search-box-button")

#linktext and partial linktext
driver.find_element(By.LINK_TEXT, "Register").click()
#driver.find_element(By.PARTIAL_LINK_TEXT, "Reg").click()
driver.close()