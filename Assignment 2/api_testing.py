from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

browser = webdriver.Firefox()
browser.set_window_size(900,900)
browser.set_window_position(0,0)
sleep(1)

browser.get("https://www.w3schools.com/")
browser.find_element_by_id("search2").send_keys("HTML Tutorial")
sleep(2)

browser.find_element_by_id("search2").send_keys(Keys.RETURN)
sleep(7)

browser.execute_script("window.scrollTo(0,700);")
sleep(3)

browser.execute_script("window.scrollTo(0,-700);")
sleep(1)

print("testing is done")

