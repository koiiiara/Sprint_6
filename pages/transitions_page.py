import allure
from locators.transitions_page_locators import TransitionsPageLocators
from pages.base_page import BasePage


class TransitionsPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Кликаем по логотипу Самокат')
    def click_to_scooter_logo(self):
        self.click_to_element(TransitionsPageLocators.SCOOTER_LOGO_LOCATOR)

    @allure.step('Кликаем по логотипу яндекс')
    def click_to_yandex_logo(self):
        self.click_to_element(TransitionsPageLocators.YANDEX_LOGO_LOCATOR)

    @allure.step("Ждем загрузки страницы Дзен")
    def wait_dzen_page_load(self):
        self.find_element_with_wait(TransitionsPageLocators.SEARCH_BUTTON_LOCATOR)

    @allure.step("Ждем загрузки главной страницы")
    def wait_home_page_load(self):
        self.find_element_with_wait(TransitionsPageLocators.SCOOTER_IMG_LOCATOR)




