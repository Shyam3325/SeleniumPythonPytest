from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#Step:1
#Open the website.
baseUrl ="https://www.hollandandbarrett.com/en-au/"
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(baseUrl)
driver.save_screenshot(".//baseUrl screenshot.png")
time.sleep(3)
#Step:2
#Click on Rewards section.
element = driver.find_element(By.XPATH,"//h3[normalize-space()='Rewards for Life']")
driver.execute_script("arguments[0].scrollIntoView(true);",element)
time.sleep(3)

Element=(driver.find_element(By.XPATH,"//h3[normalize-space()='Rewards for Life']").click())
time.sleep(2)
driver.save_screenshot(".//Element screenshot.png")
#Step:3
#Click on Join Rewards for life and register for and account
element =driver.find_element(By.XPATH,"/html[1]/body[1]/div[2]/div[5]/div[1]/div[1]/div[1]/button[1]")
element.click()
time.sleep(2)

driver.save_screenshot(".//element screenshot.png")

#Register for an account, please update the details.
Text_box=(driver.find_element(By.ID,"firstName" ).send_keys("Shyam"))

Text_box=(driver.find_element(By.ID,"lastName" ).send_keys("kumar"))


Text_box=(driver.find_element(By.ID,"email" ).send_keys("shyam143pr@gmail.com"))

Text_box=(driver.find_element(By.ID,"confirmEmail" ).send_keys("shyam143pr@gmail.com"))


Text_box=(driver.find_element(By.NAME,"password" ).send_keys("Sam@pr9493!"))


Accept_box = driver.find_element(By.XPATH,"//input[@name='consentEmail']")
Accept_box.click()

Accept_box = driver.find_element(By.XPATH,"//input[@name='terms']")
Accept_box.click()

Click_box =driver.find_element(By.XPATH,"//button[@type='submit']")
Click_box.click()

driver.save_screenshot(".//Click_Button screenshot.png")

# Verify whether the account has been created
driver.get("https://auth.hollandandbarrett.com/u/login")
time.sleep(2)

edit_box=(driver.find_element(By.ID,"username").send_keys("shyam143pr@gmail.com"))
time.sleep(2)
edit_box=(driver.find_element(By.NAME,"password").send_keys("Sam@pr9493"))
time.sleep(2)

Click_box=driver.find_element(By.XPATH,"//button[normalize-space()='Sign In']").click()
time.sleep(3)

driver.save_screenshot(".//Click_box screenshot.png")

print("login Successful")

driver.quit()







