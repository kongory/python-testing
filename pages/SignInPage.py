import logging

from playwright.sync_api import Page

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


class SignInPage:
    EMAIL_ADDRESS_LOCATOR = "#email"
    PASSWORD_LOCATOR = "#passwd"
    SIGN_IN_LOCATOR = "#SubmitLogin"
    AUTHENTICATION_ERROR = ".alert.alert-danger li"

    def __init__(self, page: Page):
        self.page = page

    def populate_credentials(self, email, password):
        self.page.wait_for_selector(self.EMAIL_ADDRESS_LOCATOR)
        logger.info(f"Type login: '{email}'")
        self.page.type(self.EMAIL_ADDRESS_LOCATOR, email)
        logger.info(f"Type password: '{email}'")
        self.page.type(self.PASSWORD_LOCATOR, password)

    def get_authentication_error_text(self):
        logger.info("Get authentication error")
        self.page.wait_for_selector(self.AUTHENTICATION_ERROR)
        text = self.page.text_content(self.AUTHENTICATION_ERROR)

        return text

    def click_sign_in_button(self):
        self.page.wait_for_selector(self.SIGN_IN_LOCATOR)
        logger.info("Click on the 'Sign In' button")
        self.page.click(self.SIGN_IN_LOCATOR)
