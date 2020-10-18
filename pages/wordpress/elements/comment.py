from selenium.webdriver.remote.webelement import WebElement


class Comment:
    def __init__(self, root_element: WebElement):
        self.root = root_element

    def get_author(self):
        return self.root.find_element_by_css_selector('.comment-author .fn').text

    def get_text(self):
        return self.root.find_element_by_css_selector('.comment-content').text
