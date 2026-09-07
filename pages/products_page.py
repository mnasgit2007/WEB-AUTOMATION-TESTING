from pages.base_page import BasePage


class ProductPage(BasePage):
    
    def __init__(self, page):
        super().__init__(page)
        
        self.user_email = (page.get_by_test_id("user-email"))
        
        self.products_title = (page.get_by_test_id("products-title"))
        
        