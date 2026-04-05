import allure

from constants import BASE_URL
from locators.main_page import MainPageLocators
from locators.modal_page import ModalPageLocators
from page_objects.base_page import BasePage


class MainPage(BasePage):
    @allure.step("Открыть окно")
    def open(self):
        self.open_page(BASE_URL)
        self.wait_until_modal_invisible()

    @allure.step("Клик по линку конструктора")
    def click_constructor(self):
        self.click(MainPageLocators.CONSTRUCTOR_LINK)

    @allure.step("Клик по линку фида")
    def click_feed(self):
        self.click(MainPageLocators.FEED_LINK)

    @allure.step("Клик по первому ингредиенту")
    def click_first_ingredient(self):
        self.click(MainPageLocators.INGREDIENT_CARD)

    def is_modal_open(self):
        try:
            self.wait_until_locator_visible(ModalPageLocators.MODAL_OPENED)
            return True
        except:
            return False

    @allure.step("Закрыть модальное окно")
    def close_modal(self):
        self.click(ModalPageLocators.MODAL_CLOSE)

    def is_modal_closed(self):
        try:
            self.wait_until_locator_invisible(ModalPageLocators.MODAL_OPENED)
            return True
        except:
            return False

    @allure.step("Взять ингредиент")
    def get_ingredient(self):
        return self.wait_until_present(MainPageLocators.INGREDIENT_CARD)

    @allure.step("Взять текущее кол-во ингредиента")
    def get_ingredient_counter(self, ingredient):
        return int(ingredient.find_element(*MainPageLocators.INGREDIENT_COUNTER).text)
