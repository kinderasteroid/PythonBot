import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

path = "C:\msedgedriver.exe"
driver = webdriver.Edge(path)
args: ['--disable-web-security', '--user-data-dir', '--allow-running-insecure-content' ]
driver.get("https://google.com")
s = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div/div/div[2]/a")
s.click()
email = driver.find_element_by_css_selector("#identifierId")
args: ['--disable-web-security', '--user-data-dir', '--allow-running-insecure-content' ]
email.send_keys("ssuuhhaass777@gmail.com")
email.send_keys(Keys.ENTER)
time.sleep(3)
passu = driver.find_element_by_css_selector("#password > div.aCsJod.oJeWuf > div > div.Xb9hP > input")
passu.send_keys("ssuuhhaass")
passu.send_keys(Keys.ENTER)
time.sleep(3)
args: ['--disable-web-security', '--user-data-dir', '--allow-running-insecure-content' ]
driver.get("https://meet.google.com/?hs=197&pli=1&authuser=0")
meet = driver.find_element_by_css_selector("#i3")
meet.send_keys("tsmrufsfgp")
meet.send_keys(Keys.ENTER)
time.sleep(5)
driver.find_element_by_xpath("/html/body/div/div[3]/div/div[2]/div[3]/div/span/span").click()
time.sleep(2)
driver.find_element_by_xpath("/html/body/div/c-wiz/div/div/div[9]/div[3]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div/div/div[1]/span").click()





