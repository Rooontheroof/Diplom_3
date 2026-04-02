import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from constants import BASE_URL, LOGIN_URL, EMAIL, PASSWORD, MAIN_URL
from page_objects.base_page import BasePage
from page_objects.main_page import MainPage
from page_objects.modal_locators import ModalLocators


class LoginPage(BasePage):
    EMAIL_INPUT = (By.CSS_SELECTOR, "input[name='name']")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input[name='Пароль']")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")

    @allure.step("Логинимся на сайт")
    def login(self):
        self._open()
        self._login(EMAIL, PASSWORD)
        self._wait_for_main_page()

    def _open(self):
        super().open(LOGIN_URL)
        self._wait.until(EC.invisibility_of_element_located(ModalLocators.LOADING_MODAL_OPENED))

    def _login(self, email, password):
        self._wait.until(EC.invisibility_of_element_located(ModalLocators.LOADING_MODAL_OPENED))
        self._wait.until(EC.visibility_of_element_located(self.EMAIL_INPUT)).send_keys(email)
        self._wait.until(EC.visibility_of_element_located(self.PASSWORD_INPUT)).send_keys(password)
        button = self._wait.until(EC.element_to_be_clickable(self.LOGIN_BUTTON))
        button.click()

    def _wait_for_main_page(self):
        """Ждёт редиректа на главную страницу после логина."""
        self._wait.until(EC.url_to_be(MAIN_URL))
        # Дополнительно ждём появления ингредиентов
        self._wait.until(EC.presence_of_element_located(MainPage.INGREDIENT_CARD))
        # ждем, когда пропадет лоадер
        self._wait.until(EC.invisibility_of_element_located(ModalLocators.LOADING_MODAL_OPENED))
