from selenium.webdriver.common.by import By

class FeedPageLocators:
    COUNTER_ALL_TIME = (By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p")
    COUNTER_TODAY = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p")
    IN_PROGRESS_LIST = (By.XPATH, "//p[text()='В работе:']/following-sibling::ul")
    ORDER_LIST = (By.CSS_SELECTOR, "ul.OrderFeed_list__OLh59")
