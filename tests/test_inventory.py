from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

def test_inventory(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)

    driver.get("https://www.saucedemo.com/")
    login_page.login("standard_user", "secret_sauce")
    products = inventory_page.get_products()
    assert len(products) > 0
    assert inventory_page.get_name_first_product() == "Sauce Labs Backpack"
    assert inventory_page.get_price_first_product() == "$29.99"
    assert inventory_page.is_menu_displayed()
    assert inventory_page.is_filter_displayed()
