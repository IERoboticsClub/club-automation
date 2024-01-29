from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
HYPER, username, password = None, None, None
def click_on_ie_login(driver):
    all_anchor_tags = driver.find_elements(By.TAG_NAME,"a")
    for anchor_tag in all_anchor_tags:
        if anchor_tag.text == "IE Login":
            anchor_tag.click()
            driver.implicitly_wait(3)
            return driver


def fill_first_input(driver):
    input = driver.find_element(By.ID,HYPER["first_uname_id"])
    input.send_keys(username)
    input.send_keys(Keys.CONTROL, Keys.ENTER)
    driver.implicitly_wait(3)
    return driver

def fill_second_input(driver):
    input = driver.find_element(By.ID,HYPER["second_password_id"])
    input.send_keys(password)
    input.send_keys(Keys.CONTROL, Keys.ENTER)
    driver.implicitly_wait(3)
    return driver

def stay_sign_in_check(driver):
    has_stay_signed_in = driver.find_elements(By.XPATH,"//div[text()='Stay signed in?']")
    if len(has_stay_signed_in) > 0:
        # click on the button
        button = driver.find_element(By.ID,HYPER["stay_signed_in_id"])
        button.click()
        driver.implicitly_wait(3)
    return driver



def login(
        driver : webdriver.Firefox,
        HYPER_i : dict,
        username_i : str,
        password_i : str
    ) -> webdriver.Firefox:
    global HYPER, username, password
    HYPER, username, password = HYPER_i, username_i, password_i
    print('LOGGING IN')
    driver.get(HYPER["origin"])
    print('STAGE 1 .. ', end='')
    driver = click_on_ie_login(driver)
    print('2 .. ', end='')
    driver = fill_first_input(driver)
    print('3 .. ', end='')
    driver = fill_second_input(driver)
    print('4 .. ', end='')
    driver = stay_sign_in_check(driver)
    print('5')
    driver.implicitly_wait(10)
    print('LOGGED IN')
    return driver
