import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from page_objects.base_page import BasePage
from seletools.actions import drag_and_drop

from page_objects.feed_page import FeedPage
from page_objects.main_page import MainPage
from page_objects.modal_locators import ModalLocators


class OrderPage(BasePage):
    ORDER_BUTTON = (By.CSS_SELECTOR, "button.button_button__33qZ0.button_button_type_primary__1O7Bx")
    ORDER_IDENTIFIER_TEXT = (By.XPATH, "//p[text()='идентификатор заказа']")
    TARGET_DRAG_AND_DROP_ELEMENT = (By.CSS_SELECTOR, "section.BurgerConstructor_basket__29Cd7")
    ORDER_IMAGE_ELEMENT = (By.CSS_SELECTOR, "img.constructor-element__image")

    @allure.step("Добавить ингредиент")
    def add_first_ingredient(self):
        self._wait.until(EC.invisibility_of_element_located(ModalLocators.LOADING_MODAL_OPENED))
        source = self._wait.until(EC.element_to_be_clickable(MainPage.INGREDIENT_CARD))
        target = self._wait.until(EC.presence_of_element_located(self.TARGET_DRAG_AND_DROP_ELEMENT))
        drag_and_drop(self._driver, source, target)

        self._wait.until(
            lambda d: "/static/media/" not in d.find_element(*self.ORDER_IMAGE_ELEMENT).get_attribute("src")
        )

    @allure.step("Отправить заказ")
    def submit_order(self):
        self._wait.until(EC.invisibility_of_element_located(ModalLocators.LOADING_MODAL_OPENED))
        self._wait.until(EC.element_to_be_clickable(self.ORDER_BUTTON)).click()

    @allure.step("Ждать готовности заказа")
    def wait_for_order_number(self):
        order_modal = self._wait.until(EC.visibility_of_element_located(ModalLocators.ORDER_NUMBER))
        initial_value = order_modal.text.strip()
        self._wait.until(
            lambda d: d.find_element(*ModalLocators.ORDER_NUMBER).text.strip() not in ["", initial_value]
        )
        final_order_number = self._driver.find_element(*ModalLocators.ORDER_NUMBER).text.strip()

        assert final_order_number != "", "Заказ не создался"
        return final_order_number

    @allure.step("Закрыть модальное окно")
    def close_order_modal(self):
        # Если обычная кнопка закрытия перехватывается, кликаем по фону модального окна
        overlay = self._wait.until(EC.presence_of_element_located(ModalLocators.LOADING_MODAL_OPENED))
        self._driver.execute_script("arguments[0].click();", overlay)
        self._wait.until(EC.invisibility_of_element_located(ModalLocators.MODAL_OPENED))

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
                value = int(ingredient_element.find_element(*MainPage.INGREDIENT_COUNTER).text)
                return value > counter_before
            except Exception:
                return False

        return self._wait.until(counter_increased)

    def wait_for_order_in_progress(self, order_number):
        def order_in_list(d):
            try:
                section = d.find_element(*FeedPage.IN_PROGRESS_LIST)
                items = section.find_elements(By.TAG_NAME, 'li')
                return any(str(order_number) in item.text for item in items)
            except Exception:
                return False

        return self._wait.until(order_in_list)
