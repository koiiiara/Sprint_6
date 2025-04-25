from selenium.webdriver.common.by import By


class TransitionsPageLocators:

    # Локатор логотипа Самокат
    SCOOTER_LOGO_LOCATOR = (By.XPATH, "//a[contains(@class, 'Header_LogoScooter')]")

    # Локатор логотипа Яндекс
    YANDEX_LOGO_LOCATOR = (By.XPATH, "//a[contains(@class, 'Header_LogoYandex')]")

    # Локатор кнопки поиска на странице Дзен
    SEARCH_BUTTON_LOCATOR = (By.XPATH, "//button[text()='Найти']")

    # Локатор картинки самоката на главной странице
    SCOOTER_IMG_LOCATOR = (By.XPATH, "//img[@alt='Scooter blueprint']")