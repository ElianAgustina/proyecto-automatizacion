from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from pages.login_page import LoginPage
from utils.reader import read_users_csv


@pytest.mark.parametrize(
    "data",read_users_csv()
    )
def test_login(driver, data):
    username = data["username"]
    password = data["password"]


    # Crear una instancia de la página de inicio de sesión
    login_page = LoginPage(driver)
   
    # Abrir la página de inicio de sesión
    driver.get("https://www.saucedemo.com/")
   
    # Llamar al método de inicio de sesión con las credenciales correctas
    login_page.login(username, password)
   
    if data["type_username"] == "user_ok":
        # Validar que el inicio de sesión fue exitoso
        assert "/inventory.html" in driver.current_url
       
        # Validar logo
        logo = driver.find_element(By.CLASS_NAME, "app_logo")
        assert logo.text == "Swag Labs"
   
        # Validar titulo
        title = driver.find_element(By.CSS_SELECTOR, "[data-test='title']")
        assert title.text == "Products"
   
    elif data["type_username"] == "user_error":
        # Validar que el inicio de sesión falló y se muestra un mensaje de error
        error_message = login_page.get_error_message()
        assert "Epic sadface" in error_message
