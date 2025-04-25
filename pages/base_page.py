from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def go_to_url(self, url):
        self.driver.get(url)

    def get_page_url(self):
        return self.driver.current_url

    def find_element_with_wait(self, locator):
        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(locator)
        )
        return self.driver.find_element(*locator)

    def scroll_to_element(self, locator):
        self.driver.execute_script("arguments[0].scrollIntoView(true);", self.driver.find_element(*locator))

    def click_to_element(self, locator):
        self.find_element_with_wait(locator).click()

    def send_keys_to_element(self, locator, keys):
        self.find_element_with_wait(locator).send_keys(keys)

    def get_text_from_element(self, locator):
        return self.find_element_with_wait(locator).text

    def format_locator(self, locator, text):
        by, locator_str = locator
        locator_str = locator_str.format(text)
        return by, locator_str

    def send_return_to_element(self, locator):
        self.find_element_with_wait(locator).send_keys(Keys.RETURN)

    def switch_window_to_new_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])

