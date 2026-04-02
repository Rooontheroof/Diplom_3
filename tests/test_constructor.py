import allure

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from constants import MAIN_URL
from page_objects.main_page import MainPage
from page_objects.modal_locators import ModalLocators
from page_objects.order_page import OrderPage

@allure.suite('Основная функциональность')
class TestConstructor:

    @allure.title('Переход по клику на «Конструктор»')
    def test_click_constructor_navigates_to_main(self, driver):
        page = MainPage(driver)
        page.open()
        page.click_constructor()

        assert driver.current_url == MAIN_URL

    @allure.title('Переход по клику на «Лента Заказов»')
    def test_click_feed_navigates_to_feed(self, driver):
        page = MainPage(driver)
        page.open()
        page.click_feed()
        assert '/feed' in driver.current_url

    @allure.title('Клик на ингредиент открывает модальное окно с деталями')
    def test_click_ingredient_opens_modal(self, driver):
        page = MainPage(driver)
        page.open()
        page.click_first_ingredient()
        assert page.is_modal_open()

    @allure.title('Модальное окно ингредиента содержит заголовок «Детали ингредиента»')
    def test_ingredient_modal_has_title(self, driver):
        page = MainPage(driver)
        page.open()
        page.click_first_ingredient()
        title = page._wait.until(EC.visibility_of_element_located(ModalLocators.MODAL_TITLE))
        assert 'Детали ингредиента' in title.text

    @allure.title('Модальное окно закрывается кликом по крестику')
    def test_close_modal_by_close_button(self, driver):
        page = MainPage(driver)
        page.open()
        page.click_first_ingredient()
        page.close_modal()
        assert page.is_modal_closed()

    @allure.title('При добавлении ингредиента счётчик увеличивается')
    def test_ingredient_counter_increases_on_add(self, driver, wait):
        order_page = OrderPage(driver)
        page = MainPage(driver)
        page.open()

        ingredient = wait.until(EC.presence_of_element_located(MainPage.INGREDIENT_CARD))
        counter_before = int(ingredient.find_element(*MainPage.INGREDIENT_COUNTER).text)

        order_page.add_first_ingredient()

        order_page.wait_for_counter_to_increase(ingredient, counter_before)

        counter_after = int(ingredient.find_element(*MainPage.INGREDIENT_COUNTER).text)

        assert counter_after > counter_before
