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

# locating most recent *.xlsx download file
list_of_files = glob.glob('C:/Users/Sima/Downloads/*.csv')
latest_file = max(list_of_files,key = os.path.getmtime)


# replace the "\" with "/" so file path can be located by python
latest_file = latest_file.replace("\\",'/')

# we need to locate the old .csv file(s) in the dir we want to store the new csv file in
list_of_files = glob.glob('C:/Users/Sima/OneDrive - The University of Western Ontario/Personal/Medium/Medium-python-codes/data/interactive dash/*.csv')

# need to delete old csv file(s) so if we download new csv file with the same name we do not get an error while moving it
for file in list_of_files:
    os.remove(file)
    
# Move the new file from the download directory to the Medium dir
shutil.move(latest_file,'C:/Users/Sima/OneDrive - The University of Western Ontario/Personal/Medium/Medium-python-codes/data/interactive dash/')

import pandas as pd
import re

pd.set_option('display.max_rows',500)
pd.options.display.max_colwidth = 150

# again we need to locate the csv file
list_of_files = glob.glob('C:/Users/Sima/OneDrive - The University of Western Ontario/Personal/Medium/Medium-python-codes/data/interactive dash/*.csv')
latest_file = max(list_of_files,key = os.path.getctime)

df = pd.read_csv('{}'.format(latest_file),header=0)        

# Do some cleaning                  