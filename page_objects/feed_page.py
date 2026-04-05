import allure
from selenium.webdriver.support import expected_conditions as EC

from constants import FEED_URL
from locators.feed_page import FeedPageLocators
from page_objects.base_page import BasePage


class FeedPage(BasePage):
    @allure.step("Открыть окно")
    def open(self):
        self.open_page(FEED_URL)
        self.wait_until_modal_invisible()

    @allure.step("Взять общее количество бургеров")
    def get_counter_all_time(self):
        element = self._wait.until(EC.presence_of_element_located(FeedPageLocators.COUNTER_ALL_TIME))
        return int(element.text)

    @allure.step("Взять количество бургеров за сегодня")
    def get_counter_today(self):
        element = self.wait_until_present(FeedPageLocators.COUNTER_TODAY)
        return int(element.text)

    @allure.step("Ждем, пока количество бургеров за сегодня не поменяется")
    def wait_until_counter_today_updated(self, previous_counter):
        self._wait.until(lambda d: self.get_counter_today() > previous_counter)

    @allure.step("Ждем, пока количество бургеров за все время не поменяется")
    def wait_until_counter_all_time_updated(self, previous_counter):
        self._wait.until(lambda d: self.get_counter_all_time() > previous_counter)
