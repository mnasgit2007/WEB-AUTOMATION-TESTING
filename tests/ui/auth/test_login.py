import pytest
import allure

from playwright.sync_api import expect
from config.settings import Settings
from data.login_data import LoginExpected
from data.login_data import(INVALID_LOGIN_DATA, LoginExpected)


# ==============================================================
# POSITIVE LOGIN
# ==============================================================

@allure.feature("Login")
@allure.story("Positive Login")
@allure.title("TC_LOGIN_001 - Valid Login")
@allure.severity(allure.severity_level.CRITICAL)


@pytest.mark.smoke
@pytest.mark.regression

def test_login_positive(
    login_page,
    products_page,
    credentials
):
    
    # ==============================================================
    # OPEN LOGIN PAGE
    # ==============================================================
    
    with allure.step("User opens login page"):
        login_page.open_login_page()
        
    # ==============================================================
    # LOGIN
    # ==============================================================
    
    with allure.step("User login with valid credentials"):
        login_page.login(
            credentials["email"],
            credentials["password"]
        )
    
    # ==============================================================
    # VALIDATE URL
    # ==============================================================
    
    with allure.step("Validate user redirected to products page"):
        expect(products_page.page).to_have_url(Settings.PRODUCTS_URL)
    
    # ==============================================================
    # VALIDATE USERNAME
    # ==============================================================
    
    with allure.step("Validate username is visible"):
    
        expect(products_page.user_email).to_have_text(LoginExpected.USERNAME)
    
    # ==============================================================
    # VALIDATE PRODUCTS TITLE
    # ==============================================================
    
    with allure.step("Validate products dashboard title"):
        
        expect(products_page.products_title).to_have_text(LoginExpected.PRODUCTS_TITLE)


# ==============================================================
# NEGATIVE LOGIN
# ==============================================================

@allure.feature("Login")
@allure.story("Negative Login")
@allure.title("TC_LOGIN_001 - Invalid Login")
@allure.severity(allure.severity_level.NORMAL)

@pytest.mark.negative
@pytest.mark.regression

@pytest.mark.parametrize("email,password,error_message",
    INVALID_LOGIN_DATA
)

def test_login_negative(
    login_page,
    credentials,
    email,
    password,
    error_message
):
    
    # =====================================
    # RESOLVE TEST DATA
    # =====================================

    if email is None:
        email = credentials["email"]

    if password is None:
        password = credentials["password"]
    
    
    # =====================================
    # OPEN LOGIN PAGE
    # =====================================
    
    with allure.step("User opens login page"):
        
        login_page.open_login_page()
    
    
    # =====================================
    # LOGIN WITH INVALID DATA
    # =====================================
    
    with allure.step("User login with invalid credentials"):
        
        login_page.login(
            email,
            password
        )
    
    
    # =====================================
    # VALIDATE URL
    # =====================================

    with allure.step("Validate user remains on login page"):
    
        expect(login_page.page).to_have_url(Settings.LOGIN_URL)
    
    
    # =====================================
    # VALIDATE ERROR MESSAGE
    # =====================================

    with allure.step("Validate invalid credentials message"):
    
        expect(login_page.login_error).to_have_text(error_message, timeout=10000)
    
