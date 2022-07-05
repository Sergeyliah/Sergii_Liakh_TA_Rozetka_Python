from selenium.webdriver.common.by import By
from pages.shopping_cart_page import ShoppingCartPage
from pages.home_page import HomePage
from pages.search_results_page import SearchResultPage
from pages.product_page import ProductPage


class TestAddToCart:

    def test_add_to_cart(self, driver):
        home_page = HomePage(driver)
        home_page.open(HomePage.URL)
        home_page.input_data_to_search_field(HomePage.PRODUCT)
        SearchResultPage(driver).buy_item(driver)
        assert driver.find_element(By.XPATH, ProductPage.CHECK_CART).text == ProductPage.TEXT

    def test_remove_item_from_cart(self, driver):
        home_page = HomePage(driver)
        home_page.open(HomePage.URL)
        home_page.input_data_to_search_field(HomePage.PRODUCT)
        shopping_cart_page = SearchResultPage(driver).buy_item(driver).open_cart(driver). \
            click_button(driver, ShoppingCartPage.ITEM_MENU). \
            click_button(driver, ShoppingCartPage.DELETE_FROM_CART_BUTTON)
        assert (shopping_cart_page.element_is_visible(ShoppingCartPage.CHECK_IS_CART_EMPTY)).text == ShoppingCartPage.TEXT
