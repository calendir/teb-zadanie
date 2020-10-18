import time
import uuid

from selenium.webdriver.remote.webdriver import WebDriver
from pages.wordpress.main_page import MainWPPage
from pages.wordpress.post_page import PostPage


def test_ability_to_add_a_comment(browser: WebDriver):
    main_page = MainWPPage(browser)
    main_page.open()
    main_page.get_recent_post_links()[0].click()
    post_page = PostPage(browser)

    comment_text = str(uuid.uuid4())
    author = 'Test'

    post_page.post_comment(comment_text, author, 'lol@nope.com')

    while len(post_page.get_comments_list()) == 1:
        time.sleep(1)

    assert any([comment.get_text().strip() == comment_text and comment.get_author().strip() == author
                for comment in post_page.get_comments_list()])
