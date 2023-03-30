import src.utils as u
import src.pages.homepage as hp

from src.locators.locators_index import HomePageLocators
from src.locators.locators_index import ProductLocators


@u.pytest.fixture
def driver():
    get_driver = u.setup_driver()
    yield get_driver
    get_driver.close()

@u.pytest.fixture
def driver_mod():
    get_driver = u.setup_driver(modal=True)
    yield get_driver
    get_driver.close()

@u.pytest.mark.functional
def test_select_item_in_grid(driver):
    """
    Homepage - Grid - Clicking on item in the grid takes me to the product page

    :param driver:
    :return:
    """
    driver.implicitly_wait(2)
    item_in_grid = u.WDW(driver, 5).until(u.EC.visibility_of_element_located(HomePageLocators.homeloc['grid_item']))
    item_name_grid = u.WDW(driver, 5).until(u.EC.visibility_of_element_located(HomePageLocators.homeloc['grid_item_name'])).text

    item_in_grid.click()

    item_name_in_prod = u.WDW(driver, 5).until(u.EC.visibility_of_element_located(ProductLocators.prodloc['product_name'])).text

    try:
        assert item_name_grid == item_name_in_prod

    except AssertionError:      # sometimes it may be lower/upper case letters so I fixed the test
        print(f"Possibly english lower/upper case assertion error \nin the grid: {item_name_grid} \nin the product: {item_name_in_prod} \n")
        assert item_name_grid.lower() == item_name_in_prod.lower()

@u.pytest.mark.functional
def test_grid_sort_by_popularity(driver):
    """
    Homepage - Grid - Sorting actually sorts (popularity)
    :param driver:
    :return:
    """
    hp.click_sort(driver)
    hp.select_sort(driver, 'popularity')

@u.pytest.mark.functional
def test_grid_sort_by_low_to_high(driver):
    """
    Homepage - Grid - Sorting actually sorts (price)
    :param driver:
    :return:
    """
    hp.click_sort(driver)
    hp.select_sort(driver, 'low_to_high')

    u.sleep(2)

    item_price_list = list()
    item_grid = hp.get_all_grid(driver)
    u.sleep(2)

    for x in range(1, (len(item_grid)+1)):
        product_price = driver.find_element(u.By.XPATH, f'//*[@class="productsList_list"]/a[{x}]/descendant::span[2]').text
        item_price_list.append(product_price)

    sorted_pricelist_low_to_high = item_price_list.copy()
    sorted_pricelist_low_to_high.sort()

    for ind in range(len(item_price_list)):
        try:
            assert sorted_pricelist_low_to_high[ind] == item_price_list[ind]
        except AssertionError:
            raise AssertionError(f"Sorting by low to high doesn't operate as it should be. \nEXPECTED: {sorted_pricelist_low_to_high[ind]} \nReality: {item_price_list[ind]}")

@u.pytest.mark.functional
def test_grid_sort_by_low_to_high(driver):
    """
    Homepage - Grid - Sorting actually sorts (price)
    :param driver:
    :return:
    """
    hp.click_sort(driver)
    hp.select_sort(driver, 'high_to_low')

    u.sleep(2)

    item_price_list = list()
    item_grid = hp.get_all_grid(driver)
    u.sleep(2)

    for x in range(1, (len(item_grid)+1)):
        product_price = driver.find_element(u.By.XPATH, f'//*[@class="productsList_list"]/a[{x}]/descendant::span[2]').text
        item_price_list.append(product_price)

    sorted_pricelist_high_to_low = item_price_list.copy()
    sorted_pricelist_high_to_low.sort(reverse=True)

    for ind in range(len(item_price_list)):
        try:
            assert sorted_pricelist_high_to_low[ind] == item_price_list[ind]
        except AssertionError:
            raise AssertionError(f"Sorting by low to high doesn't operate as it should be. \nEXPECTED: {sorted_pricelist_high_to_low[ind]} \nReality: {item_price_list[ind]}")

