from selenium.webdriver.common.by import By


class OrderPageLocators:
    ORDER_BUTTON = (By.CSS_SELECTOR, "button.button_button__33qZ0.button_button_type_primary__1O7Bx")
    ORDER_IDENTIFIER_TEXT = (By.XPATH, "//p[text()='идентификатор заказа']")
    TARGET_DRAG_AND_DROP_ELEMENT = (By.CSS_SELECTOR, "section.BurgerConstructor_basket__29Cd7")
    ORDER_IMAGE_ELEMENT = (By.CSS_SELECTOR, "img.constructor-element__image")
