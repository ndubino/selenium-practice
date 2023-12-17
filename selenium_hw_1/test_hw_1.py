"""
Написать параметризованный тест, который:
1 - открывает в любом браузере* сайты https://www.amazon.com/,
https://www.apple.com/, https://www.google.com/
2 - Проверяет, что на сайте заголовке окна для сайта Амазона -
Amazon, для Эпла - Apple, для Гугла - Google
3 - тест должен быть параметризованным. Т.е. должны быть две
переменные url и page_title, которые меняются
4 - на каждый сайт запускается новый тест *.
Можете попробовать запускать разные браузеры на разные сайты, например: для Амазона и Эпла - Firefox,
для Гугла - хром ** В конце теста можно делать скриншот страницы. Делается это через driver.save_screenshot()
"""

import os
from datetime import datetime

import pytest


class TestHW1:
    @pytest.mark.parametrize("url, page_title", [("https://www.amazon.com/", "Amazon"),
                                                 ("https://www.apple.com/", "Apple"),
                                                 ("https://www.google.com/", "Google")])
    def test_websites_chrome(self, driver, url, page_title):
        driver.get(url)
        title_actual = driver.title
        title_expected = page_title
        error_message = f"Expected title: {title_expected}, but actual title: {title_actual}"
        assert page_title in driver.title, error_message
        screenshot_dir = "screenshots"
        timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        screenshot_path = os.path.join(screenshot_dir, f"test_{page_title}_{timestamp}.png")
        driver.save_screenshot(screenshot_path)
        driver.quit()
