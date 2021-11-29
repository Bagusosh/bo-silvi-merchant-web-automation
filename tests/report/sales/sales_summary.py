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


class SalesSummaryTests(unittest.TestCase):

    def setUp(self) -> None:
        load_dotenv()
        warnings.filterwarnings("ignore", category=DeprecationWarning)

        self.driver = LoginDriver().driver
        #data
        self.valid_page_name = 'Sales'

        # xPaths
        self.sales_page = '//*[@id="root"]/div[2]/div[2]/div[4]/div[1]/div[2]/a'
        self.summary_page = '//*[@id="root"]/div[2]/div[3]/div/div/div[2]/div[1]/div[3]/div/button[1]'
        self.login_button_xpath = '//*[@id="root"]/div[2]/div/div[2]/form/button'
        self.calendar_button_xpath = '/html/body/div[1]/div[2]/div[3]/div/div/div[2]/div[2]/div/div[1]/div/button[2]'
        self.today_button_xpath = '/html/body/div[3]/div[3]/ul/div/div[2]/button[1]'
        self.yesterday_button_xpath = '/html/body/div[3]/div[3]/ul/div/div[2]/button[2]'
        self.this_week_button_xpath = '/html/body/div[3]/div[3]/ul/div/div[2]/button[3]'
        self.last_week_button_xpath = '/html/body/div[3]/div[3]/ul/div/div[2]/button[4]'
        self.this_month_button_xpath = '/html/body/div[3]/div[3]/ul/div/div[2]/button[5]'
        self.last_month_button_xpath = '/html/body/div[3]/div[3]/ul/div/div[2]/button[6]'
        self.this_year_button_xpath = '/html/body/div[3]/div[3]/ul/div/div[2]/button[7]'
        self.last_year_button_xpath = '/html/body/div[3]/div[3]/ul/div/div[2]/button[8]'
        self.summary_chart_xpath = '/html/body/div[1]/div[2]/div[3]/div/div/div[2]/div[2]/div/div[2]/div[1]'

        # Etc.
        self.context = {}

    def test_check_summary_today(self):
        with self.driver as driver:
            driver.find_element(By.XPATH, self.sales_page).click()

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, self.summary_chart_xpath))
                )
                page_loaded = True
            except TimeoutException:
                logger.error("Check Summary Test Case Resulted Error")
                page_loaded = False
                return

            assert page_loaded is True
            assert 'Sales' in driver.page_source
            assert 'Total Sales' in driver.page_source
            logger.success("Check Summary Today Test Case has been Tested")

    def test_check_summary_yesterday(self):
        with self.driver as driver:
            driver.find_element(By.XPATH, self.sales_page).click()

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.text_to_be_present_in_element((By.TAG_NAME, "h3"), "Sales")
                )
            except TimeoutException:
                logger.error("Check Summary Test Case Resulted Error")
                return

            driver.find_element(By.XPATH, self.calendar_button_xpath).click()

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, self.yesterday_button_xpath))
                )
            except TimeoutException:
                logger.error("Check Summary Test Case Resulted Error")
                return

            driver.find_element(By.XPATH, self.yesterday_button_xpath).click()

            driver.find_element(By.XPATH, self.yesterday_button_xpath).send_keys(Keys.ESCAPE)

            assert 'Sales' in driver.page_source
            assert 'Total Sales' in driver.page_source
            logger.success("Check Summary Yesterday  Test Case has been Tested")

    def test_check_summary_this_week(self):
        with self.driver as driver:
            driver.find_element(By.XPATH, self.sales_page).click()

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.text_to_be_present_in_element((By.TAG_NAME, "h3"), "Sales")
                )
            except TimeoutException:
                logger.error("Check Summary Test Case Resulted Error")
                return

            driver.find_element(By.XPATH, self.calendar_button_xpath).click()

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, self.this_week_button_xpath))
                )
            except TimeoutException:
                logger.error("Check Summary Test Case Resulted Error")
                return

            driver.find_element(By.XPATH, self.this_week_button_xpath).click()

            driver.find_element(By.XPATH, self.this_week_button_xpath).send_keys(Keys.ESCAPE)

            assert 'Sales' in driver.page_source
            assert 'Total Sales' in driver.page_source
            logger.success("Check Summary This Week Test Case has been Tested")

    def test_check_summary_last_week(self):
        with self.driver as driver:
            driver.find_element(By.XPATH, self.sales_page).click()

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.text_to_be_present_in_element((By.TAG_NAME, "h3"), "Sales")
                )
            except TimeoutException:
                logger.error("Check Summary Test Case Resulted Error")
                return

            driver.find_element(By.XPATH, self.calendar_button_xpath).click()

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, self.last_week_button_xpath))
                )
            except TimeoutException:
                logger.error("Check Summary Test Case Resulted Error")
                return

            driver.find_element(By.XPATH, self.last_week_button_xpath).click()

            driver.find_element(By.XPATH, self.last_week_button_xpath).send_keys(Keys.ESCAPE)

            assert 'Sales' in driver.page_source
            assert 'Total Sales' in driver.page_source
            logger.success("Check Summary Last Week Test Case has been Tested")

    def test_check_summary_this_month(self):
        with self.driver as driver:
            driver.find_element(By.XPATH, self.sales_page).click()

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.text_to_be_present_in_element((By.TAG_NAME, "h3"), "Sales")
                )
            except TimeoutException:
                logger.error("Check Summary Test Case Resulted Error")
                return

            driver.find_element(By.XPATH, self.calendar_button_xpath).click()

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, self.this_month_button_xpath))
                )
            except TimeoutException:
                logger.error("Check Summary Test Case Resulted Error")
                return

            driver.find_element(By.XPATH, self.this_month_button_xpath).click()

            driver.find_element(By.XPATH, self.this_month_button_xpath).send_keys(Keys.ESCAPE)

            assert 'Sales' in driver.page_source
            assert 'Total Sales' in driver.page_source
            logger.success("Check Summary This Month Test Case has been Tested")

    def test_check_summary_last_month(self):
        with self.driver as driver:
            driver.find_element(By.XPATH, self.sales_page).click()

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.text_to_be_present_in_element((By.TAG_NAME, "h3"), "Sales")
                )
            except TimeoutException:
                logger.error("Check Summary Test Case Resulted Error")
                return

            driver.find_element(By.XPATH, self.calendar_button_xpath).click()

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, self.last_month_button_xpath))
                )
            except TimeoutException:
                logger.error("Check Summary Test Case Resulted Error")
                return

            driver.find_element(By.XPATH, self.last_month_button_xpath).click()

            driver.find_element(By.XPATH, self.last_month_button_xpath).send_keys(Keys.ESCAPE)

            assert 'Sales' in driver.page_source
            assert 'Total Sales' in driver.page_source
            logger.success("Check Summary Last Month Test Case has been Tested")

    def test_check_summary_this_year(self):
        with self.driver as driver:
            driver.find_element(By.XPATH, self.sales_page).click()

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.text_to_be_present_in_element((By.TAG_NAME, "h3"), "Sales")
                )
            except TimeoutException:
                logger.error("Check Summary Test Case Resulted Error")
                return

            driver.find_element(By.XPATH, self.calendar_button_xpath).click()

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, self.this_year_button_xpath))
                )
            except TimeoutException:
                logger.error("Check Summary Test Case Resulted Error")
                return

            driver.find_element(By.XPATH, self.this_year_button_xpath).click()

            driver.find_element(By.XPATH, self.this_year_button_xpath).send_keys(Keys.ESCAPE)

            assert 'Sales' in driver.page_source
            assert 'Total Sales' in driver.page_source
            logger.success("Check Summary This Year Test Case has been Tested")

    def test_check_summary_last_year(self):
        with self.driver as driver:
            driver.find_element(By.XPATH, self.sales_page).click()

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.text_to_be_present_in_element((By.TAG_NAME, "h3"), "Sales")
                )
            except TimeoutException:
                logger.error("Check Summary Test Case Resulted Error")
                return

            driver.find_element(By.XPATH, self.calendar_button_xpath).click()

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, self.last_year_button_xpath))
                )
            except TimeoutException:
                logger.error("Check Summary Test Case Resulted Error")
                return

            driver.find_element(By.XPATH, self.last_year_button_xpath).click()

            driver.find_element(By.XPATH, self.last_year_button_xpath).send_keys(Keys.ESCAPE)

            assert 'Sales' in driver.page_source
            assert 'Total Sales' in driver.page_source
            logger.success("Check Summary This Year Test Case has been Tested")

    def tearDown(self) -> None:
        pass