import pytest
from selene import browser


@pytest.fixture(autouse=True, scope="session")
def setting_browser():
    browser.config.window_height = 1080  # задает высоту окна браузера
    browser.config.window_width = 1920  # задает ширину окна браузера
    yield
    browser.quit()
