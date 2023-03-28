import src.utils as u

from src.locators.locators_index import SidebarLocators
import src.pages.sidebar as sbar
import src.pages.homepage as hp
import src.pages.products as prod


@u.pytest.fixture
def driver():
    get_driver = u.setup_driver()
    yield get_driver
    get_driver.close()


def test_calculate_total_price(driver):
    """
    Side Bar - Cart - The total price is calculated correctly
    we need first few items in the cart
    VAT (Ma'am) in Israel is 17%
    :param driver:
    :return:
    """
    random_number = u.random.randint(1, 20)
    hp.click_on_random_item(driver)
    prod.insert_quantity(driver, random_number)

    vat_ils = 0.17
    u.sleep(1)

    meantime_sum_text = u.WDW(driver, 5).until(u.EC.visibility_of_element_located(SidebarLocators.sideloc['meantime_sum'])).text
    meantime_sum = float(u.filter_numbers(meantime_sum_text))

    distro_cost_text = u.WDW(driver, 5).until(u.EC.visibility_of_element_located(SidebarLocators.sideloc['distro_cost'])).text
    distro_cost = float(u.filter_numbers(distro_cost_text))

    vat_text = u.WDW(driver, 5).until(u.EC.visibility_of_element_located(SidebarLocators.sideloc['vat'])).text
    vat = float(u.filter_numbers(vat_text))

    total_sum_text = u.WDW(driver, 5).until(u.EC.visibility_of_element_located(SidebarLocators.sideloc['total_sum'])).text
    total_sum = float(u.filter_numbers(total_sum_text))

    assert round(vat) == round(meantime_sum * vat_ils)
    assert round(total_sum) == round(meantime_sum + vat + distro_cost)




def test_card_qna_link(driver):
    """
    Side Bar - Q&A - Clicking on "all question" button takes the user to the Q&A page
    :param driver:
    :return:
    """
    sbar.click_that(driver, 'card_qna')

    assert driver.current_url == 'https://qa.trado.co.il/questions'


def test_card_contact_link(driver):
    """
    Side Bar - Contact - Clicking on "Cotact" takes the user to contact page
    :param driver:
    :return:
    """
    sbar.click_that(driver, 'card_contact')

    assert driver.current_url == 'https://qa.trado.co.il/contact'


def test_card_shipment_link(driver):
    """
    Side Bar - Contact - Clicking on "Cotact" takes the user to contact page
    :param driver:
    :return:
    """
    sbar.click_that(driver, 'card_shipment')

    assert driver.current_url == 'https://qa.trado.co.il/shipment'


def test_quantity_change_from_sidebar(driver):
    """
    Side Bar - Cart - Qauntity can be changed by pressing the corresponding buttons
    Side Bar - Cart - Item can be removed by clicking on the bin icon
    :param driver:
    :return:
    """
    hp.click_on_random_item(driver)
    prod.click_quantity_add(driver)

    start_items_in_cart = sbar.get_cart_item_quantity(driver)
    sbar.click_that(driver, 'cart_item_add')
    u.sleep(1)
    current_items_in_cart = sbar.get_cart_item_quantity(driver)

    assert current_items_in_cart - start_items_in_cart == 1

    start_items_in_cart = sbar.get_cart_item_quantity(driver)
    sbar.click_that(driver, 'cart_item_subtract')
    u.sleep(1)
    current_items_in_cart = sbar.get_cart_item_quantity(driver)

    assert current_items_in_cart - start_items_in_cart == -1

    sbar.click_that(driver, 'cart_item_bin')
    assert sbar.get_cart_item_quantity(driver) == 0


def test_remove_all_items_from_cart(driver):
    """
    Side Bar - Cart - All items in the cart can be removed by clicking on the "deplete cart" button
    :param driver:
    :return:
    """
    for x in range(5):
        hp.click_specific_item(driver, u.random.randint(1, 10))
        prod.click_quantity_add(driver)
        driver.back()
        print(x)

    driver.execute_script('window.scrollTo(0,0)')

    sbar.click_that(driver, 'cart_item_deplete_all')
    items_in_cart = sbar.count_different_items_in_cart(driver)
    assert items_in_cart == 0