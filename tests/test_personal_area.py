import src.utils as u
import src.pages.personal_area as pers
import src.pages.login as lg

from src.locators.locators_index import PersonalLocators


@u.pytest.fixture
def driver():
    get_driver = u.setup_driver(modal=True)
    yield get_driver
    get_driver.close()


def test_get_to_personal_area(driver):
    """
    :param driver:
    :return:
    """
    lg.just_login_in_one_line_code(driver, '0500000000')
    pers.get_to_personal_area(driver)
    assert driver.current_url == 'https://qa.trado.co.il/user/personalArea'


def test_adding_valid_credit_card(driver):
    """
    Personal - Delivery - Adding credit card saves the card for next usages
    :return:
    """

    valid_details = {'cc': '4580000000000000', 'cvv' : '123', 'exp_month' : '5','exp_year' : '2024','ID' : '233160712' }

    lg.just_login_in_one_line_code(driver, '0500000000')
    pers.get_to_personal_area(driver)
    pers.click_that(driver, 'new_cc_btn')


    driver.switch_to.frame('yaadFrame')     # this section is becoming into iframe
    pers.fill_this_field(driver, 'field_cc_number', valid_details['cc'])
    pers.fill_this_field(driver, 'field_id_number', valid_details['ID'])
    pers.select_field_option(driver, 'field_expmonth', valid_details['exp_month'])
    pers.select_field_option(driver, 'field_expyear', valid_details['exp_year'])
    pers.fill_this_field(driver, 'field_cvv', valid_details['cvv'])
    pers.click_that(driver, 'pay_btn')

    err_elem = pers.get_element(driver, 'iframe_error')

    assert not err_elem


def test_adding_invalid_credit_card(driver):
    """
    Personal - Delivery - Adding credit card validates the credit card and the ID
    first time - all letters and ten or more chars
    second time - numbers and letter together, ten chars
    third time - all random numbers, cc:16, cvv:3, ID:9. there is a little to no chance it will success to generate real and valid ID and CC
    todo needs a better and more stable assertion than number of errors. maybe check if it goes to the next page at all

    :return:
    """

    invalid_details_set1 = {'cc': u.rand_string(u.string.ascii_letters, n=10), 'cvv': u.rand_string(u.string.ascii_letters, n=10), 'ID': u.rand_string(u.string.ascii_letters, n=5)}
    invalid_details_set2 = {'cc': u.rand_string(u.string.ascii_letters, n=16), 'cvv': u.rand_string(n=5), 'ID': u.rand_string(u.string.ascii_letters, n=5)}
    invalid_details_set3 = {'cc': u.rand_string(n=16), 'cvv': u.rand_string(n=2), 'ID': u.rand_string(n=9)}

    invalid_sets = [invalid_details_set1, invalid_details_set2, invalid_details_set3]

    lg.just_login_in_one_line_code(driver, '0500000000')
    pers.get_to_personal_area(driver)
    pers.click_that(driver, 'new_cc_btn')


    driver.switch_to.frame('yaadFrame')     # this section is becoming into iframe
    pers.select_field_option(driver, 'field_expmonth', '6')  # select limited
    pers.select_field_option(driver, 'field_expyear', '2025')      # select limited
    for testset in invalid_sets:

        pers.fill_this_field(driver, 'field_cc_number', testset['cc'])
        pers.fill_this_field(driver, 'field_id_number', testset['ID'])
        pers.fill_this_field(driver, 'field_cvv', testset['cvv'])
        u.sleep(2)
        pers.click_that(driver, 'pay_btn')

        errors_count = pers.get_elements(driver, 'error_class')
        credit_error = pers.get_elements(driver, 'credit_error')

        try:
            assert 3 <= len(errors_count) + len(credit_error)
        except AssertionError:
            driver.save_screenshot('D:\Github\IITC_trado_final_project\media\pp.png')
            raise AssertionError
