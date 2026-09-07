from playwright.sync_api import sync_playwright, expect
import pytest
import allure


data_valid = [('uno.testing3@gmail.com', '1234567890')]

@allure.title('Valid login with valid credentials.')
@allure.description('This test case will validate user login with happy flow')
@allure.feature('Login')
@allure.testcase('https://test.kelasotomesyen.com/products', name='TC-01-001')
@allure.suite('Login/')
@allure.severity(allure.severity_level.CRITICAL)

@pytest.mark.parametrize('email, password', data_valid)
def test_login_positive(chrome, email, password):
        with allure.step('user attempt to fill email field'):
            chrome.get_by_test_id("login-email-input").fill(email)
        with allure.step('user attempt to fill password field'):
            chrome.get_by_test_id("login-password-input").fill(password)
        with allure.step('user attempt to click submit button'):
            chrome.get_by_test_id("login-submit-button").click()
            chrome.wait_for_load_state('networkidle')
        with allure.step('user validate user is in product page'):
            expect(chrome).to_have_url('https://test.kelasotomesyen.com/products')
        with allure.step('user validate username is visible'):
            expect(chrome.get_by_test_id('user-email')).to_have_text('uno')
        
        title_element = chrome.get_by_test_id('products-title').text_content()
        assert title_element == 'TestApp -  Product Dashboard'

# @pytest.mark.firefox # running test tertentu -v -m chrome
# @pytest.mark.parametrize('email, password', data_valid)
# def test_login_positive_firefox(firefox, email, password):
        
#     firefox.get_by_test_id("login-email-input").fill(email)
#     firefox.get_by_test_id("login-password-input").fill(password)
#     firefox.get_by_test_id("login-submit-button").click()
#     firefox.wait_for_load_state('networkidle')
#     expect(firefox).to_have_url('https://test.kelasotomesyen.com/products')
#     expect(firefox.get_by_test_id('user-email')).to_have_text('uno')
        
#     title_element = firefox.get_by_test_id('products-title').text_content()
#     assert title_element == 'TestApp -  Product Dashboard'


# data_invalid = [('uno.testing3@gmail.com', 'salah', 'Invalid login credentials'),
#                 ('uno.testing3@gmail.co.id', '1234567890', 'Invalid login credentials')]

# @pytest.mark.parametrize('username, password, error_message', data_invalid)
# def test_login_negative(chrome, username, password, error_message):
#     '''
#     Test login dengan Email benar
#     password salah
#     '''
#     chrome.get_by_test_id("login-email-input").fill(username)
#     chrome.get_by_test_id("login-password-input").fill(password)
#     chrome.get_by_test_id("login-submit-button").click()
#     chrome.wait_for_load_state('networkidle')
#     expect(chrome).to_have_url('https://test.kelasotomesyen.com/login')
#     expect(chrome.get_by_test_id('login-error')).to_have_text(error_message)

# def test_login_negative_firefox(firefox):
#     '''
#     Test login dengan Email benar
#     password salah
#     '''
#     firefox.get_by_test_id("login-email-input").fill("uno.testing3@gmail.com")
#     firefox.get_by_test_id("login-password-input").fill("salah")
#     firefox.get_by_test_id("login-submit-button").click()
#     firefox.wait_for_load_state('networkidle')
#     expect(firefox).to_have_url('https://test.kelasotomesyen.com/login')
#     expect(firefox.get_by_test_id('login-error')).to_have_text('Invalid login credentials')
        