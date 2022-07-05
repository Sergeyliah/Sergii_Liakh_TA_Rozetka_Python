from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class HomePage(BasePage):
    URL = "https://rozetka.com.ua/"
    PRODUCT = "Велосипед Genio Lunox 20"
    SEARCH_FIELD = (By.XPATH, "//input[@name='search']")
    SEARCH_BUTTON = (By.XPATH, "//button[text()=' Найти ']")

    def input_data_to_search_field(self, product):
        self.element_is_visible(self.SEARCH_FIELD).send_keys(product)
        self.element_is_visible(self.SEARCH_BUTTON).click()
