import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Кликаем на вопрос')
    def click_to_question(self, num):
        question_locator = self.format_locator(MainPageLocators.QUESTION_LOCATOR, num)
        self.scroll_to_element(MainPageLocators.LAST_QUESTION_LOCATOR_TO_SCROLL)
        self.click_to_element(question_locator)

    @allure.step('Получаем текст ответа')
    def get_answer_text(self, num):
        answer_locator = self.format_locator(MainPageLocators.ANSWER_LOCATOR, num)
        return self.get_text_from_element(answer_locator)

    @allure.step('Кликаем по кнопке заказать')
    def click_order_button(self, locator):
        self.scroll_to_element(locator)
        self.click_to_element(locator)



