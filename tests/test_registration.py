from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from helpers import REGISTER_URL, LOGIN_URL, generate_email, generate_password


class TestRegistration:

    def test_successful_registration(self, driver):
        wait = WebDriverWait(driver, 5)

        driver.get(REGISTER_URL)

        email = generate_email()
        password = generate_password()

        wait.until(EC.element_to_be_clickable((By.XPATH, "//fieldset[1]//input"))).send_keys("Test User")
        driver.find_element(By.XPATH, "//fieldset[2]//input").send_keys(email)
        driver.find_element(By.XPATH, "//fieldset[3]//input").send_keys(password)
        driver.find_element(By.XPATH, "//button[text()='Зарегистрироваться']").click()

        wait.until(EC.url_to_be(LOGIN_URL))
        assert driver.current_url == LOGIN_URL

    def test_registration_with_invalid_password(self, driver):
        wait = WebDriverWait(driver, 5)

        driver.get(REGISTER_URL)

        wait.until(EC.element_to_be_clickable((By.XPATH, "//fieldset[1]//input"))).send_keys("Test User")
        driver.find_element(By.XPATH, "//fieldset[2]//input").send_keys(generate_email())
        driver.find_element(By.XPATH, "//fieldset[3]//input").send_keys("123")
        driver.find_element(By.XPATH, "//button[text()='Зарегистрироваться']").click()

        error = wait.until(
            EC.visibility_of_element_located((By.XPATH, "//p[text()='Некорректный пароль']"))
        )

        assert error.is_displayed()