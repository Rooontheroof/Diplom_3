import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from constants import BASE_URL
from page_objects.base_page import BasePage
from page_objects.modal_locators import ModalLocators


class MainPage(BasePage):
    CONSTRUCTOR_LINK = (By.XPATH, "//a[@href='/']//p[text()='Конструктор']")
    FEED_LINK = (By.XPATH, "//a[@href='/feed']//p[text()='Лента Заказов']")
    ACCOUNT_LINK = (By.XPATH, "//a[@href='/account']")
    INGREDIENT_CARD = (By.CSS_SELECTOR, "a.BurgerIngredient_ingredient__1TVf6")
    INGREDIENT_COUNTER = (By.CSS_SELECTOR, "p.counter_counter__num__3nue1")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")
    ORDER_BUTTON = (By.CSS_SELECTOR, "button.button_button__33qZ0.button_button_type_primary__1O7Bx")
    CONSTRUCTOR_BASKET =  (By.CSS_SELECTOR, "span.BurgerConstructor_basket__listContainer__3P_AM")
    MAKE_ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")

    @allure.step("Открыть окно")
    def open(self):
        super().open(BASE_URL)
        self._wait.until(EC.invisibility_of_element_located(ModalLocators.LOADING_MODAL_OPENED))

    @allure.step("Клик по линку конструктора")
    def click_constructor(self):
        self._wait.until(EC.presence_of_element_located(self.CONSTRUCTOR_LINK)).click()

    @allure.step("Клик по линку фида")
    def click_feed(self):
        self._wait.until(EC.element_to_be_clickable(self.FEED_LINK)).click()

    @allure.step("Клик по первому ингредиенту")
    def click_first_ingredient(self):
        self._wait.until(EC.element_to_be_clickable(self.INGREDIENT_CARD)).click()

    def is_modal_open(self):
        try:
            self._wait.until(EC.visibility_of_element_located(ModalLocators.MODAL_OPENED))
            return True
        except:
            return False

    @allure.step("Закрыть модальное окно")
    def close_modal(self):
        self._wait.until(EC.element_to_be_clickable(ModalLocators.MODAL_CLOSE)).click()

    def is_modal_closed(self):
        try:
            self._wait.until(EC.invisibility_of_element_located(ModalLocators.MODAL_OPENED))
            return True
        except:
            return False
