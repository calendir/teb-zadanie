import pytest

from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def browser():
    driver = Chrome(ChromeDriverManager().install())
    yield driver
    driver.quit()
