from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from helpers import BASE_URL, LOGIN_URL, REGISTER_URL, generate_email, generate_password


def register_and_login(driver):
    wait = WebDriverWait(driver, 7)

    email = generate_email()
    password = generate_password()

    driver.get(REGISTER_URL)

    wait.until(EC.visibility_of_element_located((By.XPATH, "//fieldset[1]//input"))).send_keys("Test User")
    driver.find_element(By.XPATH, "//fieldset[2]//input").send_keys(email)
    driver.find_element(By.XPATH, "//fieldset[3]//input").send_keys(password)
    driver.find_element(By.XPATH, "//button[text()='Зарегистрироваться']").click()

    wait.until(EC.url_to_be(LOGIN_URL))

    wait.until(EC.visibility_of_element_located((By.XPATH, "//fieldset[1]//input"))).send_keys(email)
    driver.find_element(By.XPATH, "//input[@name='Пароль']").send_keys(password)
    driver.find_element(By.XPATH, "//button[text()='Войти']").click()

    wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='/account']")))


class TestPersonalAccount:

    def test_navigate_to_profile(self, driver):
        wait = WebDriverWait(driver, 7)

        register_and_login(driver)

        current_url = driver.current_url

        wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/account']"))).click()
        wait.until(EC.url_changes(current_url))

        assert "/account" in driver.current_url

    def test_navigate_to_constructor_via_link(self, driver):
        wait = WebDriverWait(driver, 7)

        register_and_login(driver)

        wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/account']"))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, "//button[text()='Выход']")))

        current_url = driver.current_url

        # иногда перекрывается → скролл
        constructor = wait.until(
            EC.presence_of_element_located((By.XPATH, "//a[@href='/']"))
        )
        driver.execute_script("arguments[0].scrollIntoView();", constructor)

        wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/']"))).click()
        wait.until(EC.url_changes(current_url))

        assert driver.current_url == BASE_URL + "/"

    def test_navigate_to_constructor_via_logo(self, driver):
        wait = WebDriverWait(driver, 7)

        register_and_login(driver)

        wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/account']"))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, "//button[text()='Выход']")))

        current_url = driver.current_url

        logo = wait.until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(@class,'AppHeader_header__logo')]"))
        )
        driver.execute_script("arguments[0].scrollIntoView();", logo)

        wait.until(
            EC.element_to_be_clickable((By.XPATH, "//div[contains(@class,'AppHeader_header__logo')]"))
        ).click()

        wait.until(EC.url_changes(current_url))

        assert driver.current_url == BASE_URL + "/"

    def test_logout(self, driver):
        wait = WebDriverWait(driver, 7)

        register_and_login(driver)

        wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/account']"))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, "//button[text()='Выход']")))

        current_url = driver.current_url

        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Выход']"))).click()
        wait.until(EC.url_changes(current_url))

        assert "/login" in driver.current_url