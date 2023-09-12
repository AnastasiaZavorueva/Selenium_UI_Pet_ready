import pytest
from playsound import playsound

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service




@pytest.fixture(autouse=True)
def browser():
    service = Service(r"C:\Drivers\chromedriver.exe")

    browser = webdriver.Chrome(service=service)
    browser.maximize_window()
    yield browser
    browser.quit()




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
