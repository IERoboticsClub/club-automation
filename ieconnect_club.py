from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver

def open_club_page(driver, club_id):
    """
    Open the club page
    """
    print("OPENING CLUB PAGE")
    redirect_link = f"https://ieconnects.ie.edu/officer_login_redirect?club_id={club_id}"
    driver.get(redirect_link)
    driver.implicitly_wait(3)
    print("OPENED CLUB PAGE")


    return driver

def open_events_page(driver, past_events=False):
    """
    Open the events page
    """
    print("OPENING EVENTS PAGE")
    past_events_link = "https://ieconnects.ie.edu/events_list?show=past"
    events_link = "https://ieconnects.ie.edu/events_list"
    driver.get(events_link if not past_events else past_events_link)
    driver.implicitly_wait(3)
    print("OPENED EVENTS PAGE")

    return driver


