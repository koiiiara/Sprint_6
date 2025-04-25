import pytest
from selenium import webdriver
from pages.main_page import MainPage
import data

@pytest.fixture()
def driver():
    driver = webdriver.Firefox()
    driver.get(data.MAIN_PAGE_URL)
    yield driver
    driver.quit()

@pytest.fixture()
def main_page(driver):
    page = MainPage(driver)
    page.go_to_url(data.MAIN_PAGE_URL)
    return page
