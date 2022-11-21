from selenium.webdriver.common.keys import Keys
from .locators import MainPageLocators
from .base_page import BasePage


class MainPage(BasePage):
    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()

    def go_to_filter_by_type(self):
        filter_by_type = self.browser.find_element(*MainPageLocators.FILTER_BY_TYPE)
        filter_by_type.click()

    def go_to_filter_by_dog(self):
        filter_by_dog = self.browser.find_element(*MainPageLocators.FILTER_BY_DOG)
        filter_by_dog.click()

    def go_to_filter_by_pet_name(self):
        filter_by_pet_name = self.browser.find_element(*MainPageLocators.FILTER_BY_PET_NAME)
        filter_by_pet_name.send_keys('Kitty one')
        filter_by_pet_name.send_keys(Keys.RETURN)

    def go_to_next_page(self):
        next_page = self.browser.find_element(*MainPageLocators.NEXT_PAGE)
        next_page.click()

    def go_to_last_page(self):
        last_page = self.browser.find_element(*MainPageLocators.LAST_PAGE)
        last_page.click()

    def go_to_pet_details(self):
        pet_details = self.browser.find_element(*MainPageLocators.PET_DETAILS)
        pet_details.click()

    def go_to_profile_page(self):
        profile_link = self.browser.find_element(*MainPageLocators.PROFILE_LINK)
        profile_link.click()
