from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from communications.pow_mail_template import load_pow_mail_template
import time

def open_mails_page(driver):
    """
    Open the events page
    """
    print("OPENING MAILS PAGE")
    mails_page_link = "https://ieconnects.ie.edu/emails"
    driver.get(mails_page_link)
    driver.implicitly_wait(3)
    print("OPENED MAILS PAGE")

    return driver


def compose_email(driver):

    print("OPENING COMPOSE MAIL PAGE")
    compose_email_xpath = "/html/body/div[5]/div[2]/div[2]/div/div[4]/div[2]/a"
    compose_email_text = "Compose Email"

    try:
        button = driver.find_element(By.XPATH, f"//*[contains(text(), '{compose_email_text}')]")
        button.click()
    except:
        print(f"Could not find the button with the text '{compose_email_text}'")
        button = None
        try:
            button = driver.find_element(By.XPATH, compose_email_xpath)
            button.click()
        except:
            print(f"Could not find the button with the xpath '{compose_email_xpath}'")
            button = None
            return driver

    driver.implicitly_wait(5)

    return driver


def select_email_members(driver,
                  members=["dsanmartin.ieu2020@student.ie.edu"],
                  all_members=False):
    if all_members:
        select_members_button = driver.find_element(By.XPATH, "//*[@id='Checkbox1']")
        select_members_button.click()
        print("SELECTED ALL MEMBERS")
    else:
        select_student_partners_button = driver.find_element(By.XPATH, "//*[@id='mb_checkbox--all-members_7_7']")
        select_student_partners_button.click()
        print("STUDENT PARTNERS SELECTED")

    button = driver.find_element(By.XPATH, f"//*[contains(text(), 'Compose email')]")
    button.click()
    driver.implicitly_wait(5)
    
    button = driver.find_element(By.XPATH, f"//*[contains(text(), 'Email Composer')]")
    button.click()

    if not all_members:
        unselect_all_button = driver.find_element(By.XPATH, "//*[@id='efb--checkbox-select-all']")
        unselect_all_button.click()
        print("UNSELECTED ALL MEMBERS")

        add_members_text_box = driver.find_element(By.XPATH, "//*[@id='search_members']")
        for member in members:
            add_members_text_box.send_keys(member)
            time.sleep(2)
            add_members_text_box.send_keys(Keys.CONTROL, Keys.ENTER)
            print("SELECTED SPECIFIC MEMBERS")

        driver.implicitly_wait(3)
    
    return driver

from selenium.webdriver.common.action_chains import ActionChains 


def fill_email_content(driver,
        subject="The PoW has been elected - Robotics & AI Club",
        content=load_pow_mail_template()
):
    
    actions = ActionChains(driver)
    
    # unselect previous elements
    driver.find_element(By.XPATH, "//*[@id='page-cont']").click()


    if 'firefox' in driver.capabilities['browserName']:
        # Since firefox does not support the move_to_element method, we need to scroll by fixed amount
        # src: https://stackoverflow.com/questions/44777053/selenium-movetargetoutofboundsexception-with-firefox
        driver.execute_script("window.scrollTo(0, 400)")
        print("SCROLLING DOWN")
        subject_text_box = driver.find_element(By.XPATH, "//*[@id='subject']")

    else:
        actions.move_to_element(subject_text_box).perform()
    subject_text_box.send_keys(subject)
    
    driver.implicitly_wait(3)
    time.sleep(5)

    if 'firefox' in driver.capabilities['browserName']:
        driver.execute_script("window.scrollTo(0, 800)")
        print("SCROLLING DOWN")
        source_button = driver.find_element(By.XPATH, "/html/body/div[5]/div[2]/div[2]/div/div[3]/form/div/div[1]/div[3]/div/table/tbody/tr/td/div/div/span[1]/span[2]/span[7]/span[3]/a/span[1]")
    else:
        source_button = driver.find_element(By.XPATH, "//*[@id='cke_41']")
        actions.move_to_element(source_button).perform()

    source_button.click()

    driver.implicitly_wait(3)
    if 'firefox' in driver.capabilities['browserName']:
        driver.execute_script("window.scrollTo(0, 1000)")
        content_text_box = driver.find_element(By.XPATH, "/html/body/div[5]/div[2]/div[2]/div/div[3]/form/div/div[1]/div[3]/div/table/tbody/tr/td/div/div/div/textarea")
    else:
        content_text_box = driver.find_element(By.XPATH, "/html/body/div[5]/div[2]/div[2]/div/div[3]/form/div/div[1]/div[3]/div/table/tbody/tr/td/div/div/div/textarea")
        actions.move_to_element(content_text_box).perform()
    content_text_box.send_keys(content)

    return driver


def preview_and_send_mail(driver):
    preview_button = driver.find_element(By.XPATH, "/html/body/div[5]/div[2]/div[2]/div/div[3]/form/div/div[2]/input[8]")
    preview_button.click()
    print("PREVIEW BUTTON CLICKED")

    send_button = driver.find_element(By.XPATH, "//*[@id='send_email_button']")
    send_button.click()
    print("EMAIL SENT SUCCESSFULLY")

    return driver