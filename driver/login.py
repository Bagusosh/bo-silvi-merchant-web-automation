import os
import platform
import warnings
from dotenv import load_dotenv

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


class LoginDriver:

    def __init__(self):
        load_dotenv()
        warnings.filterwarnings("ignore", category=DeprecationWarning)
        if platform.system() == "Darwin":
            self.driver = webdriver.Safari()
        else:
            self.driver = webdriver.Chrome(executable_path=os.environ.get("CHROME_DRIVER"))

        self.login_url = "https://silvi-staging.netlify.app"
        self.valid_email = 'samsantechrestoran@mailnesia.com'
        self.valid_password = '123456'
        self.valid_merchant_name = 'Samsan Tech Restoran!!'

        # xPaths
        self.login_button_xpath = '//*[@id="root"]/div[2]/div/div[2]/form/button'

        # Etc.
        self.context = {}

        # Login Driver
        self.driver.maximize_window()

        self.driver.get(self.login_url)

        try:
            _ = WebDriverWait(self.driver, 3).until(
                EC.presence_of_element_located((By.ID, "email"))
            )
        except TimeoutException:
            return

        self.driver.find_element(By.ID, "email").send_keys(self.valid_email)
        self.driver.find_element(By.ID, "pin").send_keys(self.valid_password)

        self.driver.find_element(By.XPATH, self.login_button_xpath).click()

        try:
            _ = WebDriverWait(self.driver, 10).until(
                EC.text_to_be_present_in_element((By.TAG_NAME, "h4"), self.valid_merchant_name)
            )
        except TimeoutException:
            return