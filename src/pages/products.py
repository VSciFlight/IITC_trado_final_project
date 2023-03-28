import src.utils as u
from src.locators.locators_index import ProductLocators


def get_product_price(driver):
    price = u.WDW(driver, 5).until(u.EC.visibility_of_element_located(ProductLocators.prodloc['product_price']))
    return price.text


def get_product_detailed_stock(driver):
    stock = u.WDW(driver, 5).until(u.EC.visibility_of_element_located(ProductLocators.prodloc['detailed_stock'])).text
    stock_flt = "".join([flt for flt in stock if flt.isdigit()])
    return int(stock_flt)


def get_product_card_stock(driver):
    stock = u.WDW(driver, 5).until(u.EC.visibility_of_element_located(ProductLocators.prodloc['product_card_stock'])).text
    stock_flt = "".join([flt for flt in stock if flt.isdigit()])
    return int(stock_flt)


def get_product_quantity(driver):
    curr_quantity = u.WDW(driver, 5).until(u.EC.visibility_of_element_located(ProductLocators.prodloc['product_quantity'])).get_attribute('value')
    u.click_somewhere_in_the_page(driver)
    return int(curr_quantity)


def insert_quantity(driver, quantity='0'):
    prod_quan = u.WDW(driver, 5).until(u.EC.visibility_of_element_located(ProductLocators.prodloc['product_quantity']))
    prod_quan.send_keys(quantity)

# def insert_quantity_numpad(driver, quantity='0'):
#     prod_quan = u.WDW(driver, 5).until(u.EC.visibility_of_element_located(ProductLocators.prodloc['product_quantity']))
#     prod_quan.send_keys(quantity)

def click_quantity_add(driver, action = 'add'):
    if action == 'add':
        u.WDW(driver, 5).until(u.EC.visibility_of_element_located(ProductLocators.prodloc['product_quantity_add'])).click()

    elif action == 'subtract':
        u.WDW(driver, 5).until(u.EC.visibility_of_element_located(ProductLocators.prodloc['product_quantity_subtract'])).click()

    u.sleep(1)


