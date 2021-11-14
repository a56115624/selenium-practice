#搜索食譜

from  selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
#引入我們載入的chromedriver
PATH = "C:/Users/admin/Desktop/新增資料夾/chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://icook.tw/")
#指向search列
search = driver.find_element_by_name("q")
#先清空
search.clear()
#輸入牛肉
search.send_keys("牛肉")
#按下enter
search.send_keys(Keys.RETURN)
#此句的意思是,等到某句出現後才執行後續的程式碼
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "browse-title-count"))
)
#因為全部的titles都有都含同樣的class_name
titles = driver.find_elements_by_class_name("browse-recipe-name")
for title in titles:
    print(title.text)


time.sleep(5)
#執行結束後關閉
driver.close()
