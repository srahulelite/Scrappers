from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
import time
import pandas as pd

executable_path = "D:\Learnings\WebScrapping\Scrappers\Selenium\chromedriver_win64\chromedriver.exe"
website="https://www.audible.com/search"
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
service = ChromeService(executable_path=executable_path)
driver = webdriver.Chrome(service=service, options=options)
driver.get(website)
time.sleep(2)
product_list = driver.find_element(By.CLASS_NAME, 'adbl-impression-container')
product_items = product_list.find_elements(By.CLASS_NAME, 'productListItem')

product_images = []
product_title = []
product_price = []
for i, product in enumerate(product_items, start=0):
    product_images.append(product.find_elements(By.XPATH, '//picture/source')[i].get_attribute("srcset"))
    product_title.append(product.find_elements(By.XPATH, '//ul/li/h3/a')[i].text)
    product_price.append(product.find_element(By.XPATH, '//p[@id= "buybox-regular-price-{}"]/span[2]'.format(i)).text)

df = pd.DataFrame({'Product_image':product_images, 'Product_title':product_title, 'Product_price':product_price})
df.to_excel("audible.xlsx", index=False)
