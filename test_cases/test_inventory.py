import time

from POM.login_page import LoginPage
from POM.inventory_page import InventoryPage
from POM.cart_page import CartPage
from POM.product_page import ProductPage
from selenium.webdriver.common.by import By


def login(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("standard_user", "secret_sauce")


def test_add_to_cart(driver):
    login(driver)
    inventory = InventoryPage(driver)
    inventory.add_first_product()
    inventory.open_cart()
    cart = CartPage(driver)
    assert cart.is_loaded()
    assert cart.get_cart_item_name() != ""


def test_remove_from_cart(driver):
    login(driver)
    inventory = InventoryPage(driver)
    inventory.add_first_product()
    inventory.remove_first_product()
    assert "Add to cart" in inventory.find(inventory.FIRST_ADD_TO_CART).text


def test_sort_products(driver):
    login(driver)
    inventory = InventoryPage(driver)
    inventory.sort_by_z_to_a()
    first_item_text = inventory.find((By.CLASS_NAME, "inventory_item_name")).text
    assert first_item_text[0] in "ZYXWVUTSRQPONMLKJIHGFEDCBA"



def test_open_product_details(driver):
    login(driver)
    inventory = InventoryPage(driver)
    product_name = inventory.find(inventory.FIRST_PRODUCT).text
    inventory.open_first_product()
    product = ProductPage(driver)
    assert product.get_title() == product_name


def test_logout(driver):
    login(driver)
    inventory = InventoryPage(driver)
    driver.find_element("id", "react-burger-menu-btn").click()
    driver.find_element("id", "logout_sidebar_link").click()
    assert "https://www.saucedemo.com/" in driver.current_url
    time.sleep(3)

