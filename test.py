from selene import browser, be, have
import pytest


@pytest.fixture
def open_browser():
    browser.open('https://google.com')


def test_browser():
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))