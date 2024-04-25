from behave import *
from selenium import webdriver
from BDD_POM.Steps.loginPage import Login


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
    context.login.set_username("Shakil")
    context.login.set_user_email("shakil@mail.com")


@when("user click login button")
def click_login_button(context):
    context.login.click_login_button()

