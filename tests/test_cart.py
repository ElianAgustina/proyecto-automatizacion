from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



def test_cart():
    driver = webdriver.Chrome()
     
    # Espera explícita de 10 segundos
    wait = WebDriverWait(driver, 10)  
   
    try:
        # Abrir la página de inicio de sesión
        driver.get("https://www.saucedemo.com/")


        # Encontrar los elementos
        wait.until(EC.visibility_of_element_located((By.ID, "user-name"))).send_keys("standard_user")
        password = driver.find_element(By.ID, "password")
        button_login = driver.find_element(By.ID, "login-button")


        # Ingresar credenciales
        password.send_keys("secret_sauce")
        button_login.click()
       
        # obtener el primer producto de la lista para agregarlo al carrito y validar que se agrego correctamente
        first_product = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "inventory_item")))
       
        # obtener el nombre del producto para validar que se agrego correctamente al carrito
        name_product = first_product.find_element(By.CLASS_NAME, "inventory_item_name").text
       
        # obtener el boton de agregar al carrito del primer producto
        button_add = first_product.find_element(By.TAG_NAME, "button")
       
        # hacer click en el boton de agregar al carrito
        button_add.click()
       
        # validar que el contador del carrito se actualizo a 1
        counter_car = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge")))      


        assert counter_car.text == "1"
       
        # hacer click en el carrito para validar que el producto se agrego correctamente
        wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link"))).click()
       
        # validar que el producto agregado al carrito es el mismo que se agrego
        product_car = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "inventory_item_name"))).text
        assert product_car == name_product


    finally:
        driver.quit()