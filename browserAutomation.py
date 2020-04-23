# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 19:40:02 2019

@author: cheerag.verma
"""

# ===========================Basic functions==================================================
# from selenium import webdriver
# browser = webdriver.Chrome("C:/Users/cheerag.verma/Downloads/chromedriver")
# browser.get("https://youtube.com")
# link = browser.find_element_by_id("search")
# link.send_keys('kabir singh')
# cl = browser.find_element_by_id("search-icon-legacy")
# cl.click()
# 
# song = browser.find_element_by_id("video-title")
# song.click()    
# =============================================================================



from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("C:/Users/cheerag.verma/Downloads/chromedriver")
driver.get("https://web.whatsapp.com")
wait = WebDriverWait(driver,600)  # waits for 600ms to load all elements and further shows the steps
target = '"Sharbani"'
string = "selenium testing"
x_args = '//span[contains(@title, '+target+')]' 
target = wait.until(EC.presence_of_element_located((By.XPATH,x_args)))
#XPath is used to find the location of any element on a webpage using HTML DOM structure
target.click()

inputbox = driver.find_element_by_class_name("_13mgZ")
for i in range(50):
    inputbox.send_keys(string+Keys.ENTER)
    
    
    
    
    
    
    
    
    
    
    