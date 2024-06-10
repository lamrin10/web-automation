from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC




options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)

s=Service("D:/chromedriver-win64/chromedriver-win64/chromedriver.exe")

driver=webdriver.Chrome(options=options,service=s)

#go to desired url

driver.get("https://www.amazon.com/")

#for finding searchbar
searchbar=driver.find_element(By.ID,"twotabsearchtextbox")
word=searchbar.send_keys('dress',Keys.ENTER)

expected_text='"dress"'
actual_text=driver.find_element(By.XPATH,"//span[@class='a-color-state a-text-bold']").text

#testcases

assert expected_text==actual_text, f"Error.Expected text :{expected_text} ,but actual text:{actual_text}"

driver.quit()