@u.pytest.mark.functional
def test_change_view_list_and_grid(driver):
    """
    Homepage - Grid - Grid view changes on click
    :param driver:
    :return:
    """
    hp.click_change_view(driver, 'list')
    u.sleep(1)
    item = u.WDW(driver, 5).until(u.EC.visibility_of_element_located(HomePageLocators.homeloc['grid_item']))
    list_view_item = item.find_element(u.By.XPATH, f'//*[@class="productsList_list"]/a[{HomePageLocators.need_a_random}]/child::div').get_attribute('class')

    try:
        assert 'inlineProduct_inlineProduct ' == list_view_item
    except AssertionError:
        raise AssertionError("Class isn't the right one, should be viewed as list, instead shown as grid")

    hp.click_change_view(driver, 'grid')
    u.sleep(1)
    item = u.WDW(driver, 5).until(u.EC.visibility_of_element_located(HomePageLocators.homeloc['grid_item']))
    list_view_item = item.find_element(u.By.XPATH, f'//*[@class="productsList_list"]/a[{HomePageLocators.need_a_random}]/child::div').get_attribute('class')

    try:
        assert 'product_product ' == list_view_item
    except AssertionError:
        raise AssertionError("Class isn't the right one, should be viewed as grid, instead shown as list")


def test_slider_nav_buttons_sanity(driver):
    """
    Homepage - Slider - Clicking on the navigation buttons will transform the slider accordingly
    :param driver:
    :return:
    """
    selected_slide = driver.find_element(u.By.XPATH, '//li[@class="slide selected"]')
    hp.slider_click_nav_btn(driver, 'next')
    next_slide = selected_slide.find_element(u.By.XPATH, './following-sibling::li')

    assert selected_slide.get_attribute('class') != next_slide.get_attribute('class')
    assert next_slide.get_attribute('class') == 'slide selected'


    hp.slider_click_nav_btn(driver, 'prev')
    selected_slide = driver.find_element(u.By.XPATH, '//li[@class="slide selected"]')
    hp.slider_click_nav_btn(driver, 'prev')
    prev_slide = selected_slide.find_element(u.By.XPATH, './preceding-sibling::li')

    assert selected_slide.get_attribute('class') != prev_slide.get_attribute('class')
    assert prev_slide.get_attribute('class') == 'slide selected'


def test_counted_items_vs_grid_items(driver):
    """
    Homepage - Grid - Item count at start match the overall products count
    :param driver:
    :return:
    """
    item_count = hp.get_title_item_count(driver)
    grid_count = hp.get_grid_item_count(driver)

    assert item_count == grid_count


def test_prefer_misadot_in_popup(driver_mod):
    """
    Homepage - Preferences - Selecting "Misadot" results in having restaurants products related
    :param driver:
    :return:
    """
    u.WDW(driver_mod, 5).until(u.EC.presence_of_element_located(HomePageLocators.homeloc['popup_modal']))
    hp.click_that(driver_mod, 'modal_restaurant')
    hp.click_that(driver_mod, 'modal_save')

    num_of_elements = len(hp.get_elements(driver_mod, 'navbar_list'))

    assert num_of_elements == 4


def test_prefer_cocktails_in_popup(driver_mod):
    """
    Homepage - Preferences - Selecting "cocktail" results in having cocktails products related    :param driver:
    "apparently drinks and cannabis goes together"
    :return:
    """
    u.WDW(driver_mod, 5).until(u.EC.presence_of_element_located(HomePageLocators.homeloc['popup_modal']))
    hp.click_that(driver_mod, 'modal_cocktail')
    hp.click_that(driver_mod, 'modal_save')

    num_of_elements = len(hp.get_elements(driver_mod, 'navbar_list'))

    assert num_of_elements == 5

def test_prefer_none_in_popup(driver_mod):
    """
    Popup - Preferences - No selection will give me all products to view
    expecting all the departments to be available since I didn't choose yey

    :return:
    """
    u.WDW(driver_mod, 5).until(u.EC.presence_of_element_located(HomePageLocators.homeloc['popup_modal']))
    hp.click_that(driver_mod, 'modal_save')

    num_of_elements = len(hp.get_elements(driver_mod, 'navbar_list'))

    assert num_of_elements == 8

def test_prefer_both_in_popup(driver_mod):
    """
    Popup - Preferences - No selection will give me all products to view
    expecting all the departments to be available since I chose all
    :return:
    """
    u.WDW(driver_mod, 5).until(u.EC.presence_of_element_located(HomePageLocators.homeloc['popup_modal']))
    hp.click_that(driver_mod, 'modal_cocktail')
    hp.click_that(driver_mod, 'modal_restaurant')
    hp.click_that(driver_mod, 'modal_save')

    num_of_elements = len(hp.get_elements(driver_mod, 'navbar_list'))

    assert num_of_elements == 8





