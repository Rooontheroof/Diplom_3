import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from locators.locators import ModalLocators, OrderPageLocators, MainPageLocators
from page_objects.base_page import BasePage
from seletools.actions import drag_and_drop


class OrderPage(BasePage):
    def add_first_ingredient(self):
        self._wait.until(EC.invisibility_of_element_located(ModalLocators.LOADING_MODAL_OPENED))
        source = self._wait.until(EC.element_to_be_clickable(MainPageLocators.INGREDIENT_CARD))
        target = self._wait.until(EC.presence_of_element_located(OrderPageLocators.TARGET_DRAG_AND_DROP_ELEMENT))
        drag_and_drop(self._driver, source, target)

        self._wait.until(
            lambda driver: "/static/media/" not in driver.find_element(*OrderPageLocators.ORDER_IMAGE_ELEMENT).get_attribute("src")
        )

    def submit_order(self):
        self._wait.until(EC.invisibility_of_element_located(ModalLocators.LOADING_MODAL_OPENED))
        # Ждем окончания анимации
        time.sleep(0.5)
        self._wait.until(EC.element_to_be_clickable(OrderPageLocators.ORDER_BUTTON)).click()

    def wait_for_order_number(self):
        order_modal = self._wait.until(EC.visibility_of_element_located(ModalLocators.ORDER_NUMBER))
        initial_value = order_modal.text.strip()
        self._wait.until(
            lambda driver: driver.find_element(*ModalLocators.ORDER_NUMBER).text.strip() not in ["", initial_value]
        )
        final_order_number = self._driver.find_element(*ModalLocators.ORDER_NUMBER).text.strip()

        assert final_order_number != "", "Заказ не создался"
        return final_order_number

    def close_order_modal(self):
        # Если обычная кнопка закрытия перехватывается, кликаем по фону модального окна
        overlay = self._wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "div.Modal_modal_overlay__x2ZCr")
        ))
        self._driver.execute_script("arguments[0].click();", overlay)
        self._wait.until(EC.invisibility_of_element_located(ModalLocators.MODAL_OPENED))

    def make_order(self):
        self.add_first_ingredient()
        self.submit_order()
        order_number = self.wait_for_order_number()
        self.close_order_modal()
        return order_number
