from selenium.webdriver import Chrome
import time
driver = Chrome("./chromedriver.exe")
#打開網址
driver.get("https://accounts.google.com/signin/v2/identifier?service=youtube&uilel=3&passive=true&continue=https%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26app%3Ddesktop%26hl%3Dzh-TW%26next%3Dhttps%253A%252F%252Fwww.youtube.com%252Fwatch%253Fv%253DUkO-Jxkqr0k&hl=zh-TW&ec=65620&flowName=GlifWebSignIn&flowEntry=ServiceLogin")
# find ->find_elements
# find_all-> find_elements
driver.find_element_by_id("identifierId").send_keys("qazshane1268@gmail.com")
driver.find_element_by_id("identifierNext").click()
time.sleep(0.1)
driver.find_element_by_class_name("whsOnd").send_keys("shane1268")
driver.find_element_by_id("passwordNext").click()
time.sleep(5)