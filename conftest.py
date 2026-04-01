import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from page_objects.login_page import LoginPage

EMAIL = 'aleksandrpushkin@yandex.ru'
PASSWORD = 'parol1-dlya-testa23!'


@pytest.fixture(params=['chrome', 'firefox'])
def driver(request):
    browser = request.param

    if browser == 'chrome':
        options = ChromeOptions()
        options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=options)
    else:
        options = FirefoxOptions()
        driver = webdriver.Firefox(options=options)

    driver.maximize_window()

    yield driver

    driver.quit()

@pytest.fixture
def logged_in_driver(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(EMAIL, PASSWORD)

    wait = WebDriverWait(driver, 10)

    # Ждём, что пользователь реально залогинился
    wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "//button[text()='Оформить заказ']")
        )
    )

    return driver
