import os.path

import pytest
from selenium import webdriver


class TestSelenium:

    @pytest.mark.parametrize('url, page_title',
        [('https://www.amazon.com/', 'amazon'),
         ('https://www.apple.com/', 'apple'),
         ('https://www.google.com/', 'google')
         ]
    )
    def test_selenium_first(self, url, page_title):
        driver = webdriver.Chrome()
        driver.get(url)
        current_url = driver.current_url
        assert page_title in current_url

        screenshot = os.path.join('screenshots', f'{page_title}_screenshot.png')
        driver.save_screenshot(screenshot)