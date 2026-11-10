import pytest
from selenium import webdriver

# esto es un fixture de pytest que se encarga de crear y cerrar el navegador antes y después de cada prueba
@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    yield driver # el yield permite que la prueba se ejecute y luego se cierre el navegador
    driver.quit()