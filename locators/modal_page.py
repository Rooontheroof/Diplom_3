from selenium.webdriver.common.by import By


class ModalPageLocators:
    MODAL_OPENED = (By.CSS_SELECTOR, "section.Modal_modal_opened__3ISw4")
    MODAL_TITLE = (By.CSS_SELECTOR, "h2.Modal_modal__title__2L34m")
    MODAL_CLOSE = (By.CSS_SELECTOR, "button.Modal_modal__close__TnseK")
    ORDER_NUMBER = (By.CSS_SELECTOR, "h2.Modal_modal__title_shadow__3ikwq")
    LOADING_MODAL_OPENED = (By.CSS_SELECTOR, "div.Modal_modal_overlay__x2ZCr")
