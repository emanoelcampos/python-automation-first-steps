from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pandas as pd
import re
import os
from datetime import datetime
import sys

application_path = os.path.dirname(sys.executable)

now = datetime.now()
month_day_year = now.strftime("%m%d%Y")

website = "https://news.ycombinator.com/"
path = "D:/selenium-drivers/chromedriver-win64/chromedriver.exe"

options = webdriver.ChromeOptions()
options.add_argument("--headless=new")

service = Service(executable_path=path)
driver = webdriver.Chrome(service=service, options=options)
driver.get(website)

containers = driver.find_elements(by="xpath", value="//td[@class='title']/span/a")

titles = []
links = []

search_word = 'rpa'

for container in containers:
    title = container.text
    link = container.get_attribute('href')
    if re.search(r"\b{}\b".format(search_word.lower()), title.lower()):
        titles.append(title)
        links.append(link)

my_dict = {
    'titles': titles,
    'links': links
}

df_headlines = pd.DataFrame(my_dict)
file_name = f'headline{month_day_year}.csv'
final_path = os.path.join(application_path, file_name)

df_headlines.to_csv(final_path)

driver.quit()
