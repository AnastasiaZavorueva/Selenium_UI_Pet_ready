import pytest
from playsound import playsound
from selenium import webdriver
from pages.login_page import LoginPage
import chromedriver_autoinstaller





# @pytest.fixture(autouse=True)
# def browser():
#     service = Service(r"C:\Drivers\chromedriver.exe")
#
#     browser = webdriver.Chrome(service=service)
#     browser.maximize_window()
#     yield browser
#     browser.quit()


# pip install chromedriver-autoinstaller
@pytest.fixture(autouse=True)
def browser():
    chromedriver_autoinstaller.install()
    browser = webdriver.Chrome()
    browser.maximize_window()
    yield browser
    browser.quit()



@pytest.fixture()
def go_to_login(browser):
    link = 'http://34.141.58.52:8080/#/login'

    page = LoginPage(browser, link)
    page.open()
    page.go_to_login()
    page.go_to_password()
    page.go_to_login_button()



#
# @pytest.fixture(autouse=True)
# def play_music():
#     playsound(r'2_5222034019746589188.mp3', True)





@pytest.fixture()
def cookies(browser):
    # service = Service("C:\Drivers\chromedriver.exe")
    # browser = webdriver.Chrome(service=service)
    get_cookie = browser.get_cookie()
    print(get_cookie)
