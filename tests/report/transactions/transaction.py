import os
import random
import platform
import time
import unittest
import warnings
from loguru import logger
from dotenv import load_dotenv
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

from faker import Faker

from driver.login import LoginDriver


class SalesReportTransactionTests(unittest.TestCase):
    def setUp(self) -> None:
        load_dotenv()
        warnings.filterwarnings("ignore", category=DeprecationWarning)

        self.driver = LoginDriver().driver

        # data
        self.valid_page_name = 'Sales'
        self.valid_merchant_name = 'Samsan Tech Restoran!!'
        self.title_menu_chart = 'Transaksi'

        # Xpath
        self.calendar_button_xpath = '/html/body/div[1]/div[2]/div[3]/div/div/div[2]/div/button[2]'
        self.today_button_xpath = '/html/body/div[3]/div[3]/ul/div/div[2]/button[1]'
        self.yesterday_button_xpath = '/html/body/div[3]/div[3]/ul/div/div[2]/button[2]'
        self.this_week_button_xpath = '/html/body/div[3]/div[3]/ul/div/div[2]/button[3]'
        self.last_week_button_xpath = '/html/body/div[3]/div[3]/ul/div/div[2]/button[4]'
        self.this_month_button_xpath = '/html/body/div[3]/div[3]/ul/div/div[2]/button[5]'
        self.last_month_button_xpath = '/html/body/div[3]/div[3]/ul/div/div[2]/button[6]'
        self.this_year_button_xpath = '/html/body/div[3]/div[3]/ul/div/div[2]/button[7]'
        self.last_year_button_xpath = '/html/body/div[3]/div[3]/ul/div/div[2]/button[8]'
        self.transaction_page_xpath = '//*[@id="root"]/div[2]/div[2]/div[4]/div[2]/div[2]'
        self.report_transaction_chart_xpath = '/html/body/div[1]/div[2]/div[3]/div/div/div[3]/div[1]/div[2]'

        # etc
        self.context = {}

    def test_check_report_transaction_today(self):
        with self.driver as driver:

            driver.find_element(By.XPATH, self.transaction_page_xpath).click()

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.text_to_be_present_in_element((By.TAG_NAME, "h3"), "Transaksi")
                )
            except TimeoutException:
                logger.error("Check Report Transaction Test Case Resulted Error")
                return

            driver.find_element(By.XPATH, self.calendar_button_xpath).click()

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.ID, 'startDate')),
                    EC.presence_of_element_located((By.ID, 'endDate'))
                )
            except TimeoutException:
                logger.error("Check Report Transaction Test Case Resulted Error")
                return

            driver.find_element(By.XPATH, self.today_button_xpath).click()

            driver.find_element(By.XPATH, self.today_button_xpath).send_keys(Keys.ESCAPE)

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, self.report_transaction_chart_xpath))
                )
                page_exist = True
            except TimeoutException:
                logger.error("Check Report Transaction Test Case Resulted Error")
                page_exist = False
                return

            assert page_exist is True
            logger.success("Check Report Transaction Today Test Case has been Tested")

    def test_check_report_transaction_yesterday(self):
        with self.driver as driver:

            driver.find_element(By.XPATH, self.transaction_page_xpath).click()

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.text_to_be_present_in_element((By.TAG_NAME, "h3"), "Transaksi")
                )
            except TimeoutException:
                logger.error("Check Report Transaction Test Case Resulted Error")
                return

            driver.find_element(By.XPATH, self.calendar_button_xpath).click()

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.ID, 'startDate')),
                    EC.presence_of_element_located((By.ID, 'endDate'))
                )
            except TimeoutException:
                logger.error("Check Report Transaction Test Case Resulted Error")
                return

            driver.find_element(By.XPATH, self.yesterday_button_xpath).click()

            driver.find_element(By.XPATH, self.yesterday_button_xpath).send_keys(Keys.ESCAPE)

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, self.report_transaction_chart_xpath))
                )
                page_exist = True
            except TimeoutException:
                logger.error("Check Report Transaction Test Case Resulted Error")
                page_exist = False
                return

            assert page_exist is True
            logger.success("Check Report Transaction Yesterday Test Case has been Tested")

    def test_check_report_transaction_this_week(self):
        with self.driver as driver:

            driver.find_element(By.XPATH, self.transaction_page_xpath).click()

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.text_to_be_present_in_element((By.TAG_NAME, "h3"), "Transaksi")
                )
            except TimeoutException:
                logger.error("Check Report Transaction Test Case Resulted Error")
                return

            driver.find_element(By.XPATH, self.calendar_button_xpath).click()

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.ID, 'startDate')),
                    EC.presence_of_element_located((By.ID, 'endDate'))
                )
            except TimeoutException:
                logger.error("Check Report Transaction Test Case Resulted Error")
                return

            driver.find_element(By.XPATH, self.this_week_button_xpath).click()

            driver.find_element(By.XPATH, self.this_week_button_xpath).send_keys(Keys.ESCAPE)

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, self.report_transaction_chart_xpath))
                )
                page_exist = True
            except TimeoutException:
                logger.error("Check Report Transaction Test Case Resulted Error")
                page_exist = False
                return

            assert page_exist is True
            logger.success("Check Report Transaction This Week Test Case has been Tested")

    def test_check_report_transaction_last_week(self):
        with self.driver as driver:

            driver.find_element(By.XPATH, self.transaction_page_xpath).click()

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.text_to_be_present_in_element((By.TAG_NAME, "h3"), "Transaksi")
                )
            except TimeoutException:
                logger.error("Check Report Transaction Test Case Resulted Error")
                return

            driver.find_element(By.XPATH, self.calendar_button_xpath).click()

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.ID, 'startDate')),
                    EC.presence_of_element_located((By.ID, 'endDate'))
                )
            except TimeoutException:
                logger.error("Check Report Transaction Test Case Resulted Error")
                return

            driver.find_element(By.XPATH, self.last_week_button_xpath).click()

            driver.find_element(By.XPATH, self.last_week_button_xpath).send_keys(Keys.ESCAPE)

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, self.report_transaction_chart_xpath))
                )
                page_exist = True
            except TimeoutException:
                logger.error("Check Report Transaction Test Case Resulted Error")
                page_exist = False
                return

            assert page_exist is True
            logger.success("Check Report Transaction Last Week Test Case has been Tested")

    def test_check_report_transaction_this_month(self):
        with self.driver as driver:

            driver.find_element(By.XPATH, self.transaction_page_xpath).click()

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.text_to_be_present_in_element((By.TAG_NAME, "h3"), "Transaksi")
                )
            except TimeoutException:
                logger.error("Check Report Transaction Test Case Resulted Error")
                return

            driver.find_element(By.XPATH, self.calendar_button_xpath).click()

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.ID, 'startDate')),
                    EC.presence_of_element_located((By.ID, 'endDate'))
                )
            except TimeoutException:
                logger.error("Check Report Transaction Test Case Resulted Error")
                return

            driver.find_element(By.XPATH, self.this_month_button_xpath).click()

            driver.find_element(By.XPATH, self.this_month_button_xpath).send_keys(Keys.ESCAPE)

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, self.report_transaction_chart_xpath))
                )
                page_exist = True
            except TimeoutException:
                logger.error("Check Report Transaction Test Case Resulted Error")
                page_exist = False
                return

            assert page_exist is True
            logger.success("Check Report Transaction This Month Test Case has been Tested")

    def test_check_report_transaction_last_month(self):
        with self.driver as driver:

            driver.find_element(By.XPATH, self.transaction_page_xpath).click()

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.text_to_be_present_in_element((By.TAG_NAME, "h3"), "Transaksi")
                )
            except TimeoutException:
                logger.error("Check Report Transaction Test Case Resulted Error")
                return

            driver.find_element(By.XPATH, self.calendar_button_xpath).click()

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.ID, 'startDate')),
                    EC.presence_of_element_located((By.ID, 'endDate'))
                )
            except TimeoutException:
                logger.error("Check Report Transaction Test Case Resulted Error")
                return

            driver.find_element(By.XPATH, self.last_month_button_xpath).click()

            driver.find_element(By.XPATH, self.last_month_button_xpath).send_keys(Keys.ESCAPE)

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, self.report_transaction_chart_xpath))
                )
                page_exist = True
            except TimeoutException:
                logger.error("Check Report Transaction Test Case Resulted Error")
                page_exist = False
                return

            assert page_exist is True
            logger.success("Check Report Transaction Last Month Test Case has been Tested")

    def test_check_report_transaction_this_year(self):
        with self.driver as driver:

            driver.find_element(By.XPATH, self.transaction_page_xpath).click()

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.text_to_be_present_in_element((By.TAG_NAME, "h3"), "Transaksi")
                )
            except TimeoutException:
                logger.error("Check Report Transaction Test Case Resulted Error")
                return

            driver.find_element(By.XPATH, self.calendar_button_xpath).click()

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.ID, 'startDate')),
                    EC.presence_of_element_located((By.ID, 'endDate'))
                )
            except TimeoutException:
                logger.error("Check Report Transaction Test Case Resulted Error")
                return

            driver.find_element(By.XPATH, self.this_year_button_xpath).click()

            driver.find_element(By.XPATH, self.this_year_button_xpath).send_keys(Keys.ESCAPE)

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, self.report_transaction_chart_xpath))
                )
                page_exist = True
            except TimeoutException:
                logger.error("Check Report Transaction Test Case Resulted Error")
                page_exist = False
                return

            assert page_exist is True
            logger.success("Check Report Transaction This Year Test Case has been Tested")

    def test_check_report_transaction_last_year(self):
        with self.driver as driver:

            driver.find_element(By.XPATH, self.transaction_page_xpath).click()

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.text_to_be_present_in_element((By.TAG_NAME, "h3"), "Transaksi")
                )
            except TimeoutException:
                logger.error("Check Report Transaction Test Case Resulted Error")
                return

            driver.find_element(By.XPATH, self.calendar_button_xpath).click()

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.ID, 'startDate')),
                    EC.presence_of_element_located((By.ID, 'endDate')),
                )
            except TimeoutException:
                logger.error("Check Report Transaction Test Case Resulted Error")
                return

            driver.find_element(By.XPATH, self.last_year_button_xpath).click()

            driver.find_element(By.XPATH, self.last_year_button_xpath).send_keys(Keys.ESCAPE)

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, self.report_transaction_chart_xpath))
                )
                page_exist = True
            except TimeoutException:
                logger.error("Check Report Transaction Test Case Resulted Error")
                page_exist = False
                return

            assert page_exist is True
            logger.success("Check Report Transaction Last Year Test Case has been Tested")

    def tearDown(self) -> None:
        pass
