from config.settings import Settings
from pages.base_page import BasePage
from playwright.sync_api import Page

class LoginPage(BasePage):
    
    def __init__(self, page):
        
        super().__init__(page)
        
        self.email_input = (page.get_by_test_id("login-email-input"))
        
        self.password_input = (page.get_by_test_id("login-password-input"))
        
        self.submit_button = (page.get_by_test_id("login-submit-button"))
        
        self.login_error = (page.get_by_test_id("login-error"))
        
    def open_login_page(self):
        self.open(Settings.LOGIN_URL)
    
    def fill_email(self, email):
        self.email_input.fill(email)
    
    def fill_password(self, password):
        self.password_input.fill(password)
    
    def click_login_button(self):
        self.submit_button.click()
    
    def login(self, email, password):
        
        self.fill_email(email)
        
        self.fill_password(password)
        
        self.click_login_button()