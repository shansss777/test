import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base


class Client_information_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    first_name = "//input[@id='first-name']"
    second_name = "//input[@id='last-name']"
    zip_code = "//input[@id='postal-code']"
    continue_button = "//input[@id='continue']"


    # Getters

    def get_first_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.first_name)))

    def get_second_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.second_name)))

    def get_zip_code(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.zip_code)))

    def get_continue_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.continue_button)))


    # Action

    def input_first_name(self, first_name):
        self.get_first_name().send_keys(first_name)
        print("Input first_name")

    def input_second_name(self, second_name):
        self.get_second_name().send_keys(second_name)
        print("Input second_name")


    def input_zip_code(self, zip_code):
        self.get_zip_code().send_keys(zip_code)
        print("Input zip_code")

    def click_continue_button(self):
        self.get_continue_button().click()
        print("Click continue_button")

    # Methods

    def input_info(self):
        self.get_current_url()
        self.input_first_name("Pavel")
        self.input_second_name("Bregovich")
        self.input_zip_code("123123")
        self.click_continue_button()






        # if login_name == "standard_user" or login_name == "problem_user":
        #
        #     user_name = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='user-name']")))
        #     user_name.send_keys(login_name)
        #     print("Enter Login")
        #     password = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='password']")))
        #     password.send_keys(login_password)
        #     print("Enter Password")
        #     password.send_keys(Keys.RETURN)
        #     print("Click Button Login")
        #     time.sleep(2)
        #
        # elif login_name == "locked_out_user":
        #
        #     user_name = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='user-name']")))
        #     user_name.send_keys(login_name)
        #     print("Enter Login")
        #     password = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='password']")))
        #     password.send_keys(login_password)
        #     print("Enter Password")
        #     password.send_keys(Keys.RETURN)
        #     time.sleep(2)
        #
        #
        # elif login_name == "performance_glitch_user":
        #
        #     user_name = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='user-name']")))
        #     user_name.send_keys(login_name)
        #     print("Enter Login")
        #     password = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='password']")))
        #     password.send_keys(login_password)
        #     print("Enter Password")
        #     login_button = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='login-button']")))
        #     login_button.click()
        #     time.sleep(4)
        #     # login_button.click()
        #     print("Click Button Login")
        #     time.sleep(2)


