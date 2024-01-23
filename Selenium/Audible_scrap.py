from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
import time
import pandas as pd
from selenium.webdriver.common.keys import Keys

executable_path = "D:\Learnings\WebScrapping\Scrappers\Selenium\chromedriver_win64\chromedriver.exe"

website="https://www.audible.com/search"
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
service = ChromeService(executable_path=executable_path)
driver = webdriver.Chrome(service=service, options=options)
driver.get(website)
time.sleep(2)

#Extracting from pagination
pagination = driver.find_element(By.CSS_SELECTOR, ".pagingElements")
pagenumbers = pagination.find_elements(By.XPATH, "//*[contains(@class,'pageNumberElement')]")

last_pageNumber = int(pagenumbers[-1].get_attribute('text'))

product_images = []
product_title = []
product_price = []

for k in range(1,3):
    time.sleep(3)
    if(k==2):
        locationBypass = driver.find_element(By.XPATH, "//*[contains(@id,'notification-banner-message')]/span/a")
        driver.execute_script("arguments[0].click();", locationBypass)
    
    product_list = driver.find_element(By.CLASS_NAME, 'adbl-impression-container')
    product_items = product_list.find_elements(By.CLASS_NAME, 'productListItem')

    for i, product in enumerate(product_items, start=0):
        product_images.append(product.find_elements(By.XPATH, '//picture/source')[i+1].get_attribute("srcset")) #excluding logo image by i+1
        product_title.append(product.find_elements(By.XPATH, '//ul/li/h3/a')[i].text)
        product_price.append(product.find_element(By.XPATH, '//p[@id= "buybox-regular-price-{}"]/span[2]'.format(i)).text)
    
    #click next button on pagination
    nextButton = driver.find_element(By.XPATH, "//*[contains(@class,'nextButton')]/a")
    driver.execute_script("arguments[0].click();", nextButton)
    
df = pd.DataFrame({'Product_image':product_images, 'Product_title':product_title, 'Product_price':product_price})
df.to_csv("audible.csv", index=False)
print("Completed")
