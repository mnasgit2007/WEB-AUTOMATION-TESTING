import pytest

class LoginExpected:
    
    USERNAME = "uno"
    
    PRODUCTS_TITTLE = (
        "TestApp -  Product Dashboard"
    )
    
    INVALID_CREDENTIALS = (
        "Invalid login credentials"
    )

INVALID_LOGIN_DATA = [

    pytest.param(
        None,
        "salah",
        LoginExpected.INVALID_CREDENTIALS,
        id="valid-email-invalid-password"
    ),

    pytest.param(
        "uno.testing3@gmail.co.id",
        None,
        LoginExpected.INVALID_CREDENTIALS,
        id="invalid-email-valid-password"
    )
]