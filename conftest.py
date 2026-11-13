import pytest
from selenium import webdriver

# esto es un fixture de pytest que se encarga de crear y cerrar el navegador antes y después de cada prueba
@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    yield driver # el yield permite que la prueba se ejecute y luego se cierre el navegador
    driver.quit()

@pytest.fixture
def base_url():
    return "https://reqres.in/api"

@pytest.fixture
def headers():
    return {
        "x-api-key": "pub_5bca5ffc8772df976fcf8970168a1ad219ad499c472afbba2f27085fa4b4ef7d"
    }

