from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("prefs", {"profile.default_content_settings.cookies": True})
driver = webdriver.Chrome(options=chrome_options)
driver.set_page_load_timeout("10")
driver.get("https://opensource-demo.orangehrmlive.com")
driver.find_element(By.NAME, "txtUsername").send_keys("Admin")
driver.find_element(By.ID, "txtPassword").send_keys("admin123")
driver.find_element(By.ID, "btnLogin").click()

act_title = driver.title
exp_title = "OrangeHRM"

if act_title == exp_title:
    print("Login Test Passed")
else:
    print("Login Test Failed")
driver.close()
