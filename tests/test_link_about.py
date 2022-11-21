import time

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


def test_buy_product(set_up):
    driver = webdriver.Chrome(executable_path='C:\\Users\\Onyx87\\PycharmProjects\\main_project\\chromedriver.exe')

    login = Login_page(driver)
    login.authorization()

    mp = Main_page(driver)
    mp.select_menu_about()
    driver.quit()







    # time.sleep(10)
