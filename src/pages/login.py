import src.utils as u
from src.locators.locators_index import LoginLocators


def click_login(driver):
    # u.WDW(driver, 5).until(u.EC.visibility_of_element_located(LoginLocators.logloc['header_login'])).click()
    u.WDW(driver, 5).until(u.EC.visibility_of_element_located(LoginLocators.logloc['alternative_login'])).click()


def fill_login_info(driver, phone='0500000000'):
    u.WDW(driver, 5).until(u.EC.visibility_of_element_located(LoginLocators.logloc['login_phone'])).send_keys(phone)


def click_modal_login(driver):
    u.WDW(driver, 5).until(u.EC.visibility_of_element_located(LoginLocators.logloc['login_btn'])).click()


def insert_code_into_cells(driver, phone='0500000000'):

    cells = u.WDW(driver, 5).until(u.EC.visibility_of_all_elements_located(LoginLocators.logloc['code_cells']))
    login_code = str(u.db_get.get_login_code_from_db(phone))

    for i in range(5):
        cells[i].send_keys(login_code[i])


def click_verify_button(driver):
    u.WDW(driver, 5).until(u.EC.visibility_of_element_located(LoginLocators.logloc['code_verify'])).click()


def get_login_indication(driver):
    indic = u.WDW(driver, 5).until(u.EC.visibility_of_element_located(LoginLocators.logloc['personal'])).text
    return indic


def just_login_in_one_line_code(driver, phone, remember_me=False):
    click_login(driver)
    fill_login_info(driver, phone)
    if remember_me:
        click_that(driver, 'login_remember_me')

    click_that(driver, 'login_btn')
    insert_code_into_cells(driver, phone)
    click_verify_button(driver)


def click_that(driver, location):
    u.WDW(driver, 5).until(u.EC.visibility_of_element_located(LoginLocators.logloc[location])).click()


def get_element_logout_button(driver):
    elem = driver.find_element(u.By.XPATH, '//*[@class="header_logOut"]')
    return elem


def just_logout_man(driver):
    logout_element = get_element_logout_button(driver)
    action = u.ActionChains(driver)
    action.move_to_element(logout_element)
    action.click(logout_element)
    action.perform()