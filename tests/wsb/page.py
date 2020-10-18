from selenium.webdriver.remote.webdriver import By, WebDriver
from .elements import Program


class KierunkiPage:
    URL = 'https://www.wsb.pl/studia-i-szkolenia/studia-i-stopnia/kierunki-i-specjalnosci'

    SEARCH_FIELD = (By.CSS_SELECTOR, '#listing-search')
    SORT_FIELD = (By.CSS_SELECTOR, '.sort .select-list')
    SIGN_UP_BUTTON = (By.CSS_SELECTOR, '#header-page-title a.button.secondary')

    def __init__(self, browser: WebDriver):
        self.browser = browser

    def open(self):
        self.browser.get(self.URL)

    def get_filter_names(self):
        return [element.text for element in self.browser.find_elements_by_css_selector('.filters .options p.title')]

    def get_options_for_filter(self, filter_name):
        return [element.text for element in self.browser.find_elements_by_css_selector(
            '.filters .options:nth-of-type({0}) label'.format(self.get_filter_names().index(filter_name) + 1)
        )]

    def switch_city_filter_by_name(self, city_name: str):
        self.find_element_with_text('.filters .options:nth-of-type(1) label', city_name)\
            .find_element_by_css_selector('.box').click()

    def switch_type_filter_by_name(self, type_name: str):
        self.find_element_with_text('.filters .options:nth-of-type(2) label', type_name)\
            .find_element_by_css_selector('.box').click()

    def get_displayed_programs(self):
        return [Program(element) for element in self.browser.find_elements_by_css_selector('.study-directions .direction')]

    def find_element_with_text(self, selector, text):
        return next((elem for elem in self.browser.find_elements_by_css_selector(selector) if elem.text.startswith(text)), None)
