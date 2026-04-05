import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from locators.feed_page import FeedPageLocators
from locators.main_page import MainPageLocators
from locators.modal_page import ModalPageLocators
from locators.order_page import OrderPageLocators
from page_objects.base_page import BasePage
from seletools.actions import drag_and_drop


class OrderPage(BasePage):
    @allure.step("Добавить ингредиент")
    def add_first_ingredient(self):
        self.wait_until_modal_invisible()
        source = self.wait_until_locator_clickable(MainPageLocators.INGREDIENT_CARD)
        target = self.wait_until_present(OrderPageLocators.TARGET_DRAG_AND_DROP_ELEMENT)
        drag_and_drop(self._driver, source, target)

        self._wait.until(
            lambda d: "/static/media/" not in d.find_element(*OrderPageLocators.ORDER_IMAGE_ELEMENT).get_attribute("src")
        )

    @allure.step("Отправить заказ")
    def submit_order(self):
        self.wait_until_modal_invisible()
        self.click(OrderPageLocators.ORDER_BUTTON)

    @allure.step("Ждать готовности заказа")
    def wait_for_order_number(self):
        order_modal = self.wait_until_locator_visible(ModalPageLocators.ORDER_NUMBER)
        initial_value = order_modal.text.strip()
        self._wait.until(
            lambda d: d.find_element(*ModalPageLocators.ORDER_NUMBER).text.strip() not in ["", initial_value]
        )
        final_order_number = self._driver.find_element(*ModalPageLocators.ORDER_NUMBER).text.strip()

        return final_order_number

    @allure.step("Закрыть модальное окно")
    def close_order_modal(self):
        # Если обычная кнопка закрытия перехватывается, кликаем по фону модального окна
        overlay = self.wait_until_present(ModalPageLocators.LOADING_MODAL_OPENED)
        self._driver.execute_script("arguments[0].click();", overlay)
        self.wait_until_locator_invisible(ModalPageLocators.MODAL_OPENED)

    @allure.step("Оформить заказ")
    def make_order(self):
        self.add_first_ingredient()
        self.submit_order()
        order_number = self.wait_for_order_number()
        self.close_order_modal()
        return order_number

    def wait_for_counter_to_increase(self, ingredient_element, counter_before):
        def counter_increased(_):
            try:
                value = int(ingredient_element.find_element(*MainPageLocators.INGREDIENT_COUNTER).text)
                return value > counter_before
            except Exception:
                return False

        return self._wait.until(counter_increased)

    def wait_for_order_in_progress(self, order_number):
        def order_in_list(d):
            try:
                section = d.find_element(*FeedPageLocators.IN_PROGRESS_LIST)
                items = section.find_elements(By.TAG_NAME, 'li')
                return any(str(order_number) in item.text for item in items)
            except Exception:
                return False

        return self._wait.until(order_in_list)
