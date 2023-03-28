import src.utils as u
class SearchLocators:

    searchloc = dict()

    searchloc['search_bar'] = (u.By.XPATH, '//input[@class="mainSearch_search"]')
    searchloc['search_bar_results'] = (u.By.XPATH, '//div[@class="mainSearch_results"]')
    searchloc['found_object'] = (u.By.XPATH, '//div[@class="mainSearch_results"]/descendant::div[contains(@class,"inlineProduct_inlineProduct ")]')
    searchloc['found_object_name'] = (u.By.XPATH, '//*[@class="mainSearch_results"]/descendant::*[@class="productDesc_name"]')
    searchloc['count_results'] = (u.By.XPATH, '//*[@class="mainSearch_results"]/child::h3')