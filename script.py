import requests
import os
import pandas as pd
import csv
from bs4 import BeautifulSoup
import time

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from urllib.parse import urlsplit
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


import os,glob

import warnings
warnings.filterwarnings('ignore')

#Select your directory for the download result
output_directory = r'C:\Users\andriawan\Documents\My Task\Python\weidmuller'
chrome_options = Options()
chrome_options.add_experimental_option('prefs', {
    'download.default_directory': output_directory,
    'download.prompt_for_download': False,
    'download.directory_upgrade': True,
    'safebrowsing.enabled': True,
    'plugins.always_open_pdf_externally': True
})



link = ['https://catalog.weidmueller.com/catalog/Start.do;jsessionid=640C3A1C91A40C6B190F7969FDFE13CD?ObjectID=1776900000&page=Product',
       'https://catalog.weidmueller.com/catalog/Start.do;jsessionid=640C3A1C91A40C6B190F7969FDFE13CD?ObjectID=2576190000&page=Product',
       'https://catalog.weidmueller.com/catalog/Start.do;jsessionid=640C3A1C91A40C6B190F7969FDFE13CD?ObjectID=1169900000&page=Product']

#Change your directory to folder that has chromedriver.exe 
driver = webdriver.Chrome(executable_path=r'C:\Users\andriawan\Documents\My Task\Python\weidmuller\chromedriver.exe', options=chrome_options)
for i in link:
    driver.get(i)
    try:
        time.sleep(2)
        pdf_link = driver.find_element(By.LINK_TEXT, 'PDF data sheet')
        pdf_link.click()
        time.sleep(10)
        download_link = driver.find_element(By.LINK_TEXT, 'Download data sheet')
        download_link.click()
        time.sleep(10)
    except :
        pass

  #rename file
    latest_file = max([os.path.join(output_directory, f) for f in os.listdir(output_directory)], key=os.path.getctime)
    if os.path.exists(latest_file):
        # Rename the downloaded file to the desired file name
        new_file_path = os.path.join(output_directory, i[-23:]+'.pdf')
        os.rename(latest_file, new_file_path)
        print("File renamed successfully.")
    else:
        print("File download failed or not completed.")
        
driver.quit()
