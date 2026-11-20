from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from utils.logger import logger

def test_inventory(driver):
    try:
        logger.info("Testing inventory functionality.")
        login_page = LoginPage(driver)
        inventory_page = InventoryPage(driver)

        driver.get("https://www.saucedemo.com/")
        login_page.login("standard_user", "secret_sauce")
        products = inventory_page.get_products()
        logger.info(f"Retrieved {len(products)} products.")
        assert len(products) > 0
        assert inventory_page.get_name_first_product() == "Sauce Labs Backpack"
        assert inventory_page.get_price_first_product() == "$29.99"
        assert inventory_page.is_menu_displayed()
        assert inventory_page.is_filter_displayed()
        logger.info("Inventory functionality validated.")
    except Exception:
        logger.exception(f"An error occurred during the inventory test")
        raise