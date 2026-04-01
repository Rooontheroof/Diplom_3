import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from page_objects.main_page import MainPage
from page_objects.feed_page import FeedPage
from page_objects.order_page import OrderPage
from locators.locators import ModalLocators, FeedPageLocators


@allure.suite('Лента заказов')
class TestOrderFeed:

    @allure.title('Счётчик «Выполнено за всё время» увеличивается после создания заказа')
    def test_counter_all_time_increases(self, logged_in_driver):
        driver = logged_in_driver
        wait = WebDriverWait(driver, 20)

        feed = FeedPage(driver)
        main = MainPage(driver)
        order_page = OrderPage(driver)

        feed.open()
        counter_before = feed.get_counter_all_time()

        main.open()
        order_page.make_order()

        feed.open()
        driver.refresh()

        wait.until(lambda d: feed.get_counter_all_time() > counter_before)

        counter_after = feed.get_counter_all_time()
        assert counter_after > counter_before


    @allure.title('Счётчик «Выполнено за сегодня» увеличивается после создания заказа')
    def test_counter_today_increases(self, logged_in_driver):
        driver = logged_in_driver
        wait = WebDriverWait(driver, 20)

        feed = FeedPage(driver)
        main = MainPage(driver)
        order_page = OrderPage(driver)

        feed.open()
        counter_before = feed.get_counter_today()

        main.open()
        order_page.make_order()

        feed.open()
        driver.refresh()

        wait.until(lambda d: feed.get_counter_today() > counter_before)

        counter_after = feed.get_counter_today()
        assert counter_after > counter_before


    @allure.title('После оформления заказа его номер появляется в разделе «В работе»')
    def test_order_number_appears_in_progress(self, logged_in_driver):
        driver = logged_in_driver
        wait = WebDriverWait(driver, 30)

        main = MainPage(driver)
        feed = FeedPage(driver)
        order_page = OrderPage(driver)

        main.open()
        order_number = order_page.make_order()

        feed.open()
        driver.refresh()

        def order_in_list(d):
            try:
                section = d.find_element(*FeedPageLocators.IN_PROGRESS_LIST)
                items = section.find_elements(By.TAG_NAME, 'li')
                return any(order_number in item.text for item in items)
            except Exception:
                return False

        assert wait.until(order_in_list), f'Номер заказа {order_number} не появился в «В работе»'
