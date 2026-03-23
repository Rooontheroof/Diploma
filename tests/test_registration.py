from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from helpers import REGISTER_URL, LOGIN_URL, generate_email, generate_password
from locators.locators import RegisterPageLocators


class TestRegistration:

    def test_successful_registration(self, driver):
        wait = WebDriverWait(driver, 5)

        driver.get(REGISTER_URL)

        email = generate_email()
        password = generate_password()

        wait.until(EC.element_to_be_clickable(RegisterPageLocators.NAME_INPUT)).send_keys("Test User")
        driver.find_element(*RegisterPageLocators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*RegisterPageLocators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*RegisterPageLocators.REGISTER_BUTTON).click()

        wait.until(EC.url_to_be(LOGIN_URL))
        assert driver.current_url == LOGIN_URL

    def test_registration_with_invalid_password(self, driver):
        wait = WebDriverWait(driver, 5)

        driver.get(REGISTER_URL)

        wait.until(EC.element_to_be_clickable(RegisterPageLocators.NAME_INPUT)).send_keys("Test User")
        driver.find_element(*RegisterPageLocators.EMAIL_INPUT).send_keys(generate_email())
        driver.find_element(*RegisterPageLocators.PASSWORD_INPUT).send_keys("123")
        driver.find_element(*RegisterPageLocators.REGISTER_BUTTON).click()

        error = wait.until(
            EC.visibility_of_element_located(RegisterPageLocators.PASSWORD_ERROR)
        )

        assert error.is_displayed()