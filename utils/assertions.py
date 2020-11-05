from selenium.webdriver.remote.webelement import WebElement


def assert_element_displayed(element):
    assert element.is_displayed()


def assert_text(element: WebElement, text):
    if element.tag_name == "input":
        actual_text = element.get_attribute("value").strip().lower()
    else:
        actual_text = element.text.strip().lower()
    assert actual_text == text.strip().lower(), \
        "Expected is :{}, but actual was :{}".format(text.lower(), actual_text)


def assert_script_presented(script):
    assert script, "Element isn't presented on the Page"

