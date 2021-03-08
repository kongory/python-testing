import allure
import pytest
from playwright.sync_api import Page

from pages.HomePage import HomePage
from pages.SignInPage import SignInPage


@allure.feature('Log in negative tests')
@allure.story('Authentication error')
@pytest.mark.parametrize("login,password",
                         [("aaaa@aa.aa", "123qew"), ("bbb@bb.bb", "zxcv545"), ("cccc@ccc.cc", "dfdsf7876")])
def test_sign_in_error(page: Page, login, password):
    home_page = HomePage(page)
    home_page.open_main_page()
    page.click(home_page.SIGN_IN_LOCATOR)
    sign_in_page = SignInPage(page)
    sign_in_page.populate_credentials(login, password)
    sign_in_page.click_sign_in_button()

    assert "Authentication failed." in sign_in_page.get_authentication_error_text(), \
        "Wrong authentication validation message"


@allure.feature('Log in negative tests')
@allure.story('Incorrect login error')
@pytest.mark.parametrize("login,password",
                         [("aaaa@aa,aa", "123qew"), ("bbb@bb,bb", "zxcv545"), ("cccc@ccc,cc", "dfdsf7876")])
def test_email_error(page: Page, login, password):
    home_page = HomePage(page)
    home_page.open_main_page()
    page.click(home_page.SIGN_IN_LOCATOR)
    sign_in_page = SignInPage(page)
    sign_in_page.populate_credentials(login, password)
    sign_in_page.click_sign_in_button()

    assert "Invalid email address." in sign_in_page.get_authentication_error_text(), "Wrong email validation message"
