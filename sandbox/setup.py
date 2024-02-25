from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
driver = webdriver.Remote(
    command_executor='http://localhost:4444/wd/hub',
    options=options
)
print("OPENING WHATSAPP")
driver.get("https://web.whatsapp.com/")
print(driver.title)
import time
time.sleep(10)
print(driver.title)
driver.save_screenshot("whatsapp.png")
# open the image
import os
os.system("feh whatsapp.png")
i = input("Press enter after scanned QR code")
driver.save_screenshot("whatsapp_logged_in.png")
os.system("feh whatsapp_logged_in.png")
# save the session
driver.quit()