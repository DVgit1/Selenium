from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("E:\PycharmProjects\Selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://demo.nopcommerce.com/")

#FindElement() - Returns single web element

# element=driver.find_element(By.XPATH, "//*[@id='small-searchterms']")
# element.send_keys("Apple MacBook Pro 13-inch")

#2 Locator matching with multiple webelements
# element=driver.find_element(By.XPATH, "/html/body/div[6]/div[4]")
# print(element.text) #Multiple elements printed

#3 Element not available then throw NoSuchElementException
# login_element=driver.find_element(By.LINK_TEXT, "log in")
# login_element.click()

#FindElements() - Returns multiple web elements
#1 Locator matching with single webelement
# elements=driver.find_elements(By.XPATH, "//*[@id='small-searchterms']")
# print(len(elements)) #1 Webelement
# elements[0].send_keys("Apple MacBook Pro 13-inch")

#2 Locator matching with multiple webelements
# elements=driver.find_elements(By.XPATH, "//div[@class='footer']//a")
# print(len(elements)) #23 webelements
# print(elements[0].text)

#3 Elements not available
elements=driver.find_elements(By.LINK_TEXT, "Log")
print("elements returned:", len(elements))


