from selene import browser, be, have
import pytest


@pytest.fixture
def test_first(setting_browser):
    browser.open("https://www.google.com/")


def test_browser():
    browser.open("https://www.google.com/")
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))


def test_invalid_search(setting_browser):
    browser.open("https://www.google.com/")
    browser.element('[name="q"]').should(be.blank).type('%$%^$#%#^%$^%@%@$@#$!%@#$%@#%%#%@%FDGdffgdsfgsdg').press_enter()
    browser.element('[class="gL9Hy d2IKib"]').should(have.text('Возможно, вы имели в виду:'))