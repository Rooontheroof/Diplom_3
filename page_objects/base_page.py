import allure
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from locators.modal_page import ModalPageLocators


class BasePage:
    def __init__(self, driver):
        self._driver = driver
        self._wait = WebDriverWait(driver, 10)

    def open_page(self, url):
        self._driver.get(url)

    def find(self, locator):
        return self._wait.until(EC.visibility_of_element_located(locator))

    def click(self, locator):
        self.wait_until_locator_clickable(locator).click()

    @allure.step("Клик по элементу, если он появился")
    def click_if_clickable(self, locator):
        try:
            self.wait_until_locator_clickable(locator).click()
        except TimeoutException:
            return

    def fill(self, locator, text):
        element = self.find(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        return self.find(locator).text

    def get_current_url(self):
        return self._driver.current_url

    def is_visible(self, locator):
        try:
            self.find(locator)
            return True
        except Exception:
            return False

    def scroll_to(self, locator):
        element = self.find(locator)
        self._driver.execute_script("arguments[0].scrollIntoView();", element)

    def get_modal_window_title(self):
        return self._wait.until(EC.visibility_of_element_located(ModalPageLocators.MODAL_TITLE))

    @allure.step("Переключение на новую вкладку")
    def switch_to_new_tab(self):
        self._wait.until(lambda d: len(d.window_handles) > 1)
        self._driver.switch_to.window(self._driver.window_handles[-1])
        self._wait.until(lambda d: d.current_url != "about:blank")

    def wait_until_modal_invisible(self):
        self.wait_until_locator_invisible(ModalPageLocators.LOADING_MODAL_OPENED)

    def wait_until_locator_visible(self, locator):
        return self._wait.until(EC.visibility_of_element_located(locator))

    def wait_until_locator_invisible(self, locator):
        return self._wait.until(EC.invisibility_of_element_located(locator))

    def wait_until_locator_clickable(self, locator):
        return self._wait.until(EC.element_to_be_clickable(locator))

    def wait_until_present(self, locator):
        return self._wait.until(EC.presence_of_element_located(locator))

    def refresh(self):
        self._driver.refresh()
