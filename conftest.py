import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.support.ui import WebDriverWait

#@pytest.fixture(params=['chrome', 'firefox'])
@pytest.fixture(params=['chrome'])
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
def wait(driver):
    return WebDriverWait(driver, 10)
