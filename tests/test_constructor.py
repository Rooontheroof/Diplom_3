import allure

from constants import MAIN_URL
from page_objects.main_page import MainPage
from page_objects.order_page import OrderPage

@allure.suite('Основная функциональность')
class TestConstructor:

    @allure.title('Переход по клику на «Конструктор»')
    def test_click_constructor_navigates_to_main(self, driver):
        page = MainPage(driver)
        page.open()
        page.click_constructor()

        assert page.get_current_url() == MAIN_URL

    @allure.title('Переход по клику на «Лента Заказов»')
    def test_click_feed_navigates_to_feed(self, driver):
        page = MainPage(driver)
        page.open()
        page.click_feed()
        assert '/feed' in page.get_current_url()

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
        title = page.get_modal_window_title()
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

        ingredient = page.get_ingredient()
        counter_before = page.get_ingredient_counter(ingredient)

        order_page.add_first_ingredient()

        order_page.wait_for_counter_to_increase(ingredient, counter_before)

        counter_after = page.get_ingredient_counter(ingredient)

        assert counter_after > counter_before
