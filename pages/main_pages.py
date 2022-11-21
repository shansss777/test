import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base


class Main_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    # name_product_1 = "//div[@class='inventory_item_name']" #name
    select_product_1 = "//button[@id='add-to-cart-sauce-labs-backpack']" #add_product
    select_product_2 = "//button[@id='add-to-cart-sauce-labs-bike-light']"
    select_product_3 = "//button[@id='add-to-cart-sauce-labs-bolt-t-shirt']"
    cart = "//a[@class='shopping_cart_link']" #go in cart
    menu = "//button[@id='react-burger-menu-btn']"
    about = "//a[@id='about_sidebar_link']"


    # Getters

    def get_select_product_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_product_1)))

    def get_select_product_2(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_product_2)))

    def get_select_product_3(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_product_3)))

    def get_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart)))

    def get_menu(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.menu)))
    #
    def get_about(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.about)))


    # Action

    def click_select_product_1(self):
        self.get_select_product_1().click()
        print("Click select product 1")

    def click_select_product_2(self):
        self.get_select_product_2().click()
        print("Click select product 2")

    def click_select_product_3(self):
        self.get_select_product_3().click()
        print("Click select product 3")

    def click_cart(self):
        self.get_cart().click()
        print("Click cart")

    def click_menu(self):
        self.get_menu().click()
        print("Click menu")

    def click_about(self):
        self.get_about().click()
        print("Click about")

    # Methods

    def select_products_1(self):
        self.get_current_url()
        self.click_select_product_1()
        self.click_cart()

    def select_products_2(self):
        self.get_current_url()
        self.click_select_product_2()
        self.click_cart()

    def select_products_3(self):
        self.get_current_url()
        self.click_select_product_3()
        self.click_cart()

    def select_menu_about(self):
        self.get_current_url()
        self.click_menu()
        self.click_about()
        self.assert_url('https://saucelabs.com/')






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


