from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#app > header > div > ul > li:nth-child(1) > a > span')
    FILTER_BY_TYPE = (By.ID, 'typesSelector')
    FILTER_BY_DOG = (By.ID, 'pv_id_2_0')
    FILTER_BY_PET_NAME = (By.ID, 'petName')
    NEXT_PAGE = (By.XPATH, '//*[@id="app"]/main/div/div[2]/div[3]/button[3]')
    LAST_PAGE = (By.XPATH, '//*[@id="app"]/main/div/div[2]/div[3]/button[4]')
    PET_DETAILS = (By.XPATH, '//*[@id="app"]/main/div/div[2]/div[2]/div/div/div/div[3]/div[1]/button')
    PROFILE_LINK = (By.CSS_SELECTOR, '#app > header > div > ul > li:nth-child(1) > a')


class LoginPageLocators:
    LOGIN_EMAIL = (By.ID, "login")
    LOGIN_PASS = (By.CSS_SELECTOR, "#password > input")
    LOGIN_BTN = (By.CLASS_NAME, "p-button-label")
    PROFILE = (By.XPATH, '//*[@id="app"]/header/div')


class ProfilePageLocators:
    LOGO_BTN = (By.CLASS_NAME, 'p-menubar-start')
    QUIT_BTN = (By.CSS_SELECTOR, '#app > header > div > ul > li:nth-child(2) > a')
    EDIT_PET_BTN = (By.XPATH, '//*[@id="app"]/main/div/div/div[2]/div/div[1]/div/div[2]/button[1]')
    ADD_PET_BTN = (By.CSS_SELECTOR, '#app > main > div > div > div.p-dataview-header > div > div:nth-child(1) > button')
    ADD_PET_NAME = (By.ID, 'name')
    ADD_PET_AGE = (By.CSS_SELECTOR, '#age > input')
    CHOOSE_PET_TYPE = (By.CSS_SELECTOR, '#typeSelector')
    CHOOSE_PET_TYPE_DOG = (By.XPATH, '//*[@aria-label="dog"]')
    CHOOSE_PET_GENDER = (By.CSS_SELECTOR, '#genderSelector')
    CHOOSE_PET_GENDER_MALE = (By.XPATH, '//*[@aria-label="Male"]')
    SUBMIT_ADD_PET_BTN = (By.XPATH, '//*[@id="app"]/main/div/div/form/div/div[2]/div[3]/button[1]')
    ADD_PHOTO = (By.XPATH, '//*[@id="app"]/main/div/div/div[2]/div[2]/div/span/input')
    SUBMIT_ADD_PHOTO = (By. XPATH, '//*[@id="app"]/main/div/div/div[2]/div[2]/div/span')
