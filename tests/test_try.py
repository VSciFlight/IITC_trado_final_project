import pytest

@pytest.fixture
def setup():
    print("HELLO")


@pytest.mark.probability
def test_add(setup):
    assert 3 == 1 + 2


@pytest.mark.sanity
def test_prod(setup):
    assert 2 == 1 * 2