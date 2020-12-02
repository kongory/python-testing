import pytest
from playwright.sync_api import Page

from pages.HomePage import HomePage
from pages.SignInPage import SignInPage


@pytest.mark.parametrize("login,password",
                         [("aaaa@aa.aa", "123qew"), ("bbb@bb.bb", "zxcv545"), ("cccc@ccc.cc", "dfdsf7876")])
def test_sign_in_error(page: Page, login, password):
    home_page = HomePage(page)
    home_page.open_main_page()
    page.click(home_page.SIGN_IN_LOCATOR)
    signin_page = SignInPage(page)
    signin_page.populate_credentials(login, password)
    signin_page.click_sign_in_button()

    assert "Authentication failed." in signin_page.get_authentication_error_text()


@pytest.mark.parametrize("login,password",
                         [("aaaa@aa,aa", "123qew"), ("bbb@bb,bb", "zxcv545"), ("cccc@ccc,cc", "dfdsf7876")])
def test_email_error(page: Page, login, password):
    home_page = HomePage(page)
    home_page.open_main_page()
    page.click(home_page.SIGN_IN_LOCATOR)
    signin_page = SignInPage(page)
    signin_page.populate_credentials(login, password)
    signin_page.click_sign_in_button()

    assert "Invalid email address." in signin_page.get_authentication_error_text()
