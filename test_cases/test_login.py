import time

from POM.login_page import LoginPage
from POM.inventory_page import InventoryPage

def test_valid_login(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)

    login_page.load()
    login_page.login("standard_user", "secret_sauce")
    assert inventory_page.is_loaded() is True

def test_invalid_login(driver):
    login_page = LoginPage(driver)

    login_page.load()
    login_page.login("wrong_user", "wrong_pass")

    assert "Epic sadface" in login_page.get_error()
