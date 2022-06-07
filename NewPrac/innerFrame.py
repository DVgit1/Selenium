# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
#
# serv_obj = Service("E:\PycharmProjects\Selenium\drivers\chromedriver.exe")
# driver = webdriver.Chrome(service=serv_obj)
# driver.get("http://demo.automationtesting.in/Frames.html")
# driver.maximize_window()
#
# driver.find_element(By.XPATH, "//a[normalize-space()='Iframe with in an Iframe']").click()
#
# outerframe=driver.find_element(By.XPATH, "//iframe[@src='MultipleFrames.html']")
# driver.switch_to.frame(outerframe)
#
# innerframe=driver.find_element(By.XPATH, "/html/body/section/div/div/iframe")
# driver.switch_to.frame(innerframe)
#
# driver.find_element(By.XPATH, "//input[@type='text']").send_keys("welcome")
#
# #driver.switch_to.parent_frame() #directly switch to parent frame(outerframe)
#

# largest = -1
# print("Before", largest)
# for the_num in [9, 41, 12, 3, 74, 15]:
#     if the_num > largest:
#         largest = the_num
#     print(largest, the_num)
# print("After", largest)

