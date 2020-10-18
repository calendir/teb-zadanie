from selenium.webdriver.remote.webelement import WebElement


class Program:
    def __init__(self, root_element: WebElement):
        self.root = root_element

    def get_image_url(self):
        return self.root.find_element_by_css_selector('.direction-img').get_attribute('src')

    def get_name(self):
        return self.root.find_element_by_css_selector('.study-description .title').text

    def get_cities(self):
        return [element.text for element in self.root.find_elements_by_css_selector('.study-description .cities span')]
