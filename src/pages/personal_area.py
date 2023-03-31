import src.utils as u
from src.locators.locators_index import PersonalLocators

import src.pages.login as lg


def get_to_personal_area(driver):
    lg.click_that(driver, 'personal')


def click_that(driver, location):
    u.WDW(driver, 5).until(u.EC.visibility_of_element_located(PersonalLocators.persloc[location])).click()


def fill_this_field(driver, location, data):

    field = u.WDW(driver, 5).until(u.EC.visibility_of_element_located(PersonalLocators.persloc[location]))
    field.click()
    field.clear()
    field.send_keys(data)


def select_field_option(driver, select_field, option_value):
    field = u.WDW(driver, 5).until(u.EC.visibility_of_element_located(PersonalLocators.persloc[select_field]))
    field.click()
    u.WDW(field, 5).until(u.EC.visibility_of_element_located((u.By.XPATH, f'./option[@value={option_value}]'))).click()


def get_element(driver, location):
    elem = u.WDW(driver, 5).until(u.EC.visibility_of_element_located(PersonalLocators.persloc[location]))
    return elem


def get_elements(driver, location):
    try:
        elems = u.WDW(driver, 5).until(u.EC.visibility_of_all_elements_located(PersonalLocators.persloc[location]))
        return elems
    except u.sel_except.TimeoutException:
        print("No suggested items were found")
        return 0

