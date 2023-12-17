from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def click(xpath_value, driver):
    xpath = (By.XPATH, xpath_value)
    wait = WebDriverWait(driver, 10)
    for condition in [
        EC.presence_of_element_located,
        EC.visibility_of_element_located,
        EC.element_to_be_clickable,
    ]:
        wait.until(condition(xpath))
    element = driver.find_element(*xpath)
    element.click()


class TestLesson3:
    def test_selenium_second(self, driver):
        wait = WebDriverWait(driver, 10)

        driver.get("https://www.ebay.com/")

        our_first_element = driver.find_element(By.XPATH, "//*[@id='gh-ac']")
        our_first_element.send_keys("python")

        find_button = driver.find_element(By.XPATH, "//*[@id='gh-btn']")
        find_button.click()

        click("//*[contains(@class, 'heartIcon')]", driver)
        ...
