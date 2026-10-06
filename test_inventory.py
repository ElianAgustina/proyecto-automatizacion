from selenium import webdriver
from selenium.webdriver.common.by import By


def test_inventory():
    driver = webdriver.Chrome()
    
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
        
        #Verificar titulo de la pagina
        assert driver.title == "Swag Labs"
        
        products = driver.find_elements(By.CLASS_NAME,"inventory_item")
        assert len(products) > 0
        
        first_product = products[0]
        name_product = first_product.find_element(By.CLASS_NAME,"inventory_item_name").text
        
        price_product = first_product.find_element(By.CLASS_NAME,"inventory_item_price").text
        
        assert name_product == "Sauce Labs Backpack"
        assert price_product == "$29.99"
        
        #verificar menu
        menu = driver.find_element(By.ID,"react-burger-menu-btn")
        
        assert menu.is_displayed()
        
        #Verificar filtro
        filter = driver.find_element(By.CLASS_NAME,"product_sort_container")
        
        assert filter.is_displayed
    finally:
        driver.quit()
    