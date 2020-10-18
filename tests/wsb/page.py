from selenium.webdriver.remote.webdriver import By, WebDriver
from .elements import Program


class KierunkiPage:
    URL = 'https://www.wsb.pl/studia-i-szkolenia/studia-i-stopnia/kierunki-i-specjalnosci'

    # FILTERS = (By.CSS_SELECTOR, )

    def __init__(self, browser: WebDriver):
        self.browser = browser

    def open(self):
        self.browser.get(self.URL)

    def switch_city_filter_by_name(self, city_name: str):
        self.browser.find_element_by_css_selector(
            ".filters .options:nth-of-type(1) label:contains('{name}')".format(name=city_name)
        ).click()

    def switch_type_filter_by_name(self, city_name: str):
        self.browser.find_element_by_css_selector(
            ".filters .options:nth-of-type(2) label:contains('{name}')".format(name=city_name)
        ).click()

    def get_displayed_programs(self):
        return [Program(element) for element in self.browser.find_elements_by_css_selector('.study-directions .direction')]
