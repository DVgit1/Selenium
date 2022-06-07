from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("E:\PycharmProjects\Selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()

# windowid=driver.current_window_handle
# print(windowid)
driver.find_element(By.XPATH, "//*[@id='footer']/div[1]/a").click()
windowsIDs=driver.window_handles

# Approach1

# parentwindowID=windowsIDs[0] #CDwindow-79F31C06A4821F5569F8943BC46A82AE
# childwindowID=windowsIDs[1] #CDwindow-80DA7FBE43469DE49A6AFE6AD708E151
# #print(parentwindowID, childwindowID)
#
# driver.switch_to.window(childwindowID)
# print("Title of child window", driver.title)
# driver.switch_to.window(parentwindowID)
# print("Title of parent window", driver.title)
# driver.close()

# Approach2
# for winId in windowsIDs:
#     driver.switch_to.window(winId)
#     print(driver.title)

#3) close specific browser windows
for winId in windowsIDs:
    driver.switch_to.window(winId)
    if driver.title=="OrangeHRM":
        driver.close()