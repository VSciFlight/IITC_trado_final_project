import src.utils as u

class RegisterLocators:

    regloc = dict()

    regloc['register_tab'] = (u.By.XPATH, '//*[text()="הרשם"]')
    regloc['phone'] = (u.By.XPATH, '//*[@label="מס׳ הטלפון שלך"]')
    regloc['business_number'] = (u.By.XPATH, '//*[@label="ח.פ"]')
    regloc['approve_policy'] = (u.By.XPATH, '//*[@class="form_items"]/child::div[3]')
    regloc['newsletter_regis'] = (u.By.XPATH, '//*[@class="form_items"]/child::div[4]')
    regloc['submit_btn'] = (u.By.XPATH, '//*[@class="form_submitBtn"]')

    regloc['code_cells'] = (u.By.XPATH, '//*[@class="form_loginCode"]/descendant::input')
    regloc['code_verify'] = (u.By.XPATH, '//*[@value="בצע אימות"]')
