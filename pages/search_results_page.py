from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.shopping_cart_page import ShoppingCartPage


class SearchResultPage(BasePage):
    BUY_ITEM = (By.XPATH, "//button[@aria-label='Купить']")
    CART_BUTTON = (By.XPATH, "//button[@class='header__button ng-star-inserted header__button--active']")

    def buy_item(self, driver):
        self.element_is_visible(self.BUY_ITEM).click()
        return SearchResultPage(driver)

    def open_cart(self, driver):
        self.element_is_visible(self.CART_BUTTON).click()
        return ShoppingCartPage(driver)
