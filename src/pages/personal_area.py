import src.utils as u
from src.locators.locators_index import PersonalLocators

import src.pages.login as lg



def get_to_personal_area(driver):
    lg.just_login_in_one_line_code(driver, '0500000000')
    lg.click_that(driver, 'personal')


