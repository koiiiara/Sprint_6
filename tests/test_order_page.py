import allure
import data
from conftest import *
from locators.main_page_locators import MainPageLocators
from pages.main_page import MainPage
from pages.order_page import OrderPage


class TestOrderPage:

    @allure.title("Проверка страницы заказа самоката")
    @allure.description("Кликаем по кнопке 'Заказать', заполняем поля и проверяем, что заказ успешно создан")
    @pytest.mark.parametrize(
        'locator, order_data' ,
        [
            (MainPageLocators.TOP_ORDER_BUTTON_LOCATOR, data.ORDER_DATASETS[0]),
            (MainPageLocators.BOTTOM_ORDER_BUTTON_LOCATOR, data.ORDER_DATASETS[1])
        ]
    )
    def test_order_create(self, driver, locator, order_data):
        main_page = MainPage(driver)
        main_page.click_order_button(locator)
        order_page = OrderPage(driver)
        order_page.wait_order_page_load()
        order_page.fill_order_client_fields(order_data)
        order_page.click_next_button()
        order_page.fill_order_scooter_fields(order_data)
        order_page.click_order_button()
        order_created_text = order_page.get_order_created_text()
        assert "Номер заказа" in order_created_text



