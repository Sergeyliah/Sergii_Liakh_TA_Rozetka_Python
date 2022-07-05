from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ShoppingCartPage(BasePage):
    ITEM_MENU = (By.XPATH, "//button[@class='button button--white button--small popup-menu__toggle popup-menu__toggle--context']")
    DELETE_FROM_CART_BUTTON = (By.XPATH, "//button[@class='button button--medium button--with-icon button--link context-menu-actions__button']")
    CHECK_IS_CART_EMPTY = (By.XPATH, "//p[@class='cart-dummy__caption']")
    CHECK_CART = "//span[@class='counter counter--green ng-star-inserted']"
    TEXT = "Но это никогда не поздно исправить :)"

    def click_button(self, driver, locator):
        self.element_is_visible(locator).click()
        return ShoppingCartPage(driver)
