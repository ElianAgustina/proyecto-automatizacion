''' 
el conftest.py es un archivo de configuración de pytest que contiene fixtures y configuraciones globales para las pruebas
que son llamadas automáticamente por pytest antes de ejecutar las pruebas. 
Los fixtures son funciones que se ejecutan antes de cada prueba y proporcionan datos o configuraciones necesarias para la prueba.
'''
import pytest
import pytest_html
from selenium import webdriver
import pathlib

# esto es un fixture de pytest que se encarga de crear y cerrar el navegador antes y después de cada prueba
@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    yield driver # el yield permite que la prueba se ejecute y luego se cierre el navegador
    driver.quit()

@pytest.fixture
# este fixture devuelve la URL base de la API que se va a probar cuando se llame en las pruebas
def base_url():
    return "https://reqres.in/api"

@pytest.fixture
# este fixture devuelve la URL base de la API que se va a probar cuando se llame en las pruebas
def headers():
    return {
        "x-api-key": "pub_5bca5ffc8772df976fcf8970168a1ad219ad499c472afbba2f27085fa4b4ef7d"
    }

# se escribe aqui y es llamada desde el driver
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")
        file = pathlib.Path("reports/screenshots")
        file.mkdir(parents=True, exist_ok=True)
        screenshot_file = file / f"{item.name}.png"
        driver.save_screenshot(str(screenshot_file))