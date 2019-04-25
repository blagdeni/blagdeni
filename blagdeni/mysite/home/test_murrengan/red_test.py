import time
import pytest
from selenium import webdriver

@pytest.fixture
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()


def test_title(browser):
    time.sleep(1)

    browser.get('http://127.0.0.1:8000/home/')
    header_text = browser.find_element_by_tag_name('h1').text
    inputbox = browser.find_element_by_id('Rrrr')
    inputbox.send_keys('Blagdeni')
    time.sleep(1)

    assert header_text == 'Blagdeni'
    assert browser.title == 'Blagdeni'

