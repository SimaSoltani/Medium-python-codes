# -*- coding: utf-8 -*-
"""
Create and automate an interactive dashboard using Python
From : https://towardsdatascience.com/creating-and-automating-an-interactive-dashboard-using-python-5d9dfa170206
"""
# import packages
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import shutil
import glob
import os
from unicodedata import *
import time



# open a chrome browser using selenium
driver = webdriver.Chrome(ChromeDriverManager().install())

#got to the webpage where excel file links are located
driver.get("https://data.ontario.ca/dataset/confirmed-positive-cases-of-covid-19-in-ontario/")

#these options allows selenium to download files
options = Options()
options.add_experimental_option("browser.download.folderList",2)
options.add_experimental_option('browser.download.manager.showWhenStarting',False)
options.add_experimental_option('browser.helperApps.neverAsk.saveToDisk','applocation/octet-stream,application/vnd.ms-excel')

# initialize an object to the locations on the web page and click on to download
link = driver.find_element_by_xpath('/html/body/div/div/div[3]/div/article/div/section[1]/ul[1]/li[1]/div[2]/div/a[2]')
link.click()


#Wait for 15 seconds to allow chrome to download file 
time.sleep(15) 

