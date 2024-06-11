import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def wordpress():
    chromedriver_path = 'C://Users//Z00530863//Music//chrome-win64.exe'
    service = Service(chromedriver_path)
driver = webdriver.Chrome()
driver.get("https://wordpress.org/")
driver.maximize_window()
print("*Browser launched successfully*")
print(driver.title)
time.sleep(5)

Extend = driver.find_element(By.XPATH,"//button[@aria-label='Extend submenu']").click()
Themes = driver.find_element(By.XPATH,"//span[text()='Themes']").click()
Search = driver.find_element(By.XPATH,"//input[@placeholder='Search themes...']").click()
Search = driver.find_element(By.XPATH,"//input[@placeholder='Search themes...']")
Search.send_keys("Hello Elementor")
Search.send_keys(Keys.ENTER)
time.sleep(5)
SearchImage= driver.find_element(By.XPATH,"//h3[text()='Hello Elementor']").click()
time.sleep(5)
SearchImage= driver.find_element(By.XPATH,"//h3[text()='Hello Elementor']")
driver.execute_script("window.scrollTo(0,300)")
time.sleep(5)
try:
    SearchImage= driver.find_element(By.XPATH,"//h3[text()='Hello Elementor']")
    print("*Hello Elementor Theme displayed*")
except NoSuchElementException:
    print("Theme is not found")
driver.close() 
driver.quit()
