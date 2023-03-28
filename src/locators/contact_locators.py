import src.utils as u


class ContactLocators:

    contloc = dict()

    contloc['field_first_name'] = (u.By.XPATH, '//input[@label="first name"]')
    contloc['field_last_name'] = (u.By.XPATH, '//input[@label="last name"]')
    contloc['field_email'] = (u.By.XPATH, '//input[@label="email"]')
    contloc['field_phone'] = (u.By.XPATH, '//input[@label="phone"]')
    contloc['field_content'] = (u.By.XPATH, '//textarea[@label="Content Referral"]')

    contloc['submit_btn'] = (u.By.XPATH, '//*[@class="form_submitBtn"]')
    contloc['form_message'] = (u.By.XPATH, '//*[@class="form_message"]')


    contloc['contact'] = (u.By.XPATH, '//*[text()="צור קשר"]')