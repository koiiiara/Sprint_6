from selenium.webdriver.common.by import By

class MainPageLocators:

    # Форматируемый локатор для вопроса
    QUESTION_LOCATOR = (By.XPATH, "//div[@id='accordion__heading-{}']")

    # Форматируемый локатор для ответа
    ANSWER_LOCATOR = (By.XPATH, "//div[@id='accordion__panel-{}']")

    # Локатор для последнего вопроса
    LAST_QUESTION_LOCATOR_TO_SCROLL = (By.XPATH, "//div[@id='accordion__heading-7']")

    # Локатор для кнопки "Заказать" вверху страницы
    TOP_ORDER_BUTTON_LOCATOR = (By.XPATH, "//button[text()='Заказать']")

    # Локатор для кнопки "Заказать" внизу страницы
    BOTTOM_ORDER_BUTTON_LOCATOR = (By.XPATH, "//div[contains(@class, 'Home_FinishButton')]//button[text()='Заказать']")

