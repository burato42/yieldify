from time import sleep
from selenium.webdriver.common.by import By
from browser import Browser

from selenium.common.exceptions import NoSuchElementException


class MainPageLocator(object):

    TAKE_NOTE = (By.XPATH, '//div[contains(text(), "Take a note")]/following-sibling::div')
    TITLE = (By.XPATH, '//div[contains(text(), "Title")]/following-sibling::div')
    DONE = (By.XPATH, '//div[contains(text(), "Done")]')
    OPEN_NOTE_TITLE = (By.CSS_SELECTOR, 'div[dir="ltr"][contenteditable="true"]')

    NOTE = (By.CSS_SELECTOR, 'div[dir="ltr"][contenteditable="false"]')
    ARCHIVE = (By.CSS_SELECTOR, 'div[role="toolbar"]>div[aria-label="Archive"]')
    MORE = (By.CSS_SELECTOR, 'div[role="toolbar"]>div[aria-label="More"]')
    DELETE_NOTE = (By.ID, ':2')


class MainPage(Browser):

    def click_element(self, *locator):
        self.driver.find_element(*locator).click()

    def fill(self, text, *locator):
        self.driver.find_element(*locator).send_keys(text)

    def is_present(self, *locator):
        try:
            self.driver.find_element(*locator)
            return True
        except NoSuchElementException:
            return False

    def get_element_text(self, *locator):
        return self.driver.find_element(*locator).text

    def get_element(self, *locator):
        return self.driver.find_element(*locator)

    def get_elements(self, *locator):
        return self.driver.find_elements(*locator)

    def click_last_note(self, *locator):
        try:
            self.driver.find_elements(*locator)[-1].click()
        except IndexError:
            raise NoSuchElementException('There is not any note on the page')

    def archive_notes(self):
        try:
            for _ in self.get_elements(*MainPageLocator.NOTE):
                for x in self.get_elements(*MainPageLocator.ARCHIVE):
                    # TODO Antipattern: need to change to explicit wait
                    sleep(1)
                    if x.is_enabled():
                        if x.is_displayed():
                            x.click()
        except:
            pass

    def press_more(self):
        try:
            for x in self.get_elements(*MainPageLocator.MORE):
                # TODO Antipattern: need to change to explicit wait
                sleep(1)
                if x.is_enabled():
                    if x.is_displayed():
                        x.click()
        except:
            pass
