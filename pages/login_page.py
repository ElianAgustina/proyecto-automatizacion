from selenium.webdriver.common.by import By

class LoginPage:
    # self es una referencia al objeto actual de la clase, y se utiliza para acceder a los atributos y métodos de la clase
    def __init__(self, driver):
        #driver es el objeto que representa el navegador y se pasa como parámetro al constructor de la clase
        self.driver = driver

    # definir las acciones que se pueden realizar en la página de inicio
    def enter_username(self, username):
        self.driver.find_element(By.ID, "user-name").send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(By.ID, "password").send_keys(password)

    def click_login_button(self):
        self.driver.find_element(By.ID, "login-button").click()

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()
