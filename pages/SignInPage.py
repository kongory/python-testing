import logging

from playwright.page import Page

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
        self.page.waitForSelector(self.EMAIL_ADDRESS_LOCATOR)
        logger.info(f"Type login: '{email}'")
        self.page.type(self.EMAIL_ADDRESS_LOCATOR, email)
        logger.info(f"Type password: '{email}'")
        self.page.type(self.PASSWORD_LOCATOR, password)

    def get_authentication_error_text(self):
        logger.info("Get authentication error")
        self.page.waitForSelector(self.AUTHENTICATION_ERROR)
        text = self.page.textContent(self.AUTHENTICATION_ERROR)

        return text

    def click_sign_in_button(self):
        self.page.waitForSelector(self.SIGN_IN_LOCATOR)
        logger.info("Click on the 'Sign In' button")
        self.page.click(self.SIGN_IN_LOCATOR)
