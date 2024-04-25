from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By


@given('user open web site')
def open_web_site(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.implicitly_wait(10)
    context.driver.get("https://automationexercise.com/")


@when('user click login menu')
def click_login_menu(context):
    context.driver.find_element(By.XPATH, "//a[@href='/login']").click()


@when('user entre username and email address')
def set_user_name_password(context):
    user_name = context.driver.find_element(By.NAME, "name")
    user_name.send_keys("Shakil")

    email = context.driver.find_element(By.XPATH, "(//input[@name='email'])[2]")
    email.send_keys("shakil@mail.com")


@when("user click login button")
def click_login_button(context):
    context.driver.find_element(By.XPATH, "//button[normalize-space()='Signup']").click()


@then("user get success message")
def success_message(context):
    success_message = context.driver.find_element(By.XPATH, "//h2[@class='title text-center']//b").text

    if success_message == "ENTER ACCOUNT INFORMATION":
        assert True
    else:
        assert False

    print("Login Success")
    context.driver.quit()
