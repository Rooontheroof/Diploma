from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from helpers import BASE_URL, LOGIN_URL, REGISTER_URL, FORGOT_PASSWORD_URL, generate_email, generate_password
from locators.locators import MainPageLocators, LoginPageLocators, RegisterPageLocators, ForgotPasswordPageLocators


def register_and_get_credentials(driver):
    wait = WebDriverWait(driver, 5)

    driver.get(REGISTER_URL)

    email = generate_email()
    password = generate_password()

    wait.until(EC.element_to_be_clickable(RegisterPageLocators.NAME_INPUT)).send_keys("Test User")
    driver.find_element(*RegisterPageLocators.EMAIL_INPUT).send_keys(email)
    driver.find_element(*RegisterPageLocators.PASSWORD_INPUT).send_keys(password)
    driver.find_element(*RegisterPageLocators.REGISTER_BUTTON).click()

    wait.until(EC.url_to_be(LOGIN_URL))

    return email, password


class TestLogin:

    def test_login_via_main_button(self, driver):
        wait = WebDriverWait(driver, 5)

        email, password = register_and_get_credentials(driver)

        driver.get(BASE_URL)

        wait.until(EC.element_to_be_clickable(MainPageLocators.LOGIN_BUTTON)).click()

        wait.until(EC.visibility_of_element_located(LoginPageLocators.EMAIL_INPUT)).send_keys(email)
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

        wait.until(EC.url_to_be(BASE_URL + "/"))
        assert driver.current_url == BASE_URL + "/"

    def test_login_via_personal_account_link(self, driver):
        wait = WebDriverWait(driver, 5)

        email, password = register_and_get_credentials(driver)

        driver.get(BASE_URL)

        wait.until(EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_LINK)).click()
        wait.until(EC.url_to_be(LOGIN_URL))

        wait.until(EC.visibility_of_element_located(LoginPageLocators.EMAIL_INPUT)).send_keys(email)
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

        wait.until(EC.url_to_be(BASE_URL + "/"))
        assert driver.current_url == BASE_URL + "/"

    def test_login_via_register_page_link(self, driver):
        wait = WebDriverWait(driver, 5)

        email, password = register_and_get_credentials(driver)

        driver.get(REGISTER_URL)

        wait.until(EC.element_to_be_clickable(RegisterPageLocators.LOGIN_LINK)).click()
        wait.until(EC.url_to_be(LOGIN_URL))

        wait.until(EC.visibility_of_element_located(LoginPageLocators.EMAIL_INPUT)).send_keys(email)
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

        wait.until(EC.url_to_be(BASE_URL + "/"))
        assert driver.current_url == BASE_URL + "/"

    def test_login_via_forgot_password_link(self, driver):
        wait = WebDriverWait(driver, 5)

        email, password = register_and_get_credentials(driver)

        driver.get(FORGOT_PASSWORD_URL)

        wait.until(EC.element_to_be_clickable(ForgotPasswordPageLocators.LOGIN_LINK)).click()
        wait.until(EC.url_to_be(LOGIN_URL))

        wait.until(EC.visibility_of_element_located(LoginPageLocators.EMAIL_INPUT)).send_keys(email)
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

        wait.until(EC.url_to_be(BASE_URL + "/"))
        assert driver.current_url == BASE_URL + "/"