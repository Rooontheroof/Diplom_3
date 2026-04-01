from selenium.webdriver.support import expected_conditions as EC
from locators.locators import FeedPageLocators
from page_objects.base_page import BasePage


class FeedPage(BasePage):
    URL = 'https://stellarburgers.education-services.ru/feed'

    def open(self):
        super().open(self.URL)

    def get_counter_all_time(self):
        element = self._wait.until(EC.presence_of_element_located(FeedPageLocators.COUNTER_ALL_TIME))
        return int(element.text)

    def get_counter_today(self):
        element = self._wait.until(EC.presence_of_element_located(FeedPageLocators.COUNTER_TODAY))
        return int(element.text)
