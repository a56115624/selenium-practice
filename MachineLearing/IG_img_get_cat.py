from selenium import webdriver
import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import os
import wget
PATH = "C:/Users/admin/Desktop/新增資料夾/chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://www.instagram.com/")


username = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "username"))
    )
password = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "password"))
    )
username.clear()
password.clear()

login = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button')
username.send_keys("a56115624")
password.send_keys("az30113011")
login.click()

search = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input'))
)
keyword = "#cat"
search.send_keys(keyword)
time.sleep(1)
search.send_keys(Keys.RETURN)
time.sleep(1)
search.send_keys(Keys.RETURN)

WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "FFVAD"))
    )

imgs = driver.find_elements_by_class_name("FFVAD")

path =os.path.join(keyword)
os.mkdir(path)

count =0
for img in imgs:
    save_as = os.path.join(path,keyword+str(count)+'.jpg')
    #print(img.get_attribute("src"))
    wget.download(img.get_attribute("src"),save_as)
    count = count+1