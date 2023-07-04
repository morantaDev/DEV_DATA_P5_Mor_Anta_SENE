from selenium import webdriver





url = "https://www.amazon.fr/t%C3%A9l%C3%A9phonie-t%C3%A9l%C3%A9phone-portable-smartphone/b/?ie=UTF8&node=13910711&ref_=sv_cag_2"

driver = webdriver.Chrome()
driver.get(url)