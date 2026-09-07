from playwright.sync_api import expect
from config.settings import Settings
from data.login_data import LoginExpected
from data.login_data import(INVALID_LOGIN_DATA, LoginExpected)

import pytest


@pytest.mark.smoke
@pytest.mark.regression
def test_login_positive(
    login_page,
    products_page,
    credentials
):
    
    login_page.open_login_page()
    
    login_page.login(
        credentials["email"],
        credentials["password"]
    )
    
    expect(products_page.page).to_have_url(Settings.PRODUCTS_URL)
    
    expect(products_page.user_email).to_have_text(LoginExpected.USERNAME)
    
    expect(products_page.products_title).to_have_text(LoginExpected.PRODUCTS_TITLE)


@pytest.mark.negative
@pytest.mark.regression

@pytest.mark.parametrize("email,password, error_message",
    INVALID_LOGIN_DATA
)

def test_login_negative(
    login_page,
    credentials,
    email,
    password,
    error_message
):
    
    login_page.open_login_page()
    
    login_page.login(
        credentials["email"],
        "salah"
    )
    
    expect(login_page.page).to_have_url(Settings.LOGIN_URL)
    
    expect(login_page.login_error).to_have_text(LoginExpected.INVALID_CREDENTIALS)
    
