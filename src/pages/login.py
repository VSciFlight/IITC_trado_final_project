import src.utils as u
from src.locators.locators_index import LoginLocators


def click_login(driver):
    # u.WDW(driver, 5).until(u.EC.visibility_of_element_located(LoginLocators.logloc['header_login'])).click()
    u.WDW(driver, 5).until(u.EC.visibility_of_element_located(LoginLocators.logloc['alternative_login'])).click()


def fill_login_info(driver, phone='0500000000'):
    u.WDW(driver, 5).until(u.EC.visibility_of_element_located(LoginLocators.logloc['login_phone'])).send_keys(phone)


def click_modal_login(driver):
    u.WDW(driver, 5).until(u.EC.visibility_of_element_located(LoginLocators.logloc['login_btn'])).click()


def insert_code_into_cells(driver, phone='0500000000'):

    cells = u.WDW(driver, 5).until(u.EC.visibility_of_all_elements_located(LoginLocators.logloc['code_cells']))
    login_code = str(u.db_get.get_login_code_from_db(phone))

    for i in range(5):
        cells[i].send_keys(login_code[i])


def click_verify_button(driver):
    u.WDW(driver, 5).until(u.EC.visibility_of_element_located(LoginLocators.logloc['code_verify'])).click()