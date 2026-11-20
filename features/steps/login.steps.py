from behave import given,when,then
from pages.login_page import LoginPage

@given("que el usuario se encuentre en la pagina del login")
def step_user_login(context):
    context.login_page = LoginPage(context.driver)
    context.login_page.open_page()

@when('ingresa en los campos de datos "{username}" y "{password}"')
def step_enter_credentials(context,username,password):
    if username == "VACIO":
        username = ""

    if password == "VACIO":
        password = ""

    context.login_page.enter_username(username)
    context.login_page.enter_password(password)

@when("hace click en el boton de login")
def step_click_login(context):
    context.login_page.click_login_button()

@then("deberia ingresar al inventario")
def step_validate_successful_login(context):
    assert "/inventory.html" in context.driver.current_url

@then('deberia mostrase el mensaje de error "{message}"')
def step_validate_error_message(context,message):
    error = context.login_page.get_error_message()
    print(error)
    assert message in error, f"Se esperaba '{message}', pero se obtuvo '{error}'"