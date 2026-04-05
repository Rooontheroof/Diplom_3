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
    MAKE_ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")
