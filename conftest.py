import os
from webbrowser import Chrome

import pytest
# from playsound import playsound
from selenium import webdriver
from pages.login_page import LoginPage
import chromedriver_autoinstaller
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="session")
def browser(request):
    chromedriver_autoinstaller.install()

    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--log-level=3')
    chrome_options.add_argument('--window-size=1920,1080')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--remote-debugging-port=9222')
    chrome_options.add_argument('--enable-javascript')
    chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.add_argument('--allow-insecure-localhost')

    if request.config.getoption("--headed"):
        chrome_options.add_argument('--disable-extensions')
    else:
        chrome_options.add_argument('--headless')

    driver = Chrome(options=chrome_options)
    driver.maximize_window()

    take_screenshot_on_failure = False
    screenshot_dir = ""
    screenshot_num = 0

    def finalize():
        nonlocal take_screenshot_on_failure
        nonlocal screenshot_dir
        nonlocal screenshot_num
        if take_screenshot_on_failure:
            if not os.path.exists(screenshot_dir):
                os.makedirs(screenshot_dir)
            for filename in os.listdir(screenshot_dir):
                if filename.startswith("screenshot_") and filename.endswith(".png"):
                    os.remove(os.path.join(screenshot_dir, filename))
            while os.path.exists(os.path.join(screenshot_dir, f"screenshot_{screenshot_num}.png")):
                screenshot_num += 1
            screenshot_name = f"screenshot_{screenshot_num}.png"
            driver.save_screenshot(os.path.join(screenshot_dir, screenshot_name))
        driver.quit()

    request.addfinalizer(finalize)
    yield driver


def pytest_exception_interact(node, call, report):
    global take_screenshot_on_failure
    if report.failed:
        take_screenshot_on_failure = True
    return None


def pytest_addoption(parser):
    parser.addoption("--headed", action="store_true", help="Run tests in headed mode")


# @pytest.fixture(autouse=True)
# def browser():
#     service = Service(r"C:\Drivers\chromedriver.exe")
#
#     browser = webdriver.Chrome(service=service)
#     browser.maximize_window()
#     yield browser
#     browser.quit()


# pip install chromedriver-autoinstaller
# @pytest.fixture(autouse=True)
# def browser():
#     chromedriver_autoinstaller.install()
#     browser = webdriver.Chrome()
#     browser.maximize_window()
#     yield browser
#     browser.quit()



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
