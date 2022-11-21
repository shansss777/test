import pytest


@pytest.fixture()
def set_up():
    print("Start Test")
    # driver = webdriver.Chrome(executable_path='C:\\Users\\Onyx87\\PycharmProjects\\main_project\\chromedriver.exe')
    # url = 'https://www.saucedemo.com/'
    # self.driver.get(self.url)
    # self.driver.maximize_window()

    yield

    # driver.quit()
    print("Finish Test")

@pytest.fixture(scope="module")
def set_group():
    print("Enter system")

    yield

    print("Exit system")