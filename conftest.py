import pytest
from selenium import webdriver
from pages import Goodreads
EMAIL = "ratiumarianalexandru@gmail.com"
PASSWORD = "Testamazon123@"

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture
def logged_in_driver(driver):
    g = Goodreads(driver)
    g.open()
    g.click_signin()
    g.fill_sign_in(EMAIL, PASSWORD)
    g.verify_logged_in()
    return driver