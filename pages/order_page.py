import allure
from conftest import driver
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage


class OrderPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Дожидаемся перехода на страницу заказа")
    def wait_order_page_load(self):
        self.find_element_with_wait(OrderPageLocators.NAME_FIELD_LOCATOR)


    @allure.step("Заполняем поля страницы заказа 'Для кого самокат'")
    def fill_order_client_fields(self, order_dataset):
        self.send_keys_to_element(OrderPageLocators.NAME_FIELD_LOCATOR, order_dataset['name'])
        self.send_keys_to_element(OrderPageLocators.SURNAME_FIELD_LOCATOR, order_dataset['surname'])
        self.send_keys_to_element(OrderPageLocators.ADDRESS_FIELD_LOCATOR, order_dataset['address'])
        self.click_to_element(OrderPageLocators.METRO_FIELD_LOCATOR)
        metro_station_locator = self.format_locator(OrderPageLocators.METRO_STATION_LOCATOR, order_dataset['metro'])
        self.scroll_to_element(metro_station_locator)
        self.click_to_element(metro_station_locator)
        self.send_keys_to_element(OrderPageLocators.PHONE_FIELD_LOCATOR, order_dataset['phone'])

    @allure.step("Нажимаем кнопку 'Далее' на странице заказа и ждем перехода")
    def click_next_button(self):
        self.click_to_element(OrderPageLocators.NEXT_BUTTON_LOCATOR)
        self.find_element_with_wait(OrderPageLocators.DATE_FIELD_LOCATOR)


    @allure.step("Заполняем поля страницы заказа 'Про аренду'")
    def fill_order_scooter_fields(self, order_dataset):
        self.send_keys_to_element(OrderPageLocators.DATE_FIELD_LOCATOR, order_dataset['date'])
        self.send_return_to_element(OrderPageLocators.DATE_FIELD_LOCATOR)
        self.click_to_element(OrderPageLocators.DURATION_FIELD_LOCATOR)
        rent_duration = self.format_locator(OrderPageLocators.DURATION_SELECT_LOCATOR, order_dataset["duration"])
        self.scroll_to_element(rent_duration)
        self.click_to_element(rent_duration)
        color_checkbox_locator = self.format_locator(OrderPageLocators.COLOR_CHECKBOX_LOCATOR, order_dataset['color'])
        self.click_to_element(color_checkbox_locator)
        self.send_keys_to_element(OrderPageLocators.COMMENT_FIELD_LOCATOR, order_dataset['comment'])

    @allure.step("Кликаем по кнопке 'Заказать' внизу страницы заказа и подтверждаем заказ")
    def click_order_button(self):
        self.click_to_element(OrderPageLocators.BOTTOM_ORDER_BUTTON_LOCATOR)
        self.find_element_with_wait(OrderPageLocators.CONFIRMATION_POPUP_TITLE_LOCATOR)
        self.click_to_element(OrderPageLocators.CONFIRMATION_POPUP_YES_BUTTON_LOCATOR)

    @allure.step("Ждем появление окна с надписью 'Заказ оформлен' и получаем текст сообщения")
    def get_order_created_text(self):
        self.find_element_with_wait(OrderPageLocators.ORDER_CREATED_TITLE_LOCATOR)
        return self.get_text_from_element(OrderPageLocators.ORDER_CREATED_TEXT_LOCATOR)





