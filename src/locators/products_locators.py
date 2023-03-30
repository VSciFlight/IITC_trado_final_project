import src.utils as u

class ProductLocators:

    prodloc = dict()

    prodloc['product_name'] = (u.By.XPATH, '//*[@class="fullProduct_productsHedaer"]/descendant::h1')
    prodloc['product_id'] = (u.By.XPATH, '//*[@class="fullProduct_imageW"]/child::div[2]')
    prodloc['product_price'] = (u.By.XPATH, '//*[@class="fullProduct_productsHedaer"]/descendant::*[@class="productPrice_price"]')
    prodloc['product_card_stock'] = (u.By.XPATH, '//*[@class="fullProduct_infoCard"][1]')

    prodloc['product_quantity'] = (u.By.XPATH, '//*[@class="fullProduct_productsHedaer"]/descendant::input')
    prodloc['product_quantity_add'] = (u.By.XPATH, '//*[@class="fullProduct_productsHedaer"]/descendant::*[@class="micon-plus icon_icon "]')
    prodloc['product_quantity_subtract'] = (u.By.XPATH, '//*[@class="fullProduct_productsHedaer"]/descendant::*[@class="micon-minus icon_icon "]')
    prodloc['product_min_quantity_order'] = (u.By.XPATH, '//*[@class="fullProduct_infoCard_container"]/preceding-sibling::span')

    prodloc['detailed_stock'] = (u.By.XPATH, '//*[@class="fullProduct_infoRow "]/label[text()="כמות במלאי"]/following-sibling::span')

    prodloc['error_404_message'] = (u.By.XPATH, '//*[contains(text(), "404")]')

    prodloc['suggested_items_list'] = (u.By.XPATH, '//*[@class="fullProduct_bottom"]/descendant::div[@class="productDesc_name"]')


    # Add new product

    prodloc['head_details'] = (u.By.XPATH, '//*[@class="orderTimeline_time   "][]')
    prodloc['head_quantity'] = (u.By.XPATH, '//*[@class="orderTimeline_time   "]')
    prodloc['head_delivery'] = (u.By.XPATH, '//*[@class="orderTimeline_time   "]')
    prodloc['head_progress'] = (u.By.XPATH, '//*[@class="orderTimeline_time orderTimeline_current  "]')

    prodloc['add_new_product'] = (u.By.XPATH, '//*[@class="verticalMenu_addProduct"]')
    prodloc['field_barcode'] = (u.By.XPATH, '//*[@label="מק״ט יצרן"]')
    prodloc['field_name'] = (u.By.XPATH, '//*[@label="שם המוצר"]')
    prodloc['field_country'] = (u.By.XPATH, '//*[@label="מדינה"]')
    prodloc['field_manufacturer'] = (u.By.XPATH, '//*[@label="manufacturer"]')
    prodloc['field_brand'] = (u.By.XPATH, '//*[@label="brand"]')
    prodloc['field_expirationDate'] = (u.By.XPATH, '//*[@label="expirationDate"]')
    prodloc['field_price'] = (u.By.XPATH, '//*[@label="price"]')
    prodloc['field_add_product'] = (u.By.XPATH, '//*[@class="form_submitBtn"]')

    prodloc['option_israel'] = (u.By.XPATH, '//*[@value="Israel"]')
    prodloc['option_other'] = (u.By.XPATH, '//*[@value="Other"]')

    prodloc['amount_in_carton'] = (u.By.XPATH, '//*[@label="כמות בקרטון2"]')
    prodloc['carton_stock'] = (u.By.XPATH, '//*[@label="מספר קרטונים במלאי"]')
    prodloc['min_for_order'] = (u.By.XPATH, '//*[@label="מינימום קרטונים בהזמנה"]')

    prodloc['product_ready_in_days'] = (u.By.XPATH, '//*[@class="productBtn_amount"]/input')
    prodloc['location_city'] = (u.By.XPATH, '//*[@label="city"]')
    prodloc['location_street'] = (u.By.XPATH, '//*[@label="street"]')
    prodloc['location_number'] = (u.By.XPATH, '//*[@label="number"]')
    prodloc['location_entrance'] = (u.By.XPATH, '//*[@label="entrance"]')
    prodloc['location_notes'] = (u.By.XPATH, '//*[@label="הערות"]')
    prodloc['location_floor'] = (u.By.XPATH, '//*[@label="floor"]')
    prodloc['location_contact'] = (u.By.XPATH, '//*[@label="שם איש קשר"]')
    prodloc['location_phone'] = (u.By.XPATH, '//*[@label="טלפון"]')


    prodloc['product_added_successfully'] = (u.By.XPATH, '//*[text()="מוצר התווסף בהצלחה"]')
