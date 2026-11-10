from selenium import webdriver
from selenium.webdriver.common.by import By


def test_shopping_cart():
    driver = webdriver.Chrome()

    try:
        driver.get("https://www.saucedemo.com/")

        user = driver.find_element(By.ID, "user-name")
        password = driver.find_element(By.ID, "password")
        button_login = driver.find_element(By.ID, "login-button")

        user.send_keys("standard_user")
        password.send_keys("secret_sauce")
        button_login.click()

        # se verifica que estamos en la página de productos
        assert driver.title == "Swag Labs"

        # obtenemos el primer producto el primer producto
        products = driver.find_elements(By.CLASS_NAME, "inventory_item")
        assert len(products) > 0

        first_product = products[0]

        # se obtiene nombre del primer producto
        name_product = first_product.find_element(
            By.CLASS_NAME, "inventory_item_name"
        ).text

        # se agrega el primer producto al carrito
        add_button = first_product.find_element(
            By.CSS_SELECTOR, "button.btn_inventory"
        )
        add_button.click()

        # verificamoss que el contador del carrito sea 1
        cart_badge = driver.find_element(
            By.CLASS_NAME, "shopping_cart_badge"
        )

        assert cart_badge.text == "1"

        # Ir al carrito
        cart = driver.find_element(
            By.CLASS_NAME, "shopping_cart_link"
        )
        cart.click()

        # verificamos que el producto aparezca en el carrito
        cart_product = driver.find_element(
            By.CLASS_NAME, "inventory_item_name"
        )

        assert cart_product.text == name_product

    finally:
        driver.quit()
