import allure
from conftest import *
from pages.transitions_page import TransitionsPage


class TestTransitionsPage:

    @allure.title('Проверяем переход с страницы заказа на главную')
    @allure.description(
        'Кликаем по логотипу Самокат на странице заказа и проверяем, что произошел переход на главную страницу')
    def test_transition_to_home(self, driver):
        transitions_page = TransitionsPage(driver)
        transitions_page.go_to_url(data.ORDER_PAGE_URL)
        transitions_page.click_to_scooter_logo()
        transitions_page.wait_home_page_load()
        current_url = transitions_page.get_page_url()
        assert current_url == "https://qa-scooter.praktikum-services.ru/"

    @allure.title('Проверяем переход с главной страницы на Дзен')
    @allure.description(
        'Кликаем по логотипу Яндекс на главной странице и проверяем, что произошел переход на страницу Дзен')
    def test_transition_to_dzen(self, driver):
        transitions_page = TransitionsPage(driver)
        transitions_page.go_to_url(data.MAIN_PAGE_URL)
        transitions_page.click_to_yandex_logo()
        transitions_page.switch_window_to_new_tab()
        transitions_page.wait_dzen_page_load()
        current_url =  transitions_page.get_page_url()
        assert current_url == "https://dzen.ru/?yredirect=true"