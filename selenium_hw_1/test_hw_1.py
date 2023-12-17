import pytest
from datetime import datetime


class TestHW1:
    @pytest.mark.parametrize("url, page_title", [("https://www.amazon.com/", "Amazon"),
                                                 ("https://www.apple.com/", "Apple"),
                                                 ("https://www.google.com/", "Google")])
    def test_websites_chrome(self, driver, url, page_title):
        driver.get(url)
        assert page_title in driver.title
        timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        driver.save_screenshot(f"test_{page_title}_{timestamp}.png")
