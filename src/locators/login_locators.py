import src.utils as u

class LoginLocators:

    logloc = dict()

    logloc['header_login'] = (u.By.XPATH, '//*[@class="header_userAreaLink"]')
    logloc['alternative_login'] = (u.By.XPATH, '//*[@class="verticalMenu_addProduct"]')

    logloc['login_btn'] = (u.By.XPATH, '//input[@value="התחברות"]')
    logloc['logout_btn'] = (u.By.XPATH, '//*[@class="header_logOut"]')

    logloc['login_phone'] = (u.By.XPATH, '//*[@label="מס׳ הטלפון שלך"]')
    logloc['login_remember_me'] = (u.By.XPATH, '//*[@class="login_login"]/descendant::span[@class=" checkbox_checkbox "]')
    logloc['code_cells'] = (u.By.XPATH, '//*[@class="form_loginCode"]/descendant::input')
    logloc['code_verify'] = (u.By.XPATH, '//*[@value="בצע אימות"]')

    logloc['personal'] = (u.By.XPATH, '//*[@class="header_userAreaLink"]/descendant::span[1]')