import pytest

from config.settings import Settings
from pages.login_page import LoginPage
from pages.products_page import ProductPage


@pytest.fixture
def credentials():
    
    return{
        "email": Settings.TEST_EMAIL,
        "password": Settings.TEST_PASSWORD
    }

@pytest.fixture
def login_page(page):
    
    return LoginPage(page)

@pytest.fixture
def products_page(page):
    
    return ProductPage(page)