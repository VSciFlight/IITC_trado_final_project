import pytest

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")


@pytest.fixture
def get_browser(request):
    print("get_browser was called")
    _browser = request.config.getoption("--browser")
    return _browser
