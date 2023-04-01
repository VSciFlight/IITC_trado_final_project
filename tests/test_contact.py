import src.utils as u
import sys

from src.locators.locators_index import ContactLocators
import src.pages.contact as cnt
import src.pages.homepage as hp


@u.pytest.fixture
def driver():
    get_driver = u.setup_driver()
    yield get_driver
    get_driver.close()


def test_fill_valid_form(driver):
    """
    Contact - Form - Form validates input fields
    Hebrew
    :param driver:
    :return:
    """
    cnt.get_to_contact(driver)

    cnt.fill_first_name(driver, "אסי")
    cnt.fill_last_name(driver, "כהן")
    cnt.fill_email(driver, "example@example.com")
    cnt.fill_phone(driver, "0500000000")
    cnt.fill_content(driver, "פאקשב בדיקה בדיקה")

    cnt.send_form(driver)

    message = cnt.get_form_message(driver)

    assert message == "הפרטים נקלטו בהצלחה"


def test_form_validity(driver):
    """
    Contact - Form - Form validates input fields
    :param driver:
    :return:
    """
    cnt.get_to_contact(driver)

    cnt.click_on_field(driver, 'field_first_name')
    cnt.click_on_field(driver, 'field_last_name')
    cnt.click_on_field(driver, 'field_email')
    cnt.click_on_field(driver, 'field_phone')
    cnt.click_on_field(driver, 'field_content')

    u.click_somewhere_in_the_page(driver)
    u.sleep(2)

    req_msg = driver.find_elements(u.By.XPATH, '//*[text()="נא למלא שדה זה"]')

    assert len(req_msg) == 5


def test_invalid_details(driver):
    """
    Contact - Form - Form validates input fields

    :param driver:
    :return:
    """

    cnt.get_to_contact(driver)

    cnt.fill_first_name(driver, " ")
    cnt.fill_last_name(driver, " ")
    cnt.fill_email(driver, " ")
    cnt.fill_phone(driver, " ")
    cnt.fill_content(driver, " ")

    cnt.send_form(driver)
    message = cnt.get_form_message(driver)

    assert message != "הפרטים נקלטו בהצלחה"


def test_fill_form_with_chaos(driver):
    cnt.get_to_contact(driver)

    cnt.fill_first_name(driver, u.rand_string(u.string.printable))
    cnt.fill_last_name(driver, u.rand_string(u.string.printable))
    cnt.fill_email(driver, u.rand_string(u.string.printable))
    cnt.fill_phone(driver, u.rand_string(u.string.printable))
    cnt.fill_content(driver, u.rand_string(u.string.printable))

    cnt.send_form(driver)
    message = cnt.get_form_message(driver)

    assert message != "הפרטים נקלטו בהצלחה"


def test_fill_content_textarea_above_limit(driver):
    """
    Contact - Form - Form won't let me send above 100 characters in the content
    :param driver:
    :return:
    """
    cnt.get_to_contact(driver)

    nput = u.rand_string(n=101)

    cnt.fill_content(driver, nput)
    textarea = cnt.get_content_field_value(driver)

    assert len(nput) > len(textarea)