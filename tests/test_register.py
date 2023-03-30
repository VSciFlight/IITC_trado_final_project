import src.utils as u

import src.pages.register as rg
import src.pages.login as lg

@u.pytest.fixture
def driver():
    get_driver = u.setup_driver(modal=True)
    yield get_driver
    get_driver.close()


def test_valid_register(driver):
    """
    Users - Register - "Valid" registeration
    Users - Register - Able to register with non-Israeli number (not +972)
    :param driver:
    :return:
    """

    rand_phone = u.rand_string()
    # lg.click_login(driver)
    rg.get_to_register(driver)
    rg.fill_number(driver, rand_phone)
    rg.fill_bn(driver)
    rg.click_that(driver, 'approve_policy')
    rg.click_that(driver, 'submit_btn')

    rg.insert_code_into_cells(driver, rand_phone)
    rg.click_that(driver, 'code_verify')

    u.close_popup(driver)
    u.sleep(2)

    header_indicator = lg.get_login_indication(driver)
    rec = u.db_get.get_record('users', 'phone', rand_phone)

    assert len(rec) > 0
    assert rec['phone'] == rand_phone
    assert header_indicator != "התחברות"



def test_register_with_chars_in_phone_field(driver):
    """
    Users - Register - able to register with characters in phone field (no numbers)
    :param driver:
    :return:
    """

    char_phone = u.rand_string(group=u.string.ascii_lowercase)
    # lg.click_login(driver)
    rg.get_to_register(driver)
    rg.fill_number(driver, char_phone)
    rg.fill_bn(driver)
    rg.click_that(driver, 'approve_policy')
    rg.click_that(driver, 'submit_btn')

    rg.insert_code_into_cells(driver, char_phone)
    rg.click_that(driver, 'code_verify')

    u.close_popup(driver)
    u.sleep(2)

    header_indicator = lg.get_login_indication(driver)
    rec = u.db_get.get_record('users', 'phone', char_phone)

    assert len(rec) > 0
    assert rec['phone'] == char_phone
    assert header_indicator == "התחברות"



def test_register_with_invalid_bn(driver):
    """
    Users - Register - able to register with invalid BN
    BN should be ONLY numbers, however I can write e and dots in it.
    BN: 12.3e55
    :param driver:
    :return:
    """
    rand_phone = u.rand_string()
    bn = '12.3e55'
    # lg.click_login(driver)
    rg.get_to_register(driver)
    rg.fill_number(driver, rand_phone)
    rg.fill_bn(driver, bn=bn)
    rg.click_that(driver, 'approve_policy')
    rg.click_that(driver, 'submit_btn')

    rg.insert_code_into_cells(driver, rand_phone)
    rg.click_that(driver, 'code_verify')

    u.close_popup(driver)
    u.sleep(2)
    header_indicator = lg.get_login_indication(driver)
    rec = u.db_get.get_record('users', 'phone', rand_phone)

    assert len(rec) > 0
    assert rec['phone'] == rand_phone
    assert header_indicator == "התחברות"






