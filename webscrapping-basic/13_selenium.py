from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# browser = webdriver.Chrome("C:\\Users\\user\\python-work\\python-work\\chromedriver.exe")
browser = webdriver.Chrome()
browser.get("http://naver.com")
elem = browser.find_element_by_class_name("link_login")
elem.click()
browser.back()
browser.forward()
elem = browser.find_element_by_id("query")  
elem.send_keys("나도코딩")
elem.send_keys(Keys.ENTER)