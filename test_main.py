class TestSelenium:

    def test_selenium_first(self, driver):
        # arrange

        driver.get('https://www.python.org/')

        # act
        current_url = driver.current_url
        page_tittle = driver.title
        ...

        # assert
        assert "python" in current_url

    def test_second_first(self, driver):
        # arrange

        driver.get('https://www.python.org/downloads')

        # act
        current_url = driver.current_url

        # assert
        assert "downloads" in current_url
