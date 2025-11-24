from selenium.webdriver.common.by import By
from POM.base_page import BasePage

class ProductPage(BasePage):

    PRODUCT_TITLE = (By.CLASS_NAME, "inventory_details_name")

    def get_title(self):
        return self.get_text(self.PRODUCT_TITLE)
