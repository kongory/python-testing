from playwright.page import Page


class SignInPage:
    EMAIL_ADDRESS_LOCATOR = "#email"
    PASSWORD_LOCATOR = "#passwd"
    SIGNIN_LOCATOR = "#SubmitLogin"
    AUTHENTICATION_ERROR = ".alert.alert-danger li"

    def populate_credentials(self, email, password):
        self.page.waitForSelector(self.EMAIL_ADDRESS_LOCATOR)
        self.page.type(self.EMAIL_ADDRESS_LOCATOR, email)
        self.page.type(self.PASSWORD_LOCATOR, password)

    def __init__(self, page: Page):
        self.page = page

    def get_authentication_error_text(self):
        self.page.waitForSelector(self.AUTHENTICATION_ERROR)
        text = self.page.textContent(self.AUTHENTICATION_ERROR)

        return text

    def click_sign_in_button(self):
        self.page.waitForSelector(self.SIGNIN_LOCATOR)
        self.page.click(self.SIGNIN_LOCATOR)
