import time

from selenium.webdriver.remote.webdriver import WebDriver
from .page import KierunkiPage


def test_filters_present(browser: WebDriver):
    page = KierunkiPage(browser)
    page.open()
    actual = dict((name, page.get_options_for_filter(name)) for name in page.get_filter_names())
    expected = {
        'Miasto': ['Opole', 'Poznań', 'Gdynia', 'Gdańsk', 'Chorzów/Katowice', 'Toruń', 'Szczecin', 'Wrocław', 'Bydgoszcz', 'Warszawa'],
        'Poziom kształcenia': ['Studia inżynierskie', 'Studia licencjackie'],
        'Język wykładowy': ['Angielski', 'Polski']
    }
    assert expected == actual


def test_filtering(browser: WebDriver):
    page = KierunkiPage(browser)
    page.open()
    page.switch_city_filter_by_name('Wrocław')
    page.switch_type_filter_by_name('Studia inżynierskie')
    time.sleep(1)
    programs = page.get_displayed_programs()
    assert len(programs) == 3
    for program in programs:
        assert program.get_name() != ''
        assert program.get_image_url() != ''
        assert all([city != '' for city in program.get_cities()])


def test_search_present(browser: WebDriver):
    page = KierunkiPage(browser)
    page.open()
    assert browser.find_element(*page.SEARCH_FIELD).is_displayed()


def test_sort_present(browser: WebDriver):
    page = KierunkiPage(browser)
    page.open()
    assert browser.find_element(*page.SORT_FIELD).is_displayed()


def test_sign_up_button_present(browser: WebDriver):
    page = KierunkiPage(browser)
    page.open()
    sign_up_button = browser.find_element(*page.SIGN_UP_BUTTON)
    assert sign_up_button.is_displayed()
    assert sign_up_button.text == 'Zapisz się online'
