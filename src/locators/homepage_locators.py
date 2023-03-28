import random

import src.utils as u

class HomePageLocators:

    need_a_random = random.randint(1, 10)
    homeloc = dict()

    homeloc['popup_modal'] = (u.By.XPATH, '//*[contains(@class, "modal_modalWrapper")]')
    homeloc['close_pop_up'] = (u.By.XPATH, '//*[@id="root"]/div/div[4]/div/span/i')

    homeloc['slider_next'] = (u.By.XPATH, '//*[@class="control-arrow control-next"]')
    homeloc['slider_prev'] = (u.By.XPATH, '//*[@class="control-arrow control-prev"]')
    homeloc['selected_slide'] = (u.By.XPATH, '//li[@class="slide selected"]')
    homeloc['all_slides'] = (u.By.XPATH, '//li[contains(@class,"slide")]')

    homeloc['grid_count_items'] = (u.By.XPATH, '//*[@class="productsList_title"]/span')
    homeloc['grid_items_collection'] = (u.By.XPATH, '//*[@class="productsList_list"]/a')
    homeloc['grid_item'] = (u.By.XPATH, f'//*[@class="productsList_list"]/a[{need_a_random}]')
    homeloc['grid_item_name'] = (u.By.XPATH, f'//*[@class="productsList_list"]/a[{need_a_random}]/div/div[2]/div[2]/div[1]')
    homeloc['grid_item_price'] = (u.By.XPATH, f'//*[@class="productsList_list"]/a[{need_a_random}]/descendant::span[@class="productPrice_price"]/span')

    homeloc['grid_sort'] = (u.By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div/div/div[2]/div/div[2]/div[2]/div[3]/div/select')
    homeloc['grid_sort_popular'] = (u.By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div/div/div[2]/div/div[2]/div[2]/div[3]/div/select/option[1]')
    homeloc['grid_sort_low_to_high'] = (u.By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div/div/div[2]/div/div[2]/div[2]/div[3]/div/select/option[2]')
    homeloc['grid_sort_high_to_low'] = (u.By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div/div/div[2]/div/div[2]/div[2]/div[3]/div/select/option[3]')

    homeloc['list_view'] = (u.By.XPATH, '//*[@class="micon-lines-o icon_icon "]')
    homeloc['grid_view'] = (u.By.XPATH, '//*[@class="micon-squares-o icon_icon "]')


