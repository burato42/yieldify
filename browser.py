from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

EMAIL = 'test.yieldify.task@gmail.com'
PASSWORD = 'testyieldify2013'
URL = 'https://keep.google.com/'


class Locators:
    EMAIL_LOCATOR = (By.ID, 'identifierId')
    EMAIL_NEXT = (By.ID, 'identifierNext')
    PASSWORD_LOCATOR = (By.CSS_SELECTOR, 'input[name="password"]')
    PASSWORD_NEXT = (By.CSS_SELECTOR, '#passwordNext>content')


class Browser:
    timeout = 10
    driver = webdriver.Firefox()
    driver.implicitly_wait(timeout)
    driver.set_page_load_timeout(timeout)
    driver.maximize_window()

    def close(self):
        self.driver.close()

    def wait_for_element_visible(self, locator):
        WebDriverWait(self.driver, self.timeout).until(
            EC.visibility_of_element_located(locator),
            message='Element %s %s either is not present or invisible' % locator)

    def login(self):
        self.driver.get(URL)
        self.driver.find_element(*Locators.EMAIL_LOCATOR).send_keys(EMAIL)
        self.driver.find_element(*Locators.EMAIL_NEXT).click()
        self.wait_for_element_visible(Locators.PASSWORD_LOCATOR)
        self.driver.find_element(*Locators.PASSWORD_LOCATOR).send_keys(PASSWORD)
        password_next = self.driver.find_element(*Locators.PASSWORD_NEXT)
        password_next.click()
