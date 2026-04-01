from selenium.webdriver.common.by import By


class MainPageLocators:
    CONSTRUCTOR_LINK = (By.XPATH, "//a[@href='/']//p[text()='Конструктор']")
    FEED_LINK = (By.XPATH, "//a[@href='/feed']//p[text()='Лента Заказов']")
    ACCOUNT_LINK = (By.XPATH, "//a[@href='/account']")
    INGREDIENT_CARD = (By.CSS_SELECTOR, "a.BurgerIngredient_ingredient__1TVf6")
    INGREDIENT_COUNTER = (By.CSS_SELECTOR, "p.counter_counter__num__3nue1")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")
    ORDER_BUTTON = (By.CSS_SELECTOR, "button.button_button__33qZ0.button_button_type_primary__1O7Bx")
    CONSTRUCTOR_BASKET =  (By.CSS_SELECTOR, "span.BurgerConstructor_basket__listContainer__3P_AM")


class ModalLocators:
    MODAL_OPENED = (By.CSS_SELECTOR, "section.Modal_modal_opened__3ISw4")
    MODAL_TITLE = (By.CSS_SELECTOR, "h2.Modal_modal__title__2L34m")
    MODAL_CLOSE = (By.CSS_SELECTOR, "button.Modal_modal__close__TnseK")
    ORDER_NUMBER = (By.CSS_SELECTOR, "h2.Modal_modal__title_shadow__3ikwq")
    LOADING_MODAL_OPENED = (By.CSS_SELECTOR, "div.Modal_modal_overlay__x2ZCr")


class FeedPageLocators:
    COUNTER_ALL_TIME = (By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p")
    COUNTER_TODAY = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p")
    IN_PROGRESS_LIST = (By.XPATH, "//p[text()='В работе:']/following-sibling::ul")
    ORDER_LIST = (By.CSS_SELECTOR, "ul.OrderFeed_list__OLh59")


class LoginPageLocators:
    # Из HTML: поле email имеет name="name", поле пароля — name="Пароль"
    EMAIL_INPUT = (By.CSS_SELECTOR, "input[name='name']")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input[name='Пароль']")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")


class OrderPageLocators:
    ORDER_BUTTON = (By.CSS_SELECTOR, "button.button_button__33qZ0.button_button_type_primary__1O7Bx")
    ORDER_IDENTIFIER_TEXT = (By.XPATH, "//p[text()='идентификатор заказа']")
    ORDER_MODAL_CLOSE = (By.CSS_SELECTOR, "div.Modal_modal_overlay__x2ZCr")
    TARGET_DRAG_AND_DROP_ELEMENT = (By.CSS_SELECTOR, "section.BurgerConstructor_basket__29Cd7")
    ORDER_IMAGE_ELEMENT = (By.CSS_SELECTOR, "img.constructor-element__image")

