from selenium import webdriver;
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json

url="https://www.foliflora.fr/catalogue/tous-les-produits"

driver = webdriver.Chrome()

driver.get(url)

wait = WebDriverWait(driver, 10)

nombre = 5
tabImg=[]
for tr in range(nombre):
    image_elements = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class='front-image']/img")))
    title_elements = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//p[@class='name']")))
    price_elements = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//span[@class='amount']")))
    tabImg = [image.get_attribute('src') for image in image_elements]
    tabName = [title.text for title in title_elements]
    tabPrice = [float(price.text.replace(',','.').replace('€','').strip()) for price in price_elements]
    
listProducts = []   
for i in range(len(tabPrice)-1):
    product = {}
    product['name'] = tabName[i]
    product['price'] = tabPrice[i]
    product['url'] = tabImg[i]
    
    listProducts.append(product)
    
print(listProducts)

# import pandas as pd

# df = pd.DataFrame(listProducts, columns=["name", "price", "url"])

# print(df)

with open('jsonFile.json', 'w', encoding='utf-8') as file:
    json.dump(listProducts, file, ensure_ascii=False)

print("Data successfully written to jsonFile.json.")


