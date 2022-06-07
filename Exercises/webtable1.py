from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("E:\PycharmProjects\Selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

#1) count number of rows & columns

noOfrows=len(driver.find_elements(By.XPATH, "//table[@name='BookTable']//tr"))
noOfcolumns=len(driver.find_elements(By.XPATH, "//table[@name='BookTable']//tr/th"))
print(noOfrows) #7
print(noOfcolumns) #4


#2) read specific row & column data - Master in Selenium
data=driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr[5]/td[1]").text
#print(data)

#3) Read all the rows & Columns data
print("printing all the rows and columns data...")
# for r in range(2, noOfrows+1):
#     for c in range(1, noOfcolumns+1):
#         data = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr["+str(r)+"]/td["+str(c)+"]").text
#         print(data)
#     print()

#4)Read data based on condition(List name whose author is Mukesh)
for r in range(2, noOfrows+1):
    authorName=driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr["+str(r)+"]/td[2]").text
    if authorName=="Mukesh":
        bookName = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr[" + str(r) + "]/td[1]").text
        price = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr[" + str(r) + "]/td[4]").text
        print(bookName,"           ",authorName,"         ",price)

driver.close()
