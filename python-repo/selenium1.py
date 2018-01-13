from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
password="sabgmail"
driver=webdriver.Chrome()
driver.get("https://www.google.com")
assert "Google" in driver.title
elem=driver.find_element_by_name("q")
elem.clear
elem.send_keys("date")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
e1=driver.find_element_by_css_selector("#gbw > div > div > div.gb_zc.gb_yg.gb_R > div.gb_jg.gb_R > div")
e1.click()
e2=driver.find_element_by_css_selector("#identifierId")
e2.send_keys("krishnaps909")
e2.send_keys(Keys.RETURN)
#e3=driver.find_element_by_css_selector("#password > div.aCsJod.oJeWuf > div > div.Xb9hP > input")
time.sleep(1)
e3=driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
e3.send_keys(password)
e3.send_keys(Keys.RETURN)


