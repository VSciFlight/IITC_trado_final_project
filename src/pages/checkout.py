import src.utils as u
from src.locators.locators_index import CheckoutLocators

def get_element(driver, location):
    elem = u.WDW(driver, 5).until(u.EC.visibility_of_element_located(CheckoutLocators.chkloc[location]))
    return elem


def get_elements(driver, location):
    try:
        elems = u.WDW(driver, 5).until(u.EC.visibility_of_all_elements_located(CheckoutLocators.chkloc[location]))
        return elems
    except u.sel_except.TimeoutException:
        print("No suggested items were found")
        return 0

def click_that(driver, location):
    u.WDW(driver, 5).until(u.EC.visibility_of_element_located(CheckoutLocators.chkloc[location])).click()

def fill_this_field(driver, location, data):
    field = u.WDW(driver, 5).until(u.EC.visibility_of_element_located(CheckoutLocators.chkloc[location]))
    field.clear()
    field.send_keys(data)