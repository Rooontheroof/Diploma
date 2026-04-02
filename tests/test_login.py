from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from helpers import BASE_URL, LOGIN_URL, REGISTER_URL, FORGOT_PASSWORD_URL, generate_email, generate_password


def register_and_get_credentials(driver):
    wait = WebDriverWait(driver, 5)

    driver.get(REGISTER_URL)

    email = generate_email()
    password = generate_password()

    wait.until(EC.element_to_be_clickable((By.XPATH, "//fieldset[1]//input"))).send_keys("Test User")
    driver.find_element(By.XPATH, "//fieldset[2]//input").send_keys(email)
    driver.find_element(By.XPATH, "//fieldset[3]//input").send_keys(password)
    driver.find_element(By.XPATH, "//button[text()='Зарегистрироваться']").click()

    wait.until(EC.url_to_be(LOGIN_URL))

    return email, password


class TestLogin:

    def test_login_via_main_button(self, driver):
        wait = WebDriverWait(driver, 5)

        email, password = register_and_get_credentials(driver)

        driver.get(BASE_URL)

        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Войти в аккаунт']"))).click()

        wait.until(EC.visibility_of_element_located((By.XPATH, "//fieldset[1]//input"))).send_keys(email)
        driver.find_element(By.XPATH, "//input[@name='Пароль']").send_keys(password)
        driver.find_element(By.XPATH, "//button[text()='Войти']").click()

        wait.until(EC.url_to_be(BASE_URL + "/"))
        assert driver.current_url == BASE_URL + "/"

    def test_login_via_personal_account_link(self, driver):
        wait = WebDriverWait(driver, 5)

        email, password = register_and_get_credentials(driver)

        driver.get(BASE_URL)

        wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/account']"))).click()
        wait.until(EC.url_to_be(LOGIN_URL))

        wait.until(EC.visibility_of_element_located((By.XPATH, "//fieldset[1]//input"))).send_keys(email)
        driver.find_element(By.XPATH, "//input[@name='Пароль']").send_keys(password)
        driver.find_element(By.XPATH, "//button[text()='Войти']").click()

        wait.until(EC.url_to_be(BASE_URL + "/"))
        assert driver.current_url == BASE_URL + "/"

    def test_login_via_register_page_link(self, driver):
        wait = WebDriverWait(driver, 5)

        email, password = register_and_get_credentials(driver)

        driver.get(REGISTER_URL)

        wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/login']"))).click()
        wait.until(EC.url_to_be(LOGIN_URL))

        wait.until(EC.visibility_of_element_located((By.XPATH, "//fieldset[1]//input"))).send_keys(email)
        driver.find_element(By.XPATH, "//input[@name='Пароль']").send_keys(password)
        driver.find_element(By.XPATH, "//button[text()='Войти']").click()

        wait.until(EC.url_to_be(BASE_URL + "/"))
        assert driver.current_url == BASE_URL + "/"

    def test_login_via_forgot_password_link(self, driver):
        wait = WebDriverWait(driver, 5)

        email, password = register_and_get_credentials(driver)

        driver.get(FORGOT_PASSWORD_URL)

        wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/login']"))).click()
        wait.until(EC.url_to_be(LOGIN_URL))

        wait.until(EC.visibility_of_element_located((By.XPATH, "//fieldset[1]//input"))).send_keys(email)
        driver.find_element(By.XPATH, "//input[@name='Пароль']").send_keys(password)
        driver.find_element(By.XPATH, "//button[text()='Войти']").click()

        wait.until(EC.url_to_be(BASE_URL + "/"))
        assert driver.current_url == BASE_URL + "/"