import yaml
from selenium import webdriver
from ieconnects_login import login, DEFAULT_HYPER
from ieconnect_club import open_club_page, open_events_page


with open("credentials.yaml") as f:
    credentials = yaml.load(f, Loader=yaml.FullLoader)
username = credentials["username"]
password = credentials["password"]

HYPER = DEFAULT_HYPER

# driver = webdriver.Firefox()
# make it so that it can be run from the command line with the
# driver not being visible
options = webdriver.FirefoxOptions()
if HYPER["headless"]:
    options.add_argument('--headless')
driver = webdriver.Firefox(options=options)



driver = login(driver, HYPER, username, password)
driver = open_club_page(driver, HYPER["club_id"])
driver = open_events_page(driver, past_events=True)
# print the html
print(driver.page_source)




