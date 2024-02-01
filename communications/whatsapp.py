import sys
import time
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class Whatsapp:
    def __init__(self, user_directory_path=None, headless=False, driver_path=None):
        if not user_directory_path:
            user_directory_path = os.path.join(os.getcwd(),"user_data")
        self.user_directory_path = user_directory_path
        if not driver_path:
            print("Please provide a driver path")
            sys.exit(1)
        self.driver_path = driver_path
        self.headless = headless
        self.driver = self.spawn_whatsapp_instance()


    def spawn_whatsapp_instance(self):
        # we use a chrome driver with store session
        driver = webdriver.Chrome()
        print("OPENING WHATSAPP")
        options = webdriver.ChromeOptions()
        # MODULARIZE THIS
        options.add_argument(r"user-data-dir={}".format(self.user_directory_path))
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)
        headless = False
        # make
        if headless:
            options.add_argument('--headless')
        # MODULARIZE THIS
        drier_path = self.driver_path
        os.environ["webdriver.chrome.driver"] = drier_path
        driver = webdriver.Chrome(options=options)
        print("OPENED WHATSAPP")
        driver.get("https://web.whatsapp.com/")
        driver.implicitly_wait(60) # it really takes a while
        print("LOGGED IN")
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
                continue

        time.sleep(2)
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
