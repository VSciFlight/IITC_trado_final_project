import src.utils as u

import src.pages.login as lg
import src.pages.products as prod
from src.locators.locators_index import LoginLocators


@u.pytest.fixture
def driver():
    get_driver = u.setup_driver(modal=True)
    yield get_driver
    get_driver.close()



@u.pytest.mark.functional
def test_valid_login(driver):
    """
    Users - Login - Valid login with existing account
    :param driver:
    :return:
    """

    phone = '0500000000'

    lg.click_login(driver)
    lg.fill_login_info(driver, phone)
    lg.click_modal_login(driver)

    u.sleep(2)
    lg.insert_code_into_cells(driver, phone)
    lg.click_verify_button(driver)

    u.sleep(2)
    u.close_popup(driver)
    header_indicator = lg.get_login_indication(driver)
    assert header_indicator == "אזור אישי"


@u.pytest.mark.functional
def test_logout(driver):
    """
    Users - Logout - Logout successfully, means I can log out the site
    :param driver:
    :return:
    """
    lg.just_login_in_one_line_code(driver, phone='0500000000')
    u.sleep(2)
    u.close_popup(driver)

    lg.just_logout_man(driver)
    # lg.click_that(driver, 'logout_btn')
    u.sleep(2)

    header_indicator = lg.get_login_indication(driver)
    assert header_indicator == "התחברות"


@u.pytest.mark.functional
def test_login_with_remember_me_logout(driver):
    """
    Users - Login - Login with "remember me", means I can logout properly and next time login without the need for verification
    :param driver:
    :return:
    """
    phone = '0500000000'
    lg.just_login_in_one_line_code(driver, phone, remember_me=True)

    u.sleep(1)
    u.close_popup(driver)
    lg.just_logout_man(driver)

    u.sleep(1)
    u.close_popup(driver)

    lg.click_login(driver)
    lg.fill_login_info(driver, phone)
    lg.click_modal_login(driver)

    u.sleep(1)
    u.close_popup(driver)
    header_indicator = lg.get_login_indication(driver)
    assert header_indicator == "אזור אישי"

@u.pytest.mark.functional
def test_login_with_remember_me_tab(driver):
    """
    Users - Login - Login with "remember me", means I can close the tab and re-enter again
    :param driver:
    :return:
    """
    phone = '0500000000'
    lg.just_login_in_one_line_code(driver, phone, remember_me=True)

    u.sleep(2)
    header_indicator = lg.get_login_indication(driver)
    assert header_indicator == "אזור אישי"

    driver.switch_to.new_window('tab')
    driver.get(u.url)

    u.sleep(1)
    u.close_popup(driver)
    header_indicator = lg.get_login_indication(driver)
    assert header_indicator == "אזור אישי"

@u.pytest.mark.functional
def test_login_with_remember_me_window(driver):
    """
    Users - Login - Login with "remember me", means I can open a window and login to my account easily
    :param driver:
    :return:
    """
    phone = '0500000000'
    lg.just_login_in_one_line_code(driver, phone, remember_me=True)

    u.sleep(2)
    header_indicator = lg.get_login_indication(driver)
    assert header_indicator == "אזור אישי"

    driver.switch_to.new_window('window')
    driver.get(u.url)

    u.sleep(2)
    u.close_popup(driver)
    header_indicator = lg.get_login_indication(driver)
    assert header_indicator == "אזור אישי"


@u.pytest.mark.skip(reason="couldn't find a way to test quitting browser and reopen it and still works, done manually though, it failed")
def test_login_with_remember_me_close_browser(driver):
    """
    Users - Login - Login with "remember me", means I can close the browser and re-enter again
    :param driver:
    :return:
    """
    phone = '0500000000'
    lg.just_login_in_one_line_code(driver, phone, remember_me=True)

    u.sleep(2)
    header_indicator = lg.get_login_indication(driver)
    assert header_indicator == "אזור אישי"

    driver.quit()
    u.sleep(1)
    u.setup_driver()

    u.sleep(1)
    u.close_popup(driver)
    header_indicator = lg.get_login_indication(driver)
    assert header_indicator == "אזור אישי"



def test_add_new_product(driver):
    """
    Users - Store - Add new product
    :param driver:
    :return:
    """
    random_num = u.random.randint(1, 200)
    phone = '0500000000'
    product_name = 'Deluxe_Toilet_Paper_' + str(random_num)
    print(product_name)

    lg.just_login_in_one_line_code(driver, phone)
    prod.click_that(driver, 'add_new_product')
    u.sleep(1)

    prod.fill_this_field(driver, 'field_barcode', u.rand_string())
    prod.fill_this_field(driver, 'field_name', product_name)

    prod.click_that(driver, 'field_country')
    prod.click_that(driver, 'option_israel')

    prod.fill_this_field(driver, 'field_manufacturer', 'Dunder Mifflin Ltd.')
    prod.fill_this_field(driver, 'field_brand', 'Deluxe Paper')
    prod.fill_this_field(driver, 'field_expirationDate', '2023-04-03')
    prod.fill_this_field(driver, 'field_price', u.rand_string(n=3))

    prod.click_that(driver, 'field_add_product')

    u.sleep(1)

    prod.fill_this_field(driver, 'amount_in_carton', '10')
    prod.fill_this_field(driver, 'carton_stock', f'{random_num}')
    prod.fill_this_field(driver, 'min_for_order', '1')
    prod.click_that(driver, 'field_add_product')

    prod.fill_this_field(driver, 'product_ready_in_days', '6')
    prod.fill_this_field(driver, 'location_city', 'רמת גן')
    prod.fill_this_field(driver, 'location_street', 'החילזון')
    prod.fill_this_field(driver, 'location_number', '6')    # should be numbers only
    prod.fill_this_field(driver, 'location_entrance', 'ב')      # placeholder in english though the site in Hebrew
    prod.fill_this_field(driver, 'location_notes', 'תביא פנקייקים ותחייך')  # for some reason it is required
    prod.fill_this_field(driver, 'location_floor', '2')
    prod.fill_this_field(driver, 'location_contact', 'אוסטאו סטריגה')
    prod.fill_this_field(driver, 'location_phone', phone)
    prod.click_that(driver, 'field_add_product')

    # Expecting it will take me to "Delivery"
    headers_prog = prod.get_elements(driver, 'head_progress')
    # try:
    #     assert len(headers_prog) == 3
    #
    # except AssertionError:
    #     print("No Delivery Step")

    prod_added_message = prod.get_element(driver, 'product_added_successfully')
    assert prod_added_message.text == 'מוצר התווסף בהצלחה'

    try:
        u.sleep(2)
        prod_in_db = u.db_get.get_value('products', 'name', product_name)
        assert str(prod_in_db) == str(product_name)

    except:
        raise AssertionError("Item was not found/uploaded to the database")

    lg.click_that(driver, 'personal')
    u.sleep(2)

    try:
        u.WDW(driver, 5).until(u.EC.visibility_of_element_located((u.By.XPATH, f'//*[@class="userProducts_list"]/*[text()="{product_name}"]')))

    except u.sel_except.TimeoutException:
        raise u.sel_except.TimeoutException("Item cannot be found in the uploaded items")





