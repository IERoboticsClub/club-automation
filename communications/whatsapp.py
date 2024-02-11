import sys
import time
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging as log
# set logs to write to automation.log
log.basicConfig(filename="/tmp/automation.log", level=log.INFO)


class Whatsapp:
    def __init__(self, user_directory_path=None, headless=False, driver_path=None):
        log.info("Initializing Whatsapp Instance at {}".format(time.ctime()))
        if not user_directory_path:
            user_directory_path = os.path.join(os.getcwd(),"user_data")
            log.warning("No user directory path provided. Using default path")
        self.user_directory_path = user_directory_path
        if not driver_path:
            print("Please provide a driver path")
            log.error("Please provide a driver path")
            sys.exit(1)
        self.driver_path = driver_path
        self.headless = headless
        self.driver = self.spawn_whatsapp_instance()




    def spawn_whatsapp_instance(self):
        # we use a chrome driver with store session
        print("OPENING WHATSAPP")
        options = webdriver.ChromeOptions()
        # MODULARIZE THIS
        options.add_argument(r"user-data-dir={}".format(self.user_directory_path))
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)
        headless = self.headless
        log.info("Spawning Whatsapp Instance")
        # make
        if headless:
            print("HEADLESS MODE")
            log.info("Using HEADLESS mode for whatsapp instance")
            options.add_argument('--headless')
            options.add_argument('--no-sandbox')
            options.add_argument('--disable-dev-shm-usage')
        # MODULARIZE THIS
        drier_path = self.driver_path
        os.environ["webdriver.chrome.driver"] = drier_path
        driver = webdriver.Chrome(options=options)
        driver.get("https://web.whatsapp.com/")
        # wait for Loading your chats not not be in the page
        print("OPENED WHATSAPP")
        WebDriverWait(driver, 60).until(
            # the search bar is visiblesWebDriverWait(driver, 60).until(
            EC.visibility_of_element_located((By.XPATH, "//div[@contenteditable='true']"))


        )

        print("LOGGED IN")
        log.info("Logged into whatsapp")
        return driver


    def broadcast_message(self, contacts : list, message : str, driver=None):
        """
        Send a message to a list of contacts
        :param contacts:
        :param message:
        :param driver:
        :return:
        """
        if not driver:
            driver = self.driver
        # search for contact in search box
        for contact in contacts:
            # print name
            print(f"SENDING MESSAGE TO {contact}")
            log.info(f"Sending message to {contact}")
            # search for contact in search box
            try:
                search_box = driver.find_elements(By.XPATH,"//div[@contenteditable='true']")[0]
                # wait for the search box to load
                driver.implicitly_wait(3)
                search_box.send_keys(contact)
                # wait for the contact to load
                driver.implicitly_wait(5)
                # select the contact
                contact = driver.find_element(By.XPATH,f"//span[@title='{contact}']")
                contact.click()
                # wait for the chat to load
                driver.implicitly_wait(3)
                # send the message
                message_box = driver.find_elements(By.XPATH,"//div[@contenteditable='true']")[1]
                message_box.send_keys(message)
                message_box.send_keys(Keys.ENTER)

            except Exception as e:
                print(e)
                print("Something went wrong. Try again.")
                log.error("Failed to broadcast message")
                continue

        time.sleep(5)
        return driver


"""
Want a better way to manage directory data, when the program starts we download the directory of the profile
unpack the directory into the user_directory_path
We also at the end of the script pack the directory into a zip file and upload it to the cloud
best provided thats free for this would be google drive
"""


def automatic_driver_download():
    """
    Download the CHrome driver automatically
    :return:
    """


if __name__ == '__main__':
    users = ['Daniel RÖSEL']
    message = "Hello, this is a test message."
    whatsapp = Whatsapp(
        user_directory_path="/home/velocitatem/.config/google-chrome/Profile 1",
        headless=False,
        driver_path="/home/velocitatem/Downloads/software/chromedriver_linux64.zip"
    )
    whatsapp.broadcast_message(users,message)
