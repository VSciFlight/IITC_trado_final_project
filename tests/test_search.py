import src.utils as u

import src.pages.search as srch
import src.pages.homepage as hp
from src.locators.locators_index import SearchLocators
from src.locators.locators_index import ProductLocators

@u.pytest.fixture
def driver():
    get_driver = u.setup_driver()
    yield get_driver
    get_driver.close()


def test_search_existing_item(driver):
    """
    Search - Bar - Able to search the quried value
    :param driver:
    :return:
    """
    bar = u.WDW(driver, 5).until(u.EC.visibility_of_element_located(SearchLocators.searchloc['search_bar']))
    item_name = hp.get_random_item(driver)

    bar.click()
    bar.send_keys(item_name)

    driver.find_element(u.By.XPATH, '//html').click()
    u.sleep(2)
    bar.click()
    fnd = u.WDW(driver, 15).until(u.EC.visibility_of_element_located(SearchLocators.searchloc['found_object']))

    assert fnd



def test_search_item_with_its_id(driver):
    """
    Search - Bar - Able to find product with its id
    :param driver:
    :return:
    """
    bar = u.WDW(driver, 5).until(u.EC.visibility_of_element_located(SearchLocators.searchloc['search_bar']))
    item = hp.click_on_random_item(driver)
    item_id_ext = u.WDW(driver, 5).until(u.EC.visibility_of_element_located(ProductLocators.prodloc['product_id'])).text
    item_name = u.WDW(driver, 5).until(u.EC.visibility_of_element_located(ProductLocators.prodloc['product_name'])).text

    item_id = [s for s in item_id_ext.split() if s.isdigit()]

    bar.click()
    bar.send_keys(item_id)

    u.click_somewhere_in_the_page(driver)
    u.sleep(2)
    bar.click()
    fnd = u.WDW(driver, 15).until(u.EC.visibility_of_element_located(SearchLocators.searchloc['found_object']))
    fnd_name = u.WDW(driver, 15).until(u.EC.visibility_of_element_located(SearchLocators.searchloc['found_object_name'])).text

    assert fnd
    assert item_name == fnd_name


def test_search_non_existing_product(driver):
    query = 'אבק'

    bar = u.WDW(driver, 5).until(u.EC.visibility_of_element_located(SearchLocators.searchloc['search_bar']))
    bar.click()
    bar.send_keys(query)

    driver.find_element(u.By.XPATH, '//html').click()
    u.sleep(2)
    bar.click()

    fnd_count = u.WDW(driver, 5).until(u.EC.visibility_of_element_located(SearchLocators.searchloc['count_results'])).text
    assert '0' in fnd_count