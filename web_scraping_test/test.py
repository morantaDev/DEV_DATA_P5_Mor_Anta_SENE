from selenium import webdriver

from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
from selenium.webdriver.firefox.options import Options

url = "https://www.lequipe.fr/Football/ligue-1/page-classement-equipes/general"

firefox_options = Options()
firefox_options.headless = True  # Run Firefox in headless mode
# firefox_options.add_argument("--width=1920")
# firefox_options.add_argument("--height=1080")

driver= webdriver.Firefox(options=firefox_options)

driver.get(url)
#attendre 10 secondes pour que la page se charge afin de récupérer les données
wait = WebDriverWait(driver, 5)

# team_path = "/html/body/div[4]/div/div/div[2]/div/div[3]/main/div[2]/div[2]/div/table/tbody/tr[1]/td[2]/a"
# team_journey = "tr.table__row:nth-child(2) > td:nth-child(5)"

teams_classement = driver.find_elements(By.XPATH, "//tr[@class='table__row']/td[1]")
teams_name = driver.find_elements(By.XPATH, "//tr[@class='table__row']/td[2]")
teams_points = driver.find_elements(By.XPATH, "//tr[@class='table__row']/td[4]")
teams_days = driver.find_elements(By.XPATH, "//tr[@class='table__row']/td[5]")
teams_gains = driver.find_elements(By.XPATH, "//tr[@class='table__row']/td[6]")
teams_draws = driver.find_elements(By.XPATH, "//tr[@class='table__row']/td[7]")
teams_losses = driver.find_elements(By.XPATH, "//tr[@class='table__row']/td[8]")

# /html/body/div[4]/div/div/div[2]/div/div[3]/main/div[2]/div[2]/div/table/tbody/tr[1]/td[4]

infos=[]
classement_table = [classement.text for classement in teams_classement]
name_table = [name.text for name in teams_name]
points_table = [points.text for points in teams_points]
days_table = [day.text for day in teams_days]
gains_table = [gain.text for gain in teams_gains]
draws_table = [draw.text for draw in teams_draws]
losses_table = [loss.text for loss in teams_losses]

for i in range(len(teams_classement)):
    team_info = {}
    team_info['classement'] = classement_table[i]
    team_info['names'] = name_table[i]
    team_info['days'] = days_table[i]
    team_info['points'] = points_table[i]
    team_info['gains'] = gains_table[i]
    team_info['draws'] = draws_table[i]
    team_info['losses'] = losses_table[i]
    # print(team_info)
    infos.append(team_info)

# print(infos)

df = pd.DataFrame(infos, columns=['names', 'days', 'points', 'gains', 'draws', 'losses'])
print(df)
df.to_json('json_file.json')


##################################################

# while True:
#     # Scrape data from the current page
#     # ...

#     # Find and click the next button
#     next_button = driver.find_element_by_xpath('//button[@class="next-page-button"]')
#     if next_button.is_enabled():
#         next_button.click()
#     else:
#         break

###################################################
    
    
    

# teams_rows = driver.find_elements(By.CLASS_NAME, "table__row")

# teams = driver.find_elements(By.CLASS_NAME, "table__link")
# teams_points = driver.find_elements(By.CLASS_NAME, "table__col--points")

# points_table = [journey.text for journey in teams_points]

# for point in points_table:
#     # print(point)

#     pass



# teams_table = [team_name.text for team_name in teams]
# for team in teams_table:
#     # print(team)
#     pass
# teams = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".table > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(2) > a:nth-child(1)")))

# teams = driver.find_elements(By.CSS_SELECTOR, team_css_selector)
# # print(teams.text)
# for team in teams:
#     print(team.text)

# for team in teams:
    # team = tm.find_element(By.XPATH, "/html/body/div[4]/div/div/div[2]/div/div[3]/main/div[2]/div[2]/div/table/tbody/tr[1]/td[4]")
    # print(team.text)


driver.quit()










































# import requests
# from bs4 import BeautifulSoup


# url = "https://www.selenium.dev/selenium/web/web-form.html"

# get_url = requests.get(url)
# html_page = get_url.text
# page = BeautifulSoup(html_page, 'html.parser')

# coupe = page.select('#my-options')

# for coup in coupe:
#     print(coup)
    


# from selenium import webdriver
# from selenium.webdriver.common.by import By





# def test_eight_components():
#     driver = webdriver.Chrome()

#     driver.get("https://www.selenium.dev/selenium/web/web-form.html")

#     title = driver.title
#     assert title == "Web form"

#     driver.implicitly_wait(0.5)

#     text_box = driver.find_element(by=By.NAME, value="my-text")
#     submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")

#     text_box.send_keys("Selenium")
#     submit_button.click()

#     message = driver.find_element(by=By.ID, value="message")
#     value = message.text
#     assert value == "Received!"

#     driver.quit()
    
# test_eight_components()











# #définir ou instancier notre driver(objet)
# # options = webdriver.ChromeOptions()
# # print(options)
# driver = webdriver.Chrome(ChromeDriverManager().install()) #, #options=options)
# # print(driver)


# #url de navigation
# driver.get('https://www.selenium.dev/selenium/web/web-form.html')

# html = driver.page_source

# source  = BeautifulSoup(html, 'html.parser')
# print(source)

# #fermer la navigation si faite
# driver.quit()


# url = "https://www.selenium.dev/selenium/web/web-form.html"

# driver = webdriver.Chrome()

# driver.get(url)


# submit_button = driver.find_element(By.XPATH, "/html/body/main/div/form/div/div[2]/button")
# class_submits = driver.find_element(By.CLASS_NAME, "btn btn-outline-primary mt-3")

# print(class_submits)

# submit_button.click()
# selectTag = "/html/body/main/div/form/div/div[2]/label[1]/select"

# selected_elements = driver.find_elements(By.XPATH, "/html/body/main/div/form/div/div[2]/label[1]/select")

# /html/body/main/div/form/div/div[2]/label[1]/select/option[1]
# selects = driver.find_elements(By.XPATH, "./html/body/main/div/form/div/div[2]/label[1]/select")
# datalist = driver.find_elements(By.XPATH,"//*[@id='my-options']")

# for data in datalist:
    
#     values = data.find_elements(By.TAG_NAME, "value")
#     for value in values:
#         print(value.text)
# print(datalist)
# for select in selects:
#     print(select.text)


# for element in selected_elements:
#     print(element.text)
    # pass




