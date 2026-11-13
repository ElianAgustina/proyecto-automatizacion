from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def get_name_product(self):
        return self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "inventory_item_name"))).text
    
        

    def get_price_product(self):
        price_product = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "inventory_item_price"))).text
        print(f"Precio del producto en el carrito: {price_product}")
        return float(price_product.replace("$", ""))  # Convertir a float y eliminar el símbolo de dólar