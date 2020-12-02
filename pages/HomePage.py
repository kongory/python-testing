from playwright.page import Page


class HomePage:
    ADDRESS = "http://automationpractice.com/index.php"

    CONFIRMATION_LOCATOR = "#layer_cart h2"
    SIGN_IN_LOCATOR = ".header_user_info a"

    def open_main_page(self):
        home_page = HomePage(self.page)
        self.page.goto(home_page.ADDRESS)
        self.page.waitForLoadState()

    def add_thing_to_cart_by_name(self, name):
        self.page.waitForSelector(f"a[title='{name}']")
        self.page.hover(f"a[title='{name}']")
        self.page.click(
            f"//ul[@id='homefeatured']//div[h5//a[normalize-space()='{name}']]//a[span[text()='Add to cart']]")

    def get_confirmation_text(self):
        self.page.waitForSelector(self.CONFIRMATION_LOCATOR)

        return self.page.textContent(self.CONFIRMATION_LOCATOR)

    def close_confirmation_modal(self):
        button = "span[title='Close window']"
        self.page.waitForSelector(button)
        self.page.click(button)

    def expand_cart(self):
        button = ".shopping_cart a[title='View my shopping cart']"
        self.page.waitForSelector(button)
        self.page.hover(button)

    def return_purchase_data(self):
        item_locator = ".cart_block_list .product-name a"
        price_locator = ".cart_block_list .cart-info .price"
        self.page.waitForSelector(item_locator)
        title = self.page.getAttribute(item_locator, "title")
        price = self.page.textContent(price_locator)

        return title, price

    def __init__(self, page: Page):
        self.page = page
