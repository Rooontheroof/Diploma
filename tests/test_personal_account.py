from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from helpers import BASE_URL, LOGIN_URL, REGISTER_URL, generate_email, generate_password
from locators.locators import MainPageLocators, LoginPageLocators, RegisterPageLocators, ProfilePageLocators


def register_and_login(driver):
    wait = WebDriverWait(driver, 7)

    email = generate_email()
    password = generate_password()

    driver.get(REGISTER_URL)

    wait.until(EC.visibility_of_element_located(RegisterPageLocators.NAME_INPUT)).send_keys("Test User")
    driver.find_element(*RegisterPageLocators.EMAIL_INPUT).send_keys(email)
    driver.find_element(*RegisterPageLocators.PASSWORD_INPUT).send_keys(password)
    driver.find_element(*RegisterPageLocators.REGISTER_BUTTON).click()

    wait.until(EC.url_to_be(LOGIN_URL))

    wait.until(EC.visibility_of_element_located(LoginPageLocators.EMAIL_INPUT)).send_keys(email)
    driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(password)
    driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

    wait.until(EC.visibility_of_element_located(MainPageLocators.PERSONAL_ACCOUNT_LINK))


class TestPersonalAccount:

    def test_navigate_to_profile(self, driver):
        wait = WebDriverWait(driver, 7)

        register_and_login(driver)

        current_url = driver.current_url

        wait.until(EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_LINK)).click()
        wait.until(EC.url_changes(current_url))

        assert "/account" in driver.current_url

    def test_navigate_to_constructor_via_link(self, driver):
        wait = WebDriverWait(driver, 7)

        register_and_login(driver)

        wait.until(EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_LINK)).click()
        wait.until(EC.visibility_of_element_located(ProfilePageLocators.LOGOUT_BUTTON))

        current_url = driver.current_url

        wait.until(EC.element_to_be_clickable(MainPageLocators.CONSTRUCTOR_LINK)).click()
        wait.until(EC.url_changes(current_url))

        assert driver.current_url == BASE_URL + "/"

    def test_navigate_to_constructor_via_logo(self, driver):
        wait = WebDriverWait(driver, 7)

        register_and_login(driver)

        wait.until(EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_LINK)).click()
        wait.until(EC.visibility_of_element_located(ProfilePageLocators.LOGOUT_BUTTON))

        current_url = driver.current_url

        wait.until(EC.element_to_be_clickable(MainPageLocators.LOGO)).click()
        wait.until(EC.url_changes(current_url))

        assert driver.current_url == BASE_URL + "/"

    def test_logout(self, driver):
        wait = WebDriverWait(driver, 7)

        register_and_login(driver)

        wait.until(EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_LINK)).click()
        wait.until(EC.visibility_of_element_located(ProfilePageLocators.LOGOUT_BUTTON))

        current_url = driver.current_url

        wait.until(EC.element_to_be_clickable(ProfilePageLocators.LOGOUT_BUTTON)).click()
        wait.until(EC.url_changes(current_url))

        assert "/login" in driver.current_url