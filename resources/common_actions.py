from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from faker import Faker
from webconfig import Driver
from selenium.webdriver.support.wait import WebDriverWait

fake = Faker()
userDetails = []


class CommonActions:

    def __init__(self):
        self.browse = Driver()
        self.driver = self.browse.driver
        self.driver.maximize_window()
        self.action = ActionChains(self.driver)
        self.wait = WebDriverWait(self.driver, 10)
        self.userDetails = []

    def launch_page(self, url):
        self.driver.get(url)

    def click_element(self, element):
        self.wait_for_presence(element)
        self.driver.find_element(By.CSS_SELECTOR, element).click()

    def type_text(self, field, text):
        self.wait_for_presence(field)
        self.driver.find_element(By.CSS_SELECTOR, field).send_keys(text)

    def wait_for_presence(self, element):

        self.wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, element)))

    def wait_for_selection(self, element):

        self.wait.until(ec.element_located_to_be_selected((By.CSS_SELECTOR, element)))

    def wait_for_text_presence(self, element, text):

        self.wait.until(ec.text_to_be_present_in_element((By.CSS_SELECTOR, element), text))

    def verify_text(self, element, message):
        try:
            self.wait_for_presence(element)
            expect_text = self.driver.find_element(By.CSS_SELECTOR, element).text
            assert expect_text in message
        except AssertionError:
            return AssertionError

    def select_value(self, element, value):

        self.wait_for_presence(element)
        ele = self.driver.find_element(By.CSS_SELECTOR, element)
        select = Select(ele)
        select.select_by_value(value)

    def user_details(self):

        self.userDetails = [
            fake.first_name(), fake.last_name(), fake.street_address(), fake.city(), fake.state(),
            fake.zipcode(), fake.phone_number(), fake.ssn(), fake.user_name(), 'Test1234@', 'Test1234@'
        ]
        return self.userDetails

    def fetch_elements(self, elements):

        return self.driver.find_elements(By.CSS_SELECTOR, elements)

    def execute_click_action(self, element):

        self.wait_for_presence(element)
        ele = self.driver.find_element(By.CSS_SELECTOR, element)
        self.driver.execute_script("arguments[0].click();", ele)

    def click_back(self):

        self.driver.back()
