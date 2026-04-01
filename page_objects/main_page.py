import time

from selenium.webdriver.support import expected_conditions as EC
from locators.locators import MainPageLocators, ModalLocators
from page_objects.base_page import BasePage


class MainPage(BasePage):
    URL = 'https://stellarburgers.education-services.ru'

    def open(self):
        super().open(self.URL)
        self._wait.until(EC.invisibility_of_element_located(ModalLocators.LOADING_MODAL_OPENED))
        # для Firefox
        time.sleep(0.5)

    def click_constructor(self):
        self._wait.until(EC.presence_of_element_located(MainPageLocators.CONSTRUCTOR_LINK)).click()

    def click_feed(self):
        self._wait.until(EC.element_to_be_clickable(MainPageLocators.FEED_LINK)).click()

    def click_first_ingredient(self):
        self._wait.until(EC.element_to_be_clickable(MainPageLocators.INGREDIENT_CARD)).click()

    def is_modal_open(self):
        try:
            self._wait.until(EC.visibility_of_element_located(ModalLocators.MODAL_OPENED))
            return True
        except:
            return False

    def close_modal(self):
        self._wait.until(EC.element_to_be_clickable(ModalLocators.MODAL_CLOSE)).click()

    def is_modal_closed(self):
        try:
            self._wait.until(EC.invisibility_of_element_located(ModalLocators.MODAL_OPENED))
            return True
        except:
            return False
