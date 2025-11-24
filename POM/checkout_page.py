from selenium.webdriver.common.by import By
from POM.base_page import BasePage


class CheckoutPage(BasePage):

    # Step One
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    ERROR_MSG = (By.CSS_SELECTOR, "h3[data-test='error']")

    # Step Two Overview
    ITEM_TOTAL = (By.CLASS_NAME, "summary_subtotal_label")
    TAX = (By.CLASS_NAME, "summary_tax_label")
    TOTAL = (By.CLASS_NAME, "summary_total_label")
    FINISH_BUTTON = (By.ID, "finish")

    # Success Page
    COMPLETE_HEADER = (By.CLASS_NAME, "complete-header")
    BACK_HOME = (By.ID, "back-to-products")

    def fill_information(self, first, last, postal):
        self.find(self.FIRST_NAME).send_keys(first)
        self.find(self.LAST_NAME).send_keys(last)
        self.find(self.POSTAL_CODE).send_keys(postal)

    def continue_to_overview(self):
        self.find(self.CONTINUE_BUTTON).click()

    def get_error(self):
        return self.find(self.ERROR_MSG).text

    def finish_order(self):
        self.find(self.FINISH_BUTTON).click()

    def get_success_message(self):
        return self.find(self.COMPLETE_HEADER).text

    def go_back_home(self):
        self.find(self.BACK_HOME).click()
