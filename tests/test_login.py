import src.utils as u

import src.pages.login as lg
from src.locators.locators_index import LoginLocators


@u.pytest.fixture
def driver():
    get_driver = u.setup_driver(modal=True)
    yield get_driver
    get_driver.close()



def test_valid_login(driver):
    """
    Users - Login - Valid login with existing account
    :param driver:
    :return:
    """

    phone = '0526757809'

    lg.click_login(driver)
    lg.fill_login_info(driver, phone)
    lg.click_modal_login(driver)

    u.sleep(2)
    lg.insert_code_into_cells(driver, phone)
    lg.click_verify_button(driver)

    u.sleep(10)
