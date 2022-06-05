from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

serv_obj = Service("E:\PycharmProjects\Selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://www.opencart.com/index.php?route=account/register")
driver.maximize_window()

drpcountry_ele=driver.find_element(By.XPATH, "//select[@id='input-country']")
drpcountry=Select(drpcountry_ele)

#select option from the dropdown
#drpcountry.select_by_visible_text("Ukraine")
#drpcountry.select_by_value("170") #Poland
#drpcountry.select_by_index(215) #index

# capture all the options and print them
alloptions=drpcountry.options
print("Total number of options", len(alloptions))

for opt in alloptions:
    opt.text
    print(opt.text)

# select option from dropdown without using built-in method
# for opt in alloptions:
#     if opt.text=="Ukraine":
#         opt.click()
#         break

driver.find_elements(By.XPATH, "//select[@id='input-country']/Option")
print(len(alloptions))