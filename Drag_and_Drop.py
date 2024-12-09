from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time


baseUrl="https://admin:admin@the-internet.herokuapp.com/drag_and_drop"
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(baseUrl)
time.sleep(5)

fromElement =driver.find_element(By.ID,"column-a")
toElement =driver.find_element(By.ID,"column-b")
time.sleep(3)

try:
    actions = ActionChains(driver)
    actions.drag_and_drop(fromElement,toElement).perform()
    time.sleep(3)
    actions.drag_and_drop(fromElement,toElement).perform()

    print("Drag and Drop elements successful")
except:
    print("Drag and Drop failed on element")

