import src.utils as u
from src.locators.locators_index import ContactLocators


def get_to_contact(driver):
    u.WDW(driver, 5).until(u.EC.visibility_of_element_located(ContactLocators.contloc['contact'])).click()

def fill_first_name(driver, nput):
    field = u.WDW(driver, 5).until(u.EC.visibility_of_element_located(ContactLocators.contloc['field_first_name']))
    field.send_keys(nput)

def fill_last_name(driver, nput):
    field = u.WDW(driver, 5).until(u.EC.visibility_of_element_located(ContactLocators.contloc['field_last_name']))
    field.send_keys(nput)

def fill_email(driver, nput):
    field = u.WDW(driver, 5).until(u.EC.visibility_of_element_located(ContactLocators.contloc['field_email']))
    field.send_keys(nput)

def fill_phone(driver, nput):
    field = u.WDW(driver, 5).until(u.EC.visibility_of_element_located(ContactLocators.contloc['field_phone']))
    field.send_keys(nput)

def fill_content(driver, nput):
    field = u.WDW(driver, 5).until(u.EC.visibility_of_element_located(ContactLocators.contloc['field_content']))
    field.send_keys(nput)


def send_form(driver):
    u.WDW(driver, 5).until(u.EC.visibility_of_element_located(ContactLocators.contloc['submit_btn'])).click()


def get_form_message(driver):
    msg = u.WDW(driver, 5).until(u.EC.visibility_of_element_located(ContactLocators.contloc['form_message'])).text
    return msg

def click_on_field(driver, field):
    u.WDW(driver, 5).until(u.EC.visibility_of_element_located(ContactLocators.contloc[field])).click()


def get_content_field_value(driver):
    xfield = u.WDW(driver, 5).until(u.EC.visibility_of_element_located(ContactLocators.contloc['field_content']))
    info = driver.execute_script('var val = document.querySelector("#contactForm > div:nth-child(1) > div:nth-child(5) > textarea");'
                                 'return val.value;')
    return info
