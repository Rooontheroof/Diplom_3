import allure
from selenium.webdriver.support import expected_conditions as EC

from constants import LOGIN_URL, EMAIL, PASSWORD, MAIN_URL
from locators.login_page import LoginPageLocators
from locators.main_page import MainPageLocators
from page_objects.base_page import BasePage


class LoginPage(BasePage):
    @allure.step("Логинимся на сайт")
    def login(self):
        self._open()
        self._login(EMAIL, PASSWORD)
        self._wait_for_main_page()

    def _open(self):
        self.open_page(LOGIN_URL)
        self.wait_until_modal_invisible()

    def _login(self, email, password):
        self.wait_until_modal_invisible()
        self.wait_until_locator_visible(LoginPageLocators.EMAIL_INPUT).send_keys(email)
        self.wait_until_locator_visible(LoginPageLocators.PASSWORD_INPUT).send_keys(password)
        self.click(LoginPageLocators.LOGIN_BUTTON)

    def _wait_for_main_page(self):
        """Ждёт редиректа на главную страницу после логина."""
        self._wait.until(EC.url_to_be(MAIN_URL))
        # Дополнительно ждём появления ингредиентов
        self.wait_until_present(MainPageLocators.INGREDIENT_CARD)
        # ждем, когда пропадет лоадер
        self.wait_until_modal_invisible()
