email = '*************@domain.com' #provide user id
password = 'abcd1234' #provide user password
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys

cd = "C:\\Users\\Manas\\Desktop\\chromedriver.exe" #chorome driver path 
from selenium import webdriver
import time

driver = webdriver.Chrome(cd) #creating webdriver
driver.get("https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin") #to go to the sign in page of linked in 
time.sleep(5)

eml=driver.find_element_by_xpath('//*[@id="username"]')
eml.send_keys(email)
pswrd = driver.find_element_by_xpath('//*[@id="password"]')
pswrd.send_keys(password)
btn=driver.find_element_by_xpath('//*[@id="organic-div"]/form/div[3]/button')
btn.click()