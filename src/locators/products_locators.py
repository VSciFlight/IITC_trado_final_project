import src.utils as u

class ProductLocators:

    prodloc = dict()

    prodloc['product_name'] = (u.By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div[1]/div/div[1]/div[2]/div[1]/h1')
    prodloc['product_id'] = (u.By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div[1]/div/div/div[1]/div[2]')
    prodloc['product_price'] = (u.By.XPATH, '//*[@class="fullProduct_productsHedaer"]/descendant::*[@class="productPrice_price"]')
    prodloc['product_card_stock'] = (u.By.XPATH, '//*[@class="fullProduct_infoCard"][1]')
    prodloc['product_quantity'] = (u.By.XPATH, '//*[@class="fullProduct_productsHedaer"]/descendant::input')
    prodloc['product_quantity_add'] = (u.By.XPATH, '//*[@class="fullProduct_productsHedaer"]/descendant::*[@class="micon-plus icon_icon "]')
    prodloc['product_quantity_subtract'] = (u.By.XPATH, '//*[@class="fullProduct_productsHedaer"]/descendant::*[@class="micon-minus icon_icon "]')
    prodloc['product_min_quantity_order'] = (u.By.XPATH, '//*[@class="fullProduct_infoCard_container"]/preceding-sibling::span')

    prodloc['detailed_stock'] = (u.By.XPATH, '//*[@class="fullProduct_infoRow "]/label[text()="כמות במלאי"]/following-sibling::span')

    prodloc['error_404_message'] = (u.By.XPATH, '//*[contains(text(), "404")]')

