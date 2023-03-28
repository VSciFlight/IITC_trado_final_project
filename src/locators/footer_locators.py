import src.utils as u

class FooterLocators:

    footloc = dict()

    footloc['importants_links'] = (u.By.XPATH, '//*[@class="footer_footerWrapper "]/descendant::div[2]/a')
    footloc['additionals_list'] = (u.By.XPATH, '//*[@class="footer_footerWrapper "]/descendant::div[3]/a')
    footloc['stay_in_touch_links'] = (u.By.XPATH, '//*[@class="footer_footerWrapper "]/descendant::div[4]/a')
    footloc['other_bottom_links'] = (u.By.XPATH, '//*[@class="footer_footerWrapper "]/descendant::div[7]/a')

    footloc['headline_for_others'] = (u.By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div/div[1]/h1')

