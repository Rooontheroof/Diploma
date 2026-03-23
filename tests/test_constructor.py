from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from helpers import BASE_URL
from locators.locators import MainPageLocators


def test_navigate_to_buns(driver):
    wait = WebDriverWait(driver, 5)

    driver.get(BASE_URL)

    heading = wait.until(
        EC.visibility_of_element_located(MainPageLocators.BUNS_HEADING)
    )

    assert heading.is_displayed()