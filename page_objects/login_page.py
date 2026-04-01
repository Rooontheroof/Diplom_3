import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from locators.locators import LoginPageLocators, ModalLocators
from page_objects.base_page import BasePage


class LoginPage(BasePage):
    URL = 'https://stellarburgers.education-services.ru/login'

    def open(self):
        super().open(self.URL)

    def login(self, email, password):
        self._wait.until(EC.invisibility_of_element_located(ModalLocators.LOADING_MODAL_OPENED))
        self._wait.until(EC.visibility_of_element_located(LoginPageLocators.EMAIL_INPUT)).send_keys(email)
        self._wait.until(EC.visibility_of_element_located(LoginPageLocators.PASSWORD_INPUT)).send_keys(password)
        button = self._wait.until(EC.element_to_be_clickable(LoginPageLocators.LOGIN_BUTTON))
        # Ждем окончания анимации
        time.sleep(0.5)
        button.click()

    def wait_for_main_page(self):
        """Ждёт редиректа на главную страницу после логина."""
        self._wait.until(EC.url_to_be('https://stellarburgers.education-services.ru/'))
        # Дополнительно ждём появления ингредиентов
        self._wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "a.BurgerIngredient_ingredient__1TVf6")
        ))
