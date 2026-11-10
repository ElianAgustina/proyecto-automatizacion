from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.login_page import LoginPage

def test_login_success(driver):
    login_page = LoginPage(driver) # Crear una instancia de la página de inicio de sesión

    # Abrir la página de inicio de sesión
    driver.get("https://www.saucedemo.com/")
    # Llamar al método de inicio de sesión con las credenciales correctas
    login_page.login("standard_user", "secret_sauce") 
    # Validar URL
    assert "/inventory.html" in driver.current_url
    # Validar logo
    logo = driver.find_element(By.CLASS_NAME, "app_logo")
    assert logo.text == "Swag Labs"
    # Validar título
    title = driver.find_element(By.CSS_SELECTOR, "[data-test='title']")
    assert title.text == "Products"
