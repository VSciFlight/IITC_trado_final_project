import src.utils as u

from src.locators.locators_index import ProductLocators
import src.pages.homepage as hp
import src.pages.products as prod
import src.pages.sidebar as sbar
import src.pages.login as lg

@u.pytest.fixture
def driver():
    get_driver = u.setup_driver()
    yield get_driver
    get_driver.close()


@u.pytest.mark.functional
def test_price_from_homepage_to_product_page(driver):
    """
    Products - Profile - Price is corresponding to the price shown in the homepage grid
    :param driver:
    :return:
    """
    homepage_price = hp.get_product_price(driver)
    hp.click_on_random_item(driver)

    product_price = u.WDW(driver, 5).until(u.EC.visibility_of_element_located(ProductLocators.prodloc['product_price'])).text

    assert homepage_price == product_price


@u.pytest.mark.functional
def test_quantity_limit_logical_limit(driver):
    """
    Products - Profile - Quantity cannot be above the available stock
    Products - Profile - Quantity is able to be changed by typing the amount
    :param driver:
    :return:
    """

    hp.click_on_random_item(driver)
    avail_stock = prod.get_product_detailed_stock(driver)
    above_stock = avail_stock + 1

    prod.insert_quantity(driver, above_stock)
    u.click_somewhere_in_the_page(driver)
    u.sleep(1)

    now_quant = u.WDW(driver, 5).until(u.EC.visibility_of_element_located(ProductLocators.prodloc['product_quantity'])).get_attribute('value')
    u.click_somewhere_in_the_page(driver)

    assert int(now_quant) <= avail_stock


@u.pytest.mark.functional
def test_quantity_buttons_responding(driver):
    """
    Products - Profile - Quantity buttons are instantaneous
    Products - Profile - Quantity buttons are adding and subtracting the quantity
    Products - Profile - Increasing the quantity actually adding the items to the cart
    :param driver:
    :return:
    """

    hp.click_on_random_item(driver)
    min_for_purchase = u.WDW(driver, 5).until(u.EC.visibility_of_element_located(ProductLocators.prodloc['product_min_quantity_order'])).text
    min_for_purchase_num = [s for s in min_for_purchase.split() if s.isdigit()]

    start_quant = prod.get_product_quantity(driver)
    prod.click_quantity_add(driver, 'add')
    current_quant = prod.get_product_quantity(driver)
    cart_quant = sbar.get_cart_item_quantity(driver)

    if start_quant == 0:
        assert current_quant - start_quant == int(min_for_purchase_num[0])
        assert cart_quant == current_quant
    else:
        assert current_quant - start_quant == 1
        assert cart_quant == current_quant

    start_quant = prod.get_product_quantity(driver)
    prod.click_quantity_add(driver, 'subtract')
    current_quant = prod.get_product_quantity(driver)
    cart_quant = sbar.get_cart_item_quantity(driver)

    if start_quant == int(min_for_purchase_num[0]):
        assert current_quant - start_quant == -int(min_for_purchase_num[0])
        assert cart_quant == False
    else:
        assert current_quant - start_quant == -1
        assert cart_quant == False


@u.pytest.mark.functional
def test_nonexisting_product_page(driver):
    """
    Products - Profile - Non-exist product id url will generate me a 404 http error or will tell me the product doesn't exist
    :param driver:
    :return:
    """
    non_existing_product_id = u.rand_string(group=u.string.digits, n=10)

    driver.get(f'https://qa.trado.co.il/product/{non_existing_product_id}')
    u.close_popup(driver)

    try:
        u.WDW(driver, 5).until(u.EC.visibility_of_element_located(ProductLocators.prodloc['error_404_message']))
    except u.sel_except.TimeoutException:
        raise u.sel_except.TimeoutException("No Error Indication was found")


@u.pytest.mark.functional
def test_stocks_details(driver):
    """
    Products - Profile - Stock in the square and stock in the table below are matching
    :param driver: 
    :return: 
    """

    hp.click_on_random_item(driver)
    card_stock = prod.get_product_card_stock(driver)
    detailed_stock = prod.get_product_detailed_stock(driver)

    assert card_stock == detailed_stock


def test_suggested_products_are_the_same_supplier(driver):
    """
    Products - Suggested - Items are actually from the same supplier
    :param driver:
    :return:
    """

    hp.click_on_random_item(driver)
    product_name = str(prod.get_product_name(driver))
    store_id_in_db = u.db_get.get_product_supplier(product_name)

    suggested_items = prod.get_elements(driver, 'suggested_items_list')
    if not suggested_items:
        print("No suggested items were found for this product")

    else:
        for i in range(len(suggested_items)):
            sugg_str = str(suggested_items[i].text)
            suggested_in_db = u.db_get.get_product_supplier(sugg_str)
            assert suggested_in_db == store_id_in_db
