import yaml
from selenium import webdriver
from ieconnects_login import login, DEFAULT_HYPER
from ieconnect_club import open_club_page
from communications.mail_helpers import open_mails_page, compose_email, select_email_members, fill_email_content, preview_and_send_mail
import time


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
driver.implicitly_wait(3)
time.sleep(5)
driver = open_club_page(driver, HYPER["club_id"])
driver = open_mails_page(driver)
driver = compose_email(driver) 
driver = select_email_members(driver, all_members=False)
driver = fill_email_content(driver, "This is a test email")
driver = preview_and_send_mail(driver)
