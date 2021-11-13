from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
PATH = "C:/Users/admin/Desktop/新增資料夾/chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://popcat.click/")
div = driver.find_element_by_id('app')
while True:
    div.click()


