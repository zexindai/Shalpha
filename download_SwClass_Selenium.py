#!/usr/bin/env python
# coding: utf-8

#Download SwClass based on Selenium

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import os
import pandas as pd
import time

def download_wait(directory, timeout, nfiles=None):
    seconds = 0
    dl_wait = True
    while dl_wait and seconds < timeout:
        time.sleep(1)
        dl_wait = False
        files = os.listdir(directory)
        if nfiles and len(files) != nfiles:
            dl_wait = True
        for fname in files:
            if fname.endswith('.crdownload'):
                dl_wait = True
        seconds += 1
    return seconds

def download_SwClass():
    path = os.getcwd()
    chromeOptions = webdriver.ChromeOptions()
    prefs = {'download.default_directory' : path}
    chromeOptions.add_experimental_option("prefs",prefs)
    chromeOptions.add_argument("--headless")
    browser = webdriver.Chrome(ChromeDriverManager().install(),options=chromeOptions)
    browser.get('http://www.swsindex.com/idx0530.aspx')
    element=browser.find_element_by_xpath('//*[@id="form1"]/div[3]/div/div[1]/div[1]/div[3]/table[2]/tbody/tr[2]/td/table/tbody/tr/td[3]/a')
    element.click()
    download_wait(path, 60)
    browser.quit()
    df = pd.DataFrame(pd.read_html('SwClass.xls')[0])
    return df
    
download_SwClass()
