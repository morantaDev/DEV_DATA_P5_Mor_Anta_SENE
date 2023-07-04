import pandas as pd

# Series est un tableau unidimensionnel étiqueté capable de contenir n'importe quel type de données (entiers, chaînes, nombres à virgule flottante, objets Python, etc.). Les étiquettes d'axe sont collectivement appelées index . La méthode de base pour créer un Series est d'appeler

# s = pd.Series("Salut les amis")
# print(s.n)

from selenium import webdriver
from selenium.webdriver.common.by import By
url = "https://www.espn.com/nba/seasonleaders"
driver = webdriver.Chrome()
driver.get(url)

# button = driver.find_element(By.XPATH, "//*[@id='my-players-table']/div[1]/div[2]/div[1]/div[2]/a/div")
button = driver.find_element(By.CLASS_NAME, "jcarousel-next")
button.click()
    
driver.quit()


