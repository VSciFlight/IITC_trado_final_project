import src.utils as u
from src.locators.locators_index import RegisterLocators
from src.locators.locators_index import LoginLocators

def get_to_register(driver):
    u.WDW(driver, 5).until(u.EC.visibility_of_element_located(LoginLocators.logloc['alternative_login'])).click()
    u.WDW(driver, 5).until(u.EC.visibility_of_element_located(RegisterLocators.regloc['register_tab'])).click()


def fill_number(driver, phone='0500000000'):
    u.WDW(driver, 5).until(u.EC.visibility_of_element_located(RegisterLocators.regloc['phone'])).send_keys(phone)

def fill_bn(driver, bn=u.rand_string()):
    u.WDW(driver, 5).until(u.EC.visibility_of_element_located(RegisterLocators.regloc['business_number'])).send_keys(bn)


def click_that(driver, location):
    u.WDW(driver, 5).until(u.EC.visibility_of_element_located(RegisterLocators.regloc[location])).click()


def insert_code_into_cells(driver, phone='0500000000'):

    cells = u.WDW(driver, 5).until(u.EC.visibility_of_all_elements_located(RegisterLocators.regloc['code_cells']))
    login_code = str(u.db_get.get_login_code_from_db(phone))

    for i in range(5):
        cells[i].send_keys(login_code[i])

