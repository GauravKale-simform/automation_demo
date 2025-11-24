from selenium.webdriver.common.by import By
from POM.base_page import BasePage


class CartPage(BasePage):

    CART_TITLE = (By.CLASS_NAME, "title")
    CART_ITEM = (By.CLASS_NAME, "inventory_item_name")

    CART_ITEMS = (By.CLASS_NAME, "cart_item")
    REMOVE_BUTTON = (By.CLASS_NAME, "cart_button")
    CHECKOUT_BUTTON = (By.ID, "checkout")
    CONTINUE_SHOPPING = (By.ID, "continue-shopping")

    def is_loaded(self):
        return self.get_text(self.CART_TITLE) == "Your Cart"

    def get_cart_item_name(self):
        return self.get_text(self.CART_ITEM)

    # NEW FUNCTIONS
    def get_cart_count(self):
        return len(self.find_all(self.CART_ITEMS))

    def remove_first_item(self):
        self.find(self.REMOVE_BUTTON).click()

    def go_to_checkout(self):
        self.find(self.CHECKOUT_BUTTON).click()

    def continue_shopping(self):
        self.find(self.CONTINUE_SHOPPING).click()
