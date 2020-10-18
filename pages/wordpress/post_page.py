from selenium.webdriver.remote.webdriver import By, WebDriver
from pages.wordpress.elements.comment import Comment

class PostPage:
    URL = 'https://s1.demo.opensourcecms.com/wordpress'

    COMMENT_FIELD = (By.CSS_SELECTOR, '#comment')
    AUTHOR_FIELD = (By.CSS_SELECTOR, '#author')
    EMAIL_FIELD = (By.CSS_SELECTOR, '#email')
    POST_BUTTON = (By.CSS_SELECTOR, '#submit')
    COMMENTS = (By.CSS_SELECTOR, 'ol.comment-list li')

    def __init__(self, browser: WebDriver):
        self.browser = browser

    def post_comment(self, comment, author, email):
        self.browser.find_element_by_id('comment').send_keys(comment)
        self.browser.find_element_by_id('author').send_keys(author)
        self.browser.find_element_by_id('email').send_keys(email)
        self.browser.find_element_by_id('submit').click()

    def get_comments_list(self):
        return [Comment(element) for element in self.browser.find_elements(*self.COMMENTS)]
