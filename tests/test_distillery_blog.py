from pages.main_page import MainPage
import pytest
from utils.assertions import assert_script_presented


@pytest.mark.login_guest
class TestBlogPage():
    def test_mouseflow_script_is_presented(self, driver):
        main_page = MainPage(driver)
        main_page.open()

        blog_page = main_page.open_blog()
        mouseflow_script = blog_page.get_script(blog_page.mouseflow_script)

        assert_script_presented(mouseflow_script)
