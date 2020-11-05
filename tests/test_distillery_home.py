from pages.main_page import MainPage
import pytest
from utils.assertions import assert_text, assert_element_displayed


@pytest.mark.login_guest
class TestLoginFromMainPage():
    def test_main_page_header_is_correct(self, driver):
        main_page = MainPage(driver)
        main_page.open()

        header = main_page.get_element(main_page.header_locator)
        expected_header_text = main_page.main_page_header_text

        assert_text(header, expected_header_text)

    def test_learn_about_us_button_is_displayed(self, driver):
        main_page = MainPage(driver)
        main_page.open()

        learn_about_us_button = main_page.get_element(main_page.learn_about_us_button)

        assert_element_displayed(learn_about_us_button)
