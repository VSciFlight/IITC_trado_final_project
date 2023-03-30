# Base Mechanism
import selenium
import requests

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait as WDW
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains

from src.locators.locators_index import HomePageLocators

# Databases
from src.db import db_gets_it as db_get

# additionals
import string
import random
from time import sleep

# testing methods
import pytest
# import allure

from selenium.common import exceptions as sel_except

url = 'https://qa.trado.co.il/'

def setup_driver(modal=False):
    url = 'https://qa.trado.co.il/'
    options = Options()
    options.add_argument("--disable-extensions")
    # options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.get(url)

    if modal:
        close_popup(driver)
    else:
        remove_annoying_popup(driver)

    return driver


def remove_annoying_popup(driver):
    WDW(driver, 5).until(EC.visibility_of_element_located(HomePageLocators.homeloc['popup_modal']))
    driver.execute_script("""
       var l = document.getElementsByClassName("modal_modalWrapper")[0];
       l.parentNode.removeChild(l);
    """)


def close_popup(driver):
    try:
        WDW(driver, 5).until(EC.visibility_of_element_located(HomePageLocators.homeloc['close_pop_up'])).click()

    except sel_except.TimeoutException:
        return


def click_somewhere_in_the_page(driver):
    driver.find_element(By.XPATH, '//html').click()


def rand_string(group=string.digits, n=10):
    """
    this function is taking a group of letters and then takes a number.
    it returns a string with random chars from the group in the length of the number  we provided
    :param group:
    :param n:
    :return:
    """
    return ''.join(random.choice(group) for i in range(n))


def filter_numbers(srt):
    """
    string in, numbers out
    filter text out, save only digits
    :param srt:
    :return:
    """
    flt = "".join([flt for flt in srt if flt.isdigit()])
    return int(flt)