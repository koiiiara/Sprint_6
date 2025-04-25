from selenium.webdriver.common.by import By

class OrderPageLocators:

    # Локатор для поля Имя
    NAME_FIELD_LOCATOR = (By.CSS_SELECTOR, "[placeholder='* Имя']")

    # Локатор для поля Фамилия
    SURNAME_FIELD_LOCATOR = (By.CSS_SELECTOR, "[placeholder='* Фамилия']")

    # Локатор для поля Адрес
    ADDRESS_FIELD_LOCATOR = (By.CSS_SELECTOR, "[placeholder='* Адрес: куда привезти заказ']")

    # Локатор для поля Станция метро
    METRO_FIELD_LOCATOR = (By.CSS_SELECTOR, "[placeholder='* Станция метро']")

    # Локатор для поля Телефона
    PHONE_FIELD_LOCATOR = (By.CSS_SELECTOR, "[placeholder='* Телефон: на него позвонит курьер']")

    # Форматируемый локатор для станции метро
    METRO_STATION_LOCATOR = (By.XPATH, "//li/button//div[text()='{}']")

    # Локатор для кнопки "Далее" на странице заказа
    NEXT_BUTTON_LOCATOR = (By.XPATH, "//button[text()='Далее']")

    # Локатор для поля Когда привезти самокат
    DATE_FIELD_LOCATOR = (By.CSS_SELECTOR, "[placeholder='* Когда привезти самокат']")

    # Локатор для поля Срок аренды
    DURATION_FIELD_LOCATOR = (By.XPATH, "//div[text()='* Срок аренды']/parent::*")

    # Форматируемый локатор для выбора срока аренды
    DURATION_SELECT_LOCATOR = (By.XPATH, "//div[contains(@class, 'Dropdown-menu')]//div[text()='{}']")

    # Локатор для поля Цвет самоката
    COLOR_FIELD_LOCATOR = (By.XPATH, "//div[text()='Цвет самоката']")

    # Форматируемый локатор чек бокса цвета
    COLOR_CHECKBOX_LOCATOR = (By.XPATH, "//div[text()='Цвет самоката']/parent::div/label[@for='{}']")

    # Локатор для поля Когда привезти самокат
    COMMENT_FIELD_LOCATOR = (By.CSS_SELECTOR, "[placeholder='Комментарий для курьера']")

    # Локатор для кнопки "Заказать" внизу страницы
    BOTTOM_ORDER_BUTTON_LOCATOR = (By.XPATH, "//div[contains(@class, 'Order_Buttons')]//button[text()='Заказать']")

    # Локатор заголовка окна подтверждения заказа
    CONFIRMATION_POPUP_TITLE_LOCATOR = (By.XPATH, "//div[text()='Хотите оформить заказ?']")

    # Локатор кнопки "Да" в окне подтверждения заказа
    CONFIRMATION_POPUP_YES_BUTTON_LOCATOR = (By.XPATH, "//div[text()='Хотите оформить заказ?']/parent::div//button[text()='Да']")

    # Локатор для надписи "Заказ оформлен" в окне успешного заказа
    ORDER_CREATED_TITLE_LOCATOR = (By.XPATH, "//div[text()='Заказ оформлен']")

    # Локатор для текста в окне успешного заказа
    ORDER_CREATED_TEXT_LOCATOR = (By.XPATH, "//div[contains(@class, 'Order_Text')]")

