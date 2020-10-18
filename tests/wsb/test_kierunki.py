from selenium.webdriver.remote.webdriver import WebDriver
from .page import KierunkiPage


def test_kierunki(browser: WebDriver):
    page = KierunkiPage(browser)
    page.open()
    page.switch_city_filter_by_name('Wrocław')
    page.switch_type_filter_by_name('Studia inżynierskie')
    programs = page.get_displayed_programs()
    assert len(programs) == 3
    for program in programs:
        assert program.get_name() != ''
        assert program.get_image_url() != ''
        assert all([city != '' for city in program.get_cities()])
