cd = "C:\\Users\\Manas\\Desktop\\chromedriver.exe" #provide chromedriver path
em = "************@domain.com" #provide user id
pwd = "abcd1234" #provide user password

import time
from selenium import webdriver
driver = webdriver.Chrome(cd) #creating webdriver
driver.get("https://www.facebook.com/login/") #to go to the sign in page of linked in 
time.sleep(5) #it will hold for 5 seconds
eml=driver.find_element_by_xpath("//input[@type = 'text']")
eml.send_keys(em)
pswrd = driver.find_element_by_xpath("//input[@type = 'password']")
pswrd.send_keys(pwd)
btn=driver.find_element_by_xpath("//button[@value = '1']")
btn.click()

time.sleep(20)
driver.close()