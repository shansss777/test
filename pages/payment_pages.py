import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base


class Payment_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators


    finish_button = "//button[@id='finish']" #add_product



    # Getters

    def get_finish_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.finish_button)))



    # Action

    def click_finish_button(self):
        self.get_finish_button().click()
        print("Click finish_button")



    # Methods

    def payment(self):
        self.get_current_url()
        self.click_finish_button()






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


