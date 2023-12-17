import os

import pytest
from datetime import datetime


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
