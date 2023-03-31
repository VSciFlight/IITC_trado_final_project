import src.utils as u

class SidebarLocators:

    sideloc = dict()


    sideloc['cart_item_row'] = (u.By.XPATH, '//*[@class="inlineProduct_inlineProduct inlineProduct_inlineProductforCart "]/parent::a')
    sideloc['cart_item_quantity'] = (u.By.XPATH, '//*[@class="inlineProduct_inlineProduct inlineProduct_inlineProductforCart "]/descendant::input')
    sideloc['cart_item_add'] = (u.By.XPATH, '//*[@class="cart_list cart_list_fullProduct"]/descendant::*[@class="micon-plus icon_icon "]')
    sideloc['cart_item_subtract'] = (u.By.XPATH, '//*[@class="cart_list cart_list_fullProduct"]/descendant::*[@class="micon-minus icon_icon "]')
    sideloc['cart_item_bin'] = (u.By.XPATH, '//*[@class="cart_list cart_list_fullProduct"]/descendant::div[@class="inlineProduct_svg"]')
    sideloc['cart_item_deplete_all'] = (u.By.XPATH, '//*[@class="cart_clearCart"]')

    sideloc['meantime_sum'] = (u.By.XPATH, '//*[@class="cart_prices"]/child::h6[1]/span[2]')
    sideloc['distro_cost'] = (u.By.XPATH, '//*[@class="cart_prices"]/child::h6[2]/span[2]')
    sideloc['vat'] = (u.By.XPATH, '//*[@class="cart_prices"]/child::h6[3]/span[2]')
    sideloc['total_sum'] = (u.By.XPATH, '//*[@class="cart_prices"]/child::h6[4]/span[2]')
    sideloc['checkout'] = (u.By.XPATH, '//*[@class="cart_footer cart_footer_fullProduct"]/descendant::button')

    sideloc['card_qna'] = (u.By.XPATH, '//*[@class="cardInfo_cardInfo"][1]/div/a')
    sideloc['card_contact'] = (u.By.XPATH, '//*[@class="cardInfo_cardInfo"][2]/div/a')
    sideloc['card_shipment'] = (u.By.XPATH, '//*[@class="cardInfo_cardInfo"][3]/div/a')


