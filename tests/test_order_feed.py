import allure

from selenium.webdriver.common.by import By

from page_objects.login_page import LoginPage
from page_objects.main_page import MainPage
from page_objects.feed_page import FeedPage
from page_objects.order_page import OrderPage


@allure.suite('Лента заказов')
class TestOrderFeed:

    @allure.title('Счётчик «Выполнено за всё время» увеличивается после создания заказа')
    def test_counter_all_time_increases(self, driver):
        login_page = LoginPage(driver)
        login_page.login()

        feed = FeedPage(driver)
        main = MainPage(driver)
        order_page = OrderPage(driver)

        feed.open()
        counter_before = feed.get_counter_all_time()

        main.open()
        order_page.make_order()

        feed.open()
        driver.refresh()

        main._wait.until(lambda d: feed.get_counter_all_time() > counter_before)

        counter_after = feed.get_counter_all_time()
        assert counter_after > counter_before


    @allure.title('Счётчик «Выполнено за сегодня» увеличивается после создания заказа')
    def test_counter_today_increases(self, driver):
        login_page = LoginPage(driver)
        login_page.login()

        feed = FeedPage(driver)
        main = MainPage(driver)
        order_page = OrderPage(driver)

        feed.open()
        counter_before = feed.get_counter_today()

        main.open()
        order_page.make_order()

        feed.open()
        driver.refresh()

        main._wait.until(lambda d: feed.get_counter_today() > counter_before)

        counter_after = feed.get_counter_today()
        assert counter_after > counter_before


    @allure.title('После оформления заказа его номер появляется в разделе «В работе»')
    def test_order_number_appears_in_progress(self, driver):
        login_page = LoginPage(driver)
        login_page.login()

        main = MainPage(driver)
        feed = FeedPage(driver)
        order_page = OrderPage(driver)

        main.open()
        order_number = order_page.make_order()

        feed.open()
        driver.refresh()

        assert order_page.wait_for_order_in_progress(order_number), f'Номер заказа {order_number} не появился в «В работе»'
