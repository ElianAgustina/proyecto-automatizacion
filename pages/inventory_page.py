from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)  # Espera explícita de 10 segundos

    def get_products(self):
        products = self.driver.find_elements(By.CLASS_NAME,"inventory_item")
        return products
    
    def get_name_first_product(self):
        products = self.get_products()
        if products:
            first_product = products[0]
            name_product = first_product.find_element(By.CLASS_NAME,"inventory_item_name").text
            return name_product

    def get_price_first_product(self):
        products = self.get_products()
        if products:
            first_product = products[0]
            price_product = first_product.find_element(By.CLASS_NAME,"inventory_item_price").text
            return price_product

    def is_menu_displayed(self):
        menu = self.driver.find_element(By.ID,"react-burger-menu-btn")
        return menu.is_displayed()

    def is_filter_displayed(self):
        filter = self.driver.find_element(By.CLASS_NAME,"product_sort_container")
        return filter.is_displayed()