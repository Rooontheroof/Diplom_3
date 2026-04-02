from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from constants import FEED_URL
from page_objects.base_page import BasePage
from page_objects.modal_locators import ModalLocators


class FeedPage(BasePage):
    COUNTER_ALL_TIME = (By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p")
    COUNTER_TODAY = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p")
    IN_PROGRESS_LIST = (By.XPATH, "//p[text()='В работе:']/following-sibling::ul")
    ORDER_LIST = (By.CSS_SELECTOR, "ul.OrderFeed_list__OLh59")

    def open(self):
        super().open(FEED_URL)
        self._wait.until(EC.invisibility_of_element_located(ModalLocators.LOADING_MODAL_OPENED))

    def get_counter_all_time(self):
        element = self._wait.until(EC.presence_of_element_located(self.COUNTER_ALL_TIME))
        return int(element.text)

    def get_counter_today(self):
        element = self._wait.until(EC.presence_of_element_located(self.COUNTER_TODAY))
        return int(element.text)
