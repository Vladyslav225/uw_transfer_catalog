from bs4 import BeautifulSoup
import requests

from selenium import webdriver

driver = webdriver.Chrome(executable_path = '/home/vladyslav/uw_transfer_catalog/uw_transfer_catalog/chromedriver')

driver.get('https://wyossb.uwyo.edu/bnrprod/bwckytfc.p_display_transfer_catalog')
print(123)