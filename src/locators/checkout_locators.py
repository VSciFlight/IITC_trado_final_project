import src.utils as u


class CheckoutLocators:

    chkloc = dict()

    chkloc['store_name'] = (u.By.XPATH, '//*[@name="store"]')
    chkloc['store_bn'] = (u.By.XPATH, '//*[@name="userId"]')
    chkloc['store_email'] = (u.By.XPATH, '//*[@name="email"]')
    chkloc['store_city'] = (u.By.XPATH, '//*[@class="checkout-form_checkoutUserForm"]/section[1]/descendant::*[@name="address.city"]')
    chkloc['store_street'] = (u.By.XPATH, '//*[@class="checkout-form_checkoutUserForm"]/section[1]/descendant::*[@name="address.street"]')
    chkloc['store_house_number'] = (u.By.XPATH, '//*[@class="checkout-form_checkoutUserForm"]/section[1]/descendant::*[@name="address.building"]')
    chkloc['store_entrance'] = (u.By.XPATH, '//*[@class="checkout-form_checkoutUserForm"]/section[1]/descendant::*[@name="address.entrance"]')
    chkloc['store_floor'] = (u.By.XPATH, '//*[@class="checkout-form_checkoutUserForm"]/section[1]/descendant::*[@name="address.floor"]')

    chkloc['delivery_city'] = (u.By.XPATH, '//*[@class="checkout-form_checkoutUserForm"]/section[2]/descendant::*[@name="address.city"]')
    chkloc['delivery_street'] = (u.By.XPATH, '//*[@class="checkout-form_checkoutUserForm"]/section[2]/descendant::*[@name="address.street"]')
    chkloc['delivery_house_number'] = (u.By.XPATH, '//*[@class="checkout-form_checkoutUserForm"]/section[2]/descendant::*[@name="address.building"]')
    chkloc['delivery_entrance'] = (u.By.XPATH, '//*[@class="checkout-form_checkoutUserForm"]/section[2]/descendant::*[@name="address.entrance"]')
    chkloc['delivery_floor'] = (u.By.XPATH, '//*[@class="checkout-form_checkoutUserForm"]/section[2]/descendant::*[@name="address.floor"]')
    chkloc['delivery_contact'] = (u.By.XPATH, '//*[@name="contactName"]')
    chkloc['delivery_firstname'] = (u.By.XPATH, '//*[@name="firstName"]')
    chkloc['delivery_lastname'] = (u.By.XPATH, '//*[@name="lastName"]')
    chkloc['delivery_phone'] = (u.By.XPATH, '//*[@name="phone"]')

    chkloc['submit_order_btn'] = (u.By.XPATH, '//*[@class="checkout-form_submitBtn"]')