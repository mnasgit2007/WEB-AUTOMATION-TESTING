import os

from dotenv import load_dotenv

load_dotenv()

class Settings:
    
    BASE_URL = os.getenv(
        "BASE_URL",
        "https://test.kelasotomesyen.com"
    ).rstrip("/")
    
    LOGIN_URL = f"{BASE_URL}/login"
    
    PRODUCTS_URL = f"{BASE_URL}/products"
    
    TEST_EMAIL = os.getenv("TEST_EMAIL")
    
    TEST_PASSWORD = os.getenv("TEST_PASSWORD")