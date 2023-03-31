import src.utils as u

import src.pages.personal_area as pers
import src.pages.login as lg
import src.pages.homepage as hp
import src.pages.sidebar as sbar
import src.pages.products as prod
import src.pages.checkout as chk

from src.locators.locators_index import CheckoutLocators



def test_buy_item_then_see_it_in_last_order(driver):
    """
    Personal - Last Orders - Last orders are updated and shown properly
    gonna be long
    steps:
        1. get into a product
        2. buy it
        3. checkout
        4. ???
        5. profit
    :param driver:
    :return:
    """

    store_details = {'store_name': 'בילבי תעשיות רשע בע"מ', 'store_bn': '16495621', 'store_email': 'fake.mail@fake.domain.com'}

    lg.just_login_in_one_line_code(driver, '0500000000')
    hp.click_on_random_item(driver)
    u.close_popup(driver)
    prod.click_quantity_add(driver)
    sbar.click_that(driver, 'checkout')
    u.sleep(5)

    chk.fill_this_field(driver, 'store_name', )
