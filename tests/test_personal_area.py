import src.utils as u
import src.pages.personal_area as pers

from src.locators.locators_index import PersonalLocators


@u.pytest.fixture
def driver():
    get_driver = u.setup_driver(modal=True)
    yield get_driver
    get_driver.close()



def test_get_to_personal_area(driver):
    """
    :param driver:
    :return:
    """

    pers.get_to_personal_area(driver)
    assert driver.current_url == 'https://qa.trado.co.il/user/personalArea'

