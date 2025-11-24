from selenium.webdriver.common.by import By
from POM.base_page import BasePage

class InventoryPage(BasePage):

    TITLE = (By.CLASS_NAME, "title")
    FIRST_ADD_TO_CART = (By.CSS_SELECTOR, "button.btn_inventory")
    CART_ICON = (By.CLASS_NAME, "shopping_cart_link")
    FIRST_REMOVE_BTN = (By.XPATH, "(//button[contains(text(),'Remove')])[1]")
    SORT_DROPDOWN = (By.CLASS_NAME, "product_sort_container")
    FIRST_PRODUCT = (By.CLASS_NAME, "inventory_item_name")
    OPTION_Z_TO_A = (By.XPATH, "//option[@value='za']")

    def is_loaded(self):
        return self.get_text(self.TITLE) == "Products"

    def add_first_product(self):
        self.click(self.FIRST_ADD_TO_CART)

    def remove_first_product(self):
        self.click(self.FIRST_REMOVE_BTN)

    def open_cart(self):
        self.click(self.CART_ICON)

    def sort_by_z_to_a(self):
            # dropdown
        self.click(self.SORT_DROPDOWN)
            # Now click the Z -> A
        self.click(self.OPTION_Z_TO_A)

    def open_first_product(self):
        self.click(self.FIRST_PRODUCT)
