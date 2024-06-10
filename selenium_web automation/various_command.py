from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys




options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)

s=Service("D:/chromedriver-win64/chromedriver-win64/chromedriver.exe")

driver=webdriver.Chrome(options=options,service=s)
driver.get("https://demo.nopcommerce.com/")
driver.find_element(By.CLASS_NAME,"ico-register").click()
#conditional commands

search_bar=driver.find_element(By.XPATH,"//input[@class='search-box-text ui-autocomplete-input']")
#check it is present or not
print("displayed status:",search_bar.is_displayed())

#check enabled or not
print("enable  status:",search_bar.is_enabled())

#check radio element is selected or not
print("default radio status")

male=driver.find_element(By.XPATH,"//input[@id='gender-male']")
print('status of male checkbox',male.is_selected())

female=driver.find_element(By.XPATH,"//input[@id='gender-female']")
print('status of female checkbox',male.is_selected())



#when male is selected
male.click()
print("status of male checkbox:",male.is_selected())

female=driver.find_element(By.XPATH,"//input[@id='gender-female']")
print('status of male checkbox',female.is_selected())



 