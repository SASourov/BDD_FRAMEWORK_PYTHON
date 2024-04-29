import time

from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By

from BDD_POM.Steps.loginPage import Login
from BDD_POM.Steps.accountInfoPage import AccountInfo
import random

random_num = random.randint(0, 999)


@given('user open web site')
def open_site(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.implicitly_wait(10)
    context.driver.get("https://automationexercise.com/")


@when("user click login menu")
def click_login_menu(context):
    context.login = Login(context.driver)
    context.login.click_login_menu()


@when("user entre username and email address")
def set_username_and_email(context):
    context.login.set_username("Test")
    context.login.set_user_email("test@" + str(random_num) + "mail.com")


@when("user click login button")
def click_login_button(context):
    context.login.click_login_button()


@then("success message")
def get_success_message(context):
    message = context.driver.find_element(By.XPATH, "//h2[@class='title text-center']//b").text

    if message == "ENTER ACCOUNT INFORMATION":
        assert True

    else:
        assert False


@when('user select gender')
def select_gender(context):
    context.ac_info = AccountInfo(context.driver)
    context.ac_info.click_select_gender()
    time.sleep(2)


@when('user set password')
def user_set_password(context):
    context.ac_info.set_password('Test@12')
    time.sleep(2)


@when('user set birth info')
def user_set_birth_info(context):
    context.ac_info.click_on_birth_date()
    time.sleep(2)
    context.ac_info.click_on_birth_month()
    time.sleep(2)
    context.ac_info.click_on_birth_year()
    time.sleep(2)


@when('user select an option')
def user_select_an_option(context):
    context.ac_info.select_option()
    time.sleep(2)


@when('user set name info')
def user_set_name_info(context):
    context.ac_info.set_first_name("Abul")
    context.ac_info.set_last_name("Kalam")
    time.sleep(2)


@when('user set address info')
def user_set_address_info(context):
    context.ac_info.set_address("Banani Dhaka")
    time.sleep(2)
    context.ac_info.set_country()
    time.sleep(2)
    context.ac_info.set_state("Capital")
    time.sleep(2)
    context.ac_info.set_city("City")
    time.sleep(2)
    context.ac_info.set_zip("1230")
    time.sleep(2)
    context.ac_info.set_mobile_num("01722000000")


@when('user click button')
def user_click_button(context):
    context.ac_info.click_on_create_button()
    context.driver.quit()
