
import src.utils as u
from src.locators.locators_index import HomePageLocators


## HOME PAGE FUNCTIONS

def click_sort(driver):
    u.WDW(driver, 5).until(u.EC.visibility_of_element_located(HomePageLocators.homeloc['grid_sort'])).click()


def select_sort(driver, method=1):
    if method == "popular":
        u.WDW(driver, 5).until(u.EC.visibility_of_element_located(HomePageLocators.homeloc['grid_sort_popular'])).click()
    elif method == "low_to_high":
        u.WDW(driver, 5).until(u.EC.visibility_of_element_located(HomePageLocators.homeloc['grid_sort_low_to_high'])).click()
    elif method == "high_to_low":
        u.WDW(driver, 5).until(u.EC.visibility_of_element_located(HomePageLocators.homeloc['grid_sort_high_to_low'])).click()

    click_sort(driver)


def get_all_grid(driver):
    u.WDW(driver, 40).until(u.EC.visibility_of_all_elements_located(HomePageLocators.homeloc['grid_items_collection']))
    item_grid = driver.find_elements(u.By.XPATH, '//*[@class="productsList_list"]/a')
    return item_grid


def click_change_view(driver, des_view='grid'):
    if des_view == 'grid':
        u.WDW(driver, 5).until(u.EC.visibility_of_element_located(HomePageLocators.homeloc['grid_view'])).click()
    elif des_view == 'list':
        u.WDW(driver, 5).until(u.EC.visibility_of_element_located(HomePageLocators.homeloc['list_view'])).click()


def slider_click_nav_btn(driver, side):
    if side == 'prev':
        u.WDW(driver, 5).until(u.EC.visibility_of_element_located(HomePageLocators.homeloc['slider_prev'])).click()
    elif side == 'next':
        u.WDW(driver, 5).until(u.EC.visibility_of_element_located(HomePageLocators.homeloc['slider_next'])).click()


def get_random_item(driver):
    item = u.WDW(driver, 5).until(u.EC.visibility_of_element_located(HomePageLocators.homeloc['grid_item_name'])).text
    return item


def click_specific_item(driver, num):
    u.WDW(driver, 5).until(u.EC.visibility_of_element_located((u.By.XPATH, f'//*[@class="productsList_list"]/a[{num}]'))).click()


def click_on_random_item(driver):
    u.WDW(driver, 5).until(u.EC.visibility_of_element_located(HomePageLocators.homeloc['grid_item'])).click()


def get_product_price(driver):
    price = u.WDW(driver, 5).until(u.EC.visibility_of_element_located(HomePageLocators.homeloc['grid_item_price']))
    return price.text


def get_title_item_count(driver):
    count = u.WDW(driver, 5).until(u.EC.visibility_of_element_located(HomePageLocators.homeloc['grid_count_items'])).text
    count_num = u.filter_numbers(count)
    return count_num


def get_grid_item_count(driver):
    items = u.WDW(driver, 5).until(u.EC.visibility_of_all_elements_located(HomePageLocators.homeloc['grid_items_collection']))
    return len(items)


def click_that(driver, location):
    u.WDW(driver, 5).until(u.EC.visibility_of_element_located(HomePageLocators.homeloc[location])).click()


def get_elements(driver, location):
    try:
        elems = u.WDW(driver, 5).until(u.EC.visibility_of_all_elements_located(HomePageLocators.homeloc[location]))
        return elems
    except u.sel_except.TimeoutException:
        print("No categories were found")
        return 0