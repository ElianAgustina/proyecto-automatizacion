from selenium import webdriver
from selenium.webdriver.common.by import By

def test_login_success():
    try:
        # Se abre el navegador
        driver = webdriver.Chrome()

        # Abrir la página de inicio de sesión
        driver.get("https://www.saucedemo.com/")

        # Encontrar los elementos
        user = driver.find_element(By.ID, "user-name")
        password = driver.find_element(By.ID, "password")
        button_login = driver.find_element(By.ID, "login-button")

        # Ingresar credenciales
        user.send_keys("standard_user")
        password.send_keys("secret_sauce")
        button_login.click()

        # Validar URL
        assert "https://www.saucedemo.com/inventory.html" in driver.current_url

        # Validar logo
        logo = driver.find_element(By.CLASS_NAME, "app_logo")
        assert logo.text == "Swag Labs"

        # Validar título
        title = driver.find_element(By.CSS_SELECTOR, "[data-test='title']")
        assert title.text == "Products"

    finally:
        driver.quit()