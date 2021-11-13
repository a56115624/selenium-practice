from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time


browser = webdriver.Chrome()
url = 'https://www.instagram.com/'

# ------ 前往該網址 ------
browser.get(url)

# ------ 填入帳號與密碼 ------
WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.NAME, 'username')))

# ------ 網頁元素定位 ------
username_input = browser.find_elements_by_name('username')[0]
password_input = browser.find_elements_by_name('password')[0]
print("inputing username and password...")

# ------ 輸入帳號密碼 ------
username_input.send_keys("a56115624")
password_input.send_keys("您的IG帳號")

# ------ 登入 ------
WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.XPATH,
'//*[@id="loginForm"]/div/div[3]/button/div')))
# ------ 網頁元素定位 ------
login_click = browser.find_elements_by_xpath('//*[@id="loginForm"]/div/div[3]/button/div')[0]
# ------ 點擊登入鍵 ------
login_click.click()