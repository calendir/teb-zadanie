from selenium.webdriver.remote.webdriver import By, WebDriver


class MainWPPage:
    URL = 'https://s1.demo.opensourcecms.com/wordpress'

    def __init__(self, browser: WebDriver):
        self.browser = browser

    def open(self):
        self.browser.get(self.URL)

    def get_recent_post_links(self):
        return self.browser.find_elements_by_css_selector('#recent-posts-2 ul li a')
