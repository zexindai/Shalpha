from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import os
import pandas as pd

import basic_functions as bf

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

    bf.download_wait(path, 60)

    browser.quit()
    
    df = pd.DataFrame(pd.read_html('SwClass.xls')[0])
    return df
