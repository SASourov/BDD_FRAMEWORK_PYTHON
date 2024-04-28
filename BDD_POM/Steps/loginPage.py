from selenium.webdriver.common.by import By


class Login:
    def __init__(self, driver):
        self.driver = driver

        self.login_menu = (By.XPATH, "//a[@href='/login']")
        self.user_name = (By.NAME, "name")
        self.user_email = (By.XPATH, "(//input[@name='email'])[2]")
        self.login_button = (By.XPATH, "//button[normalize-space()='Signup']")
        #self.success_message = (By.XPATH, "//h2[@class='title text-center']//b")

    def click_login_menu(self):
        self.driver.find_element(*self.login_menu).click()

    def set_username(self, username):
        self.driver.find_element(*self.user_name).send_keys(username)

    def set_user_email(self, email):
        self.driver.find_element(*self.user_email).send_keys(email)

    def click_login_button(self):
        self.driver.find_element(*self.login_button).click()

    def get_success_message(self):
        self.driver.find_element(*self.success_message).text