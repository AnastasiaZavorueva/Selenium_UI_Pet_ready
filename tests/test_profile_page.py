import time
import pytest
from pages.profile_page import ProfilePage
from tests.test_login_page import test_go_to_login


# @pytest.mark.skip
def test_go_to_logo_button(browser):
    test_go_to_login(browser)
    link = 'http://34.141.58.52:8080/#/profile'
    page = ProfilePage(browser, link)
    page.open()
    page.go_to_logo_button()
    time.sleep(2)
    browser.save_screenshot('result9.png')


@pytest.mark.smoke
@pytest.mark.regression
def test_go_to_quit_button(browser):
    test_go_to_login(browser)
    link = 'http://34.141.58.52:8080/#/profile'
    page = ProfilePage(browser, link)
    page.open()
    page.go_to_quit_button()
    browser.save_screenshot('result10.png')


@pytest.mark.regression
def test_go_to_edit_pet_profile(browser):
    test_go_to_login(browser)
    link = 'http://34.141.58.52:8080/#/profile'
    page = ProfilePage(browser, link)
    page.open()
    page.go_to_edit_pet_profile()
    browser.save_screenshot('result11.png')


@pytest.mark.smoke
@pytest.mark.regression
def test_go_to_add_pet(browser):
    test_go_to_login(browser)
    link = 'http://34.141.58.52:8080/#/profile'
    page = ProfilePage(browser, link)
    page.open()
    page.go_to_add_pet_button()
    page.go_to_add_pet_name()
    page.go_to_add_pet_age()
    page.go_to_choose_pet_type()
    page.go_to_choose_pet_type_dog()
    page.go_to_choose_pet_gender()
    page.go_to_choose_pet_gender_male()
    page.go_to_submit_add_pet_button()
    time.sleep(2)
    page.go_to_add_photo()
    time.sleep(2)
    page.go_to_submit_add_photo()
    time.sleep(5)
    browser.save_screenshot('result4.png')
