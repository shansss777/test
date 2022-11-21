import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.cart_pages import Cart_page
from pages.client_information_pages import Client_information_page
from pages.finish_pages import Finish_page
from pages.login_pages import Login_page
from pages.main_pages import Main_page
from pages.payment_pages import Payment_page

# @pytest.mark.run(order=3)
def test_buy_product_1(set_up, set_group):
    driver = webdriver.Chrome(executable_path='C:\\Users\\Onyx87\\PycharmProjects\\main_project\\chromedriver.exe')
    print("Start test 1")

    login = Login_page(driver)
    login.authorization()

    mp = Main_page(driver)
    mp.select_products_1()

    cp = Cart_page(driver)
    cp.click_checkout_button()

    cip = Client_information_page(driver)
    cip.input_info()

    pp = Payment_page(driver)
    pp.payment()

    f = Finish_page(driver)
    f.finish()
    driver.quit()
    print("Finish test 1")

# @pytest.mark.run(order=1)
def test_buy_product_2(set_up, set_group):
    driver = webdriver.Chrome(executable_path='C:\\Users\\Onyx87\\PycharmProjects\\main_project\\chromedriver.exe')

    print("Start test 2")
    login = Login_page(driver)
    login.authorization()

    mp = Main_page(driver)
    mp.select_products_2()

    cp = Cart_page(driver)
    cp.click_checkout_button()
    driver.quit()
    print("Finish test 2")
#
# @pytest.mark.run(order=2)
def test_buy_product_3(set_up, set_group):
    driver = webdriver.Chrome(executable_path='C:\\Users\\Onyx87\\PycharmProjects\\main_project\\chromedriver.exe')

    print("Start test 3")
    login = Login_page(driver)
    login.authorization()

    mp = Main_page(driver)
    mp.select_products_3()

    cp = Cart_page(driver)
    cp.click_checkout_button()
    print("Finish test 3")
    driver.quit()

    # time.sleep(5)
