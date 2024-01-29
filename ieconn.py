import yaml
from selenium import webdriver
from ieconnects_login import login
from ieconnect_club import open_club_page, open_events_page


with open("credentials.yaml") as f:
    credentials = yaml.load(f, Loader=yaml.FullLoader)
username = credentials["username"]
password = credentials["password"]

HYPER = {
    'origin': "https://ieconnects.ie.edu/login_only",
    'first_uname_id': "i0116",
    'second_password_id': "passwordInput",
    'stay_signed_in_id': 'idSIButton9',
    'club_id': "300003041",
    'headless': False
}

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




