import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("E:\PycharmProjects\Selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://itera-qa.azurewebsites.net/home/automation")
driver.maximize_window()

# 1) select specific checkbox
checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox' and contains (@id,'day')]")
print(len(checkboxes))  # 7

# Approach1
# for i in range(len(checkboxes)):
#     checkboxes[i].click()

# Approach 2
for checkbox in checkboxes:
    checkbox.click()
#time.sleep(5)

# 3) select multiple checkboxes by choice
# for checkbox in checkboxes:
#     weekname=checkbox.get_attribute("id")
#     if weekname=='monday' or weekname=='sunday':
#         checkbox.click()

# 4) select last 2 checkboxes (total numbers of elements -2= starting index)
# for i in range(len(checkboxes)-2, len(checkboxes)): #range(5,7) --> 6,7
#     checkboxes[i].click()

# 5) select first 2 checkboxes
# for i in range(len(checkboxes)):
#     if i < 2:
#         checkboxes[i].click()

# 6) clearing all the checkboxes
for checkbox in checkboxes:
    if checkbox.is_selected():
        checkbox.click()
