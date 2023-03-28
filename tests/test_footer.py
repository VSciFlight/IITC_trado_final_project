import src.utils as u

import src.pages.footer as ft
from src.locators.locators_index import FooterLocators


@u.pytest.fixture
def driver():
    get_driver = u.setup_driver()
    yield get_driver
    get_driver.close()


def test_click_additional_information(driver):
    """
    Footer - Addionals - Clicking the link will deliver me to the corresponding pages
    :param driver:
    :return:
    """
    adds_footer = u.WDW(driver, 5).until(u.EC.visibility_of_all_elements_located(FooterLocators.footloc['additionals_list']))
    qa_trado = driver.current_window_handle
    for x in range(len(adds_footer)):
        link = adds_footer[x].get_attribute('href')
        adds_footer[x].click()

        if "max.co.il" in link:
            u.WDW(driver, 5).until(u.EC.number_of_windows_to_be(2))
            print(driver.title)
            max_window = driver.current_window_handle
            driver.switch_to.window(max_window)
            print(driver.title)
            assert link == driver.current_url
            driver.close()

        else:
            assert link == driver.current_url
            driver.back()


def test_click_stay_in_touch(driver):
    """
    Footer - Stay In Touch - Clicking the link will deliver me to the corresponding pages
    :param driver:
    :return:
    """
    adds_footer = u.WDW(driver, 5).until(u.EC.visibility_of_all_elements_located(FooterLocators.footloc['stay_in_touch_links']))

    for x in range(len(adds_footer)):
        link = adds_footer[x].get_attribute('href')
        adds_footer[x].click()

        assert link == driver.current_url


def test_click_importants(driver):
    """
    Footer - Stay In Touch - Clicking the link will deliver me to the corresponding pages
    :param driver:
    :return:
    """
    adds_footer = u.WDW(driver, 5).until(u.EC.visibility_of_all_elements_located(FooterLocators.footloc['importants_links']))

    for x in range(len(adds_footer)):
        link = adds_footer[x].get_attribute('href')
        adds_footer[x].click()

        assert link == driver.current_url


def test_click_others_bottom_links(driver):
    """
    Footer - Bottom - Clicking the link will deliver me to the corresponding pages
    :param driver:
    :return:
    """
    adds_footer = u.WDW(driver, 5).until(u.EC.visibility_of_all_elements_located(FooterLocators.footloc['other_bottom_links']))

    for x in range(len(adds_footer)):
        link = adds_footer[x].get_attribute('href')
        directed_page = adds_footer[x].text
        adds_footer[x].click()

        u.sleep(5)
        headline_page = u.WDW(driver, 30).until(u.EC.visibility_of_element_located(FooterLocators.footloc['headline_for_others'])).text

        assert link == driver.current_url
        assert headline_page in directed_page




