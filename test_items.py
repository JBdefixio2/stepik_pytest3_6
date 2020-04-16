import time
from selenium.common.exceptions import NoSuchElementException


def test_add_to_basket_button_exists(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(30)
    result = False
    try:
        button = browser.find_element_by_class_name("btn-add-to-basket")
        result = True
    except NoSuchElementException:
        result = False
    assert result is True, "Add button not found"
