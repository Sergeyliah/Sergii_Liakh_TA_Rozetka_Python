from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ProductPage(BasePage):
    BUY_BUTTON = (By.XPATH, "//span[@class='buy-button__label ng-star-inserted'][text() = ' Купить ']")
    CART_BUTTON = (By.XPATH, "//button[@class='header__button ng-star-inserted header__button--active']")
    TEXT = "1"
    CHECK_CART = "//span[@class='counter counter--green ng-star-inserted']"

    def click_buy_button(self):
        self.element_is_visible(self.BUY_BUTTON).click()

    def click_cart_button(self):
        self.element_is_visible(self.CART_BUTTON).click()
