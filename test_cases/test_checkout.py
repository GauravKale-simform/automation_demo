from POM.login_page import LoginPage
from POM.inventory_page import InventoryPage
from POM.cart_page import CartPage
from POM.checkout_page import CheckoutPage


def login(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("standard_user", "secret_sauce")


def test_add_to_cart_and_open_cart(driver):
    login(driver)

    inventory = InventoryPage(driver)
    inventory.add_first_product()

    driver.find_element("id", "shopping_cart_container").click()
    cart = CartPage(driver)

    assert cart.get_cart_count() == 1


def test_remove_item_from_cart(driver):
    login(driver)

    inventory = InventoryPage(driver)
    inventory.add_first_product()

    driver.find_element("id", "shopping_cart_container").click()
    cart = CartPage(driver)

    cart.remove_first_item()
    assert cart.get_cart_count() == 0


def test_checkout_with_missing_info(driver):
    login(driver)

    inventory = InventoryPage(driver)
    inventory.add_first_product()

    driver.find_element("id", "shopping_cart_container").click()
    cart = CartPage(driver)
    cart.go_to_checkout()

    checkout = CheckoutPage(driver)
    checkout.continue_to_overview()

    assert "Error" in checkout.get_error()


def test_successful_checkout_flow(driver):
    login(driver)

    inventory = InventoryPage(driver)
    inventory.add_first_product()

    driver.find_element("id", "shopping_cart_container").click()
    cart = CartPage(driver)
    cart.go_to_checkout()

    checkout = CheckoutPage(driver)
    checkout.fill_information("Gaurav", "Kale", "411001")
    checkout.continue_to_overview()

    checkout.finish_order()
    assert checkout.get_success_message() == "Thank you for your order!"

    checkout.go_back_home()
    assert "inventory" in driver.current_url
    time.sleep(3)
