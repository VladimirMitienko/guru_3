from selene import browser, be, have
import pytest


def test_browser(setting_browser):
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))


def test_invalid_search(setting_browser):
    browser.element('[name="q"]').should(be.blank).type('77fgfgfgfg666566').press_enter()
    browser.element('[class="v3jTId"]').should(have.text('Похоже, по вашему запросу нет полезных результатов'))