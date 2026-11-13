from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from conftest import driver
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from utils.reader import read_products_json


def test_cart(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)

    # Abrir la página de inicio de sesión
    driver.get("https://www.saucedemo.com/")
    login_page.login("standard_user", "secret_sauce")

    # Obtener el primer producto del archivo JSON
    products = read_products_json()[0] 
    print(f"Producto a agregar al carrito: {products['name']} - Precio: {products['price']}")

    # Agregar el producto al carrito desde el json
    inventory_page.add_product_to_cart(products["name"])

    assert inventory_page.count_products().text == "1"

        # Ir al carrito
    inventory_page.go_to_cart()

        # Verificar que el producto agregado al carrito sea el mismo que se obtuvo del archivo JSON
    assert cart_page.get_name_product() == products["name"]

    #validar que el precio del producto en el carrito sea el mismo que se obtuvo del archivo JSON
    assert cart_page.get_price_product() == products["price"]
