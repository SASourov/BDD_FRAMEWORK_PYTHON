from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class AccountInfo:
    def __init__(self, driver):
        self.driver = driver

        self.select_gender = (By.ID, "id_gender1")
        self.enter_password = (By.ID, "password")
        self.birth_of_date = (By.ID, "days")
        self.birth_of_month = (By.ID, "months")
        self.birth_of_year = (By.ID, "years")
        self.select_an_option = (By.ID, "optin")
        self.enter_first_name = (By.ID, "first_name")
        self.enter_last_name = (By.ID, "last_name")
        self.enter_address = (By.ID, "address1")
        self.select_country = (By.ID, "country")
        self.enter_state = (By.ID, "state")
        self.enter_city = (By.ID, "city")
        self.enter_zipcode = (By.ID, "zipcode")
        self.enter_mobile = (By.ID, "mobile_number")
        self.create_account = (By.XPATH, "//button[@class='btn btn-default']")

    def click_select_gender(self):
        self.driver.find_element(*self.select_gender).click()

    def set_password(self, password):
        self.driver.find_element(*self.enter_password).send_keys("Shakil@12")

    def click_on_birth_date(self):
        self.driver.find_element(*self.birth_of_date).click()
        self.driver.find_element(*self.birth_of_date).send_keys("15")
        self.driver.find_element(*self.birth_of_date).send_keys(Keys.ENTER)

    def click_on_birth_month(self):
        self.driver.find_element(*self.birth_of_month).click()
        self.driver.find_element(*self.birth_of_month).send_keys("April")
        self.driver.find_element(*self.birth_of_month).send_keys(Keys.ENTER)

    def click_on_birth_year(self):
        self.driver.find_element(*self.birth_of_year).click()
        self.driver.find_element(*self.birth_of_year).send_keys("1996")
        self.driver.find_element(*self.birth_of_year).send_keys(Keys.ENTER)

    def select_option(self):
        self.driver.find_element(*self.select_an_option).click()

    def set_first_name(self, f_name):
        self.driver.find_element(*self.enter_first_name).send_keys(f_name)

    def set_last_name(self, l_name):
        self.driver.find_element(*self.enter_last_name).send_keys(l_name)

    def set_address(self, address):
        self.driver.find_element(*self.enter_address).send_keys(address)

    def set_country(self):
        self.driver.find_element(*self.select_country).click()
        self.driver.find_element(*self.select_country).send_keys("C")
        self.driver.find_element(*self.select_country).send_keys(Keys.ENTER)

    def set_state(self, state):
        self.driver.find_element(*self.enter_state).send_keys(state)

    def set_city(self, city):
        self.driver.find_element(*self.enter_city).send_keys(city)

    def set_zip(self, zip):
        self.driver.find_element(*self.enter_zipcode).send_keys(zip)

    def set_mobile_num(self, mobile):
        self.driver.find_element(*self.enter_mobile).send_keys(mobile)

    def click_on_create_button(self):
        self.driver.find_element(*self.create_account).click()


