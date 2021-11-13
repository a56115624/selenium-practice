#Action chains
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

PATH = "C:/Users/admin/Desktop/新增資料夾/chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://tsj.tw/")

blow = driver.find_element_by_id("click")
blow_count = driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[4]/div[2]/h4[2]')
items = []
items.append(driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[4]/div[4]/table/tbody/tr[4]/td[5]/button[1]'))
items.append(driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[4]/div[4]/table/tbody/tr[3]/td[5]/button[1]'))
items.append(driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[4]/div[4]/table/tbody/tr[2]/td[5]/button[1]'))

prices = []
prices.append('//*[@id="app"]/div[2]/div[4]/div[4]/table/tbody/tr[4]/td[4]')
prices.append('//*[@id="app"]/div[2]/div[4]/div[4]/table/tbody/tr[3]/td[4]')
prices.append('//*[@id="app"]/div[2]/div[4]/div[4]/table/tbody/tr[2]/td[4]')


actions = ActionChains(driver)
while True:
    blow.click()




