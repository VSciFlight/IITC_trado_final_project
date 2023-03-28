import src.utils as u
from src.locators.locators_index import SidebarLocators

def get_cart_item_quantity(driver):
    try:
        quant = u.WDW(driver, 5).until(u.EC.visibility_of_element_located(SidebarLocators.sideloc['cart_item_quantity'])).get_attribute('value')
        return int(quant)
    except u.sel_except.TimeoutException:
        print("no item in sidebar!")
        return 0


def click_that(driver, location):
    u.WDW(driver, 5).until(u.EC.visibility_of_element_located(SidebarLocators.sideloc[location])).click()


def count_different_items_in_cart(driver):
    try:
        items = u.WDW(driver, 5).until(u.EC.visibility_of_all_elements_located(SidebarLocators.sideloc['cart_item_row']))
        return len(items)

    except u.sel_except.TimeoutException:
        print("no item in sidebar!")
        return 0
