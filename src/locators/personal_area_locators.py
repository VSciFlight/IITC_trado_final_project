import src.utils as u

class PersonalLocators:

    persloc = dict()

    persloc['new_cc_btn'] = (u.By.XPATH, '//*[@class="userCardsList_addCardBtn"]')
    persloc['field_cc_number'] = (u.By.XPATH, '//*[@id="credit-card-input"]')
    persloc['field_id_number'] = (u.By.XPATH, '//*[@id="userId-input"]')
    persloc['field_expmonth'] = (u.By.XPATH, '//*[@id="expmonth"]')
    persloc['field_expyear'] = (u.By.XPATH, '//*[@id="expyear"]')
    persloc['field_cvv'] = (u.By.XPATH, '//*[@id="cvv"]')
    persloc['pay_btn'] = (u.By.XPATH, '//*[@id="btnSubmit"]')

    persloc['error_class'] = (u.By.XPATH, '//*[contains(@class,"errNot")]')
    persloc['credit_error'] = (u.By.XPATH, '//*[contains(@class,"errNot")]')


    persloc['iframe_yaad'] = (u.By.XPATH, '//iframe[@id="yaadFrame"]')
    persloc['iframe_error'] = (u.By.XPATH, '//div[@id="sub-frame-error"]')
