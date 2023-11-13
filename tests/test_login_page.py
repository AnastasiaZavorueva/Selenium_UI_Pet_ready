
import time
import os
import pytest
import requests
from selenium.webdriver.common.by import By

from pages.locators import LoginPageLocators
from pages.login_page import LoginPage
import allure
from allure_commons.types import AttachmentType




@allure.feature('user_login')
@allure.story('Вводим валидный email и пароль')
@allure.severity('blocker')

def test_go_to_login(browser):
    link = 'http://34.141.58.52:8080/#/login'

    page = LoginPage(browser, link)
    page.open()
    page.go_to_login()
    page.go_to_password()
    page.go_to_login_button()
    time.sleep(3)
    with allure.step('Делаем скриншот'):
        allure.attach(browser.get_screenshot_as_png(), name='result8', attachment_type=AttachmentType.PNG)
    # browser.save_screenshot('result.png')
    profile = page.find_profile()
    assert profile



@pytest.mark.parametrize("email", ['zavan@mail.ru', 'zavan@mail2.ru'])
def test_login(browser, email):
    link = 'http://34.141.58.52:8080/#/login'
    browser.get(link)
    login_email = browser.find_element(*LoginPageLocators.LOGIN_EMAIL)
    login_email.send_keys(email)
    time.sleep(1)
    page = LoginPage(browser, link)
    page.go_to_password()
    page.go_to_login_button()
    response = requests.get('http://34.141.58.52:8080/#/profile')
    assert response.status_code == 200

# # Определение тестовых данных
# test_data = [("user1", "pass1"), ("user2", "pass2"), ("user3", "pass3")]
#
# # Использование параметризации для передачи тестовых данных
# @pytest.mark.parametrize("username, password", test_data)
# def test_login(username, password):
#     # Вызов функции логина и проверка результата
#     assert login(username, password) == "success"