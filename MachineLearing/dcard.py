from  selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
PATH = "C:/Users/admin/Desktop/新增資料夾/chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www.dcard.tw/f")
search = driver.find_element_by_name("query")
search.clear()
search.send_keys("比特幣")
search.send_keys(Keys.RETURN)

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "sc-3yr054-1"))
)
titles = driver.find_elements_by_class_name("tgn9uw-3")
for title in titles:
    print(title.text)
#點擊連結
link = driver.find_element_by_link_text("#分享 狼王11月12日復盤")
link.click()



time.sleep(5)
driver.quit()
