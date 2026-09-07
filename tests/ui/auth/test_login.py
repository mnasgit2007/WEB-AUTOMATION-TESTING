from playwright.sync_api import expect
from config.settings import Settings
from data.login_data import LoginExpected

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
    
    