from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC






options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)

s=Service("D:/chromedriver-win64/chromedriver-win64/chromedriver.exe")

driver=webdriver.Chrome(options=options,service=s)

#go to desired url

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")


user_name = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//input[@name='username']"))
    )

user_name.send_keys("Admin",Keys.ENTER)


password= WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//input[@name='password']"))
    )

password.send_keys("admin123")

login=WebDriverWait(driver,10).until(
    EC.visibility_of_element_located((By.XPATH,"//button[@type='submit']"))

)
login.click()


excepted_result="OrangeHRM"
actual_result=driver.title

if excepted_result==actual_result:
    print("login sucessful")
else:
    print("login unsucessful")


driver.quit()





