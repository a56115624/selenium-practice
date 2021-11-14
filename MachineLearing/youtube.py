from  selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
PATH = "C:/Users/admin/Desktop/新增資料夾/chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://icook.tw/")
search = driver.find_element_by_name("q")
search.send_keys("牛肉")
search.send_keys(Keys.RETURN)

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "browse-title-count"))
)

link = driver.find_element_by_link_text("牛肉湯")
link.click()

time.sleep(5)
driver.quit()



