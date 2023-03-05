from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
bedrooms = '4-bedrooms'
url = 'https://www.apartments.com/houses/san-luis-obispo-ca/' + bedrooms
driver.get(url)
WebDriverWait(driver,30).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/main/section/div[1]/section[2]/div[2]')))
source = driver.page_source
soup = BeautifulSoup(source, 'html.parser')
# hello
parent = soup.find('div', 'placardContainer').find('ul')
listings = parent.find_all('li', "mortar-wrapper")
print(len(listings))
for i in listings:
    link = i.find("article")
    print(link.get('data-url'))

