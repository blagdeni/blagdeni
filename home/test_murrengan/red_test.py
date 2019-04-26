import time
import pytest
from selenium import webdriver
#from django.urls import resolve

#from home.views import home

@pytest.fixture
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()


def test_title(browser):
    time.sleep(2)

    browser.get('http://127.0.0.1:8000/home/')
#    header_text = browser.find_element_by_tag_name('h1').text
#    inputbox = browser.find_element_by_id('Rrrr')
#    inputbox.send_keys('Blagdeni')
    time.sleep(2)

#    assert header_text == 'Blagdeni'
    assert browser.title == 'Blagdeni'

#def test_home():
#    found = resolve('/home/')
#    assert found.func == home



