import logging

from playwright.page import Page

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


class HomePage:
    ADDRESS = "http://automationpractice.com/index.php"

    CONFIRMATION_LOCATOR = "#layer_cart h2"
    SIGN_IN_LOCATOR = ".header_user_info a"
    CLOSE_MODAL_WINDOW_LOCATOR = "span[title='Close window']"
    VIEW_MY_SHOPPING_CART_LOCATOR = ".shopping_cart a[title='View my shopping cart']"
    SINGLE_ITEM_IN_CART_LOCATOR = ".cart_block_list .product-name a"
    SINGLE_ITEM_PRICE_IN_CART_LOCATOR = ".cart_block_list .cart-info .price"

    def __init__(self, page: Page):
        self.page = page

    def open_main_page(self):
        logger.info("Open Home page")
        home_page = HomePage(self.page)
        self.page.goto(home_page.ADDRESS)
        self.page.waitForLoadState()

    def add_thing_to_cart_by_name(self, name):
        logger.info(f"Waiting for the '{name}' item")
        self.page.waitForSelector(f"a[title='{name}']")
        logger.info(f"Hover on the '{name}' item")
        self.page.hover(f"a[title='{name}']")
        logger.info("Click on the 'Add to cart' button")
        self.page.click(
            f"//ul[@id='homefeatured']//div[h5//a[normalize-space()='{name}']]//a[span[text()='Add to cart']]")

    def get_confirmation_text(self):
        logger.info("Return confirmation message")
        self.page.waitForSelector(self.CONFIRMATION_LOCATOR)

        return self.page.textContent(self.CONFIRMATION_LOCATOR)

    def close_confirmation_modal(self):
        logger.info("Close confirmation window")
        self.page.waitForSelector(self.CLOSE_MODAL_WINDOW_LOCATOR)
        self.page.click(self.CLOSE_MODAL_WINDOW_LOCATOR)

    def expand_cart(self):
        logger.info("Expand cart")
        self.page.waitForSelector(self.VIEW_MY_SHOPPING_CART_LOCATOR)
        self.page.hover(self.VIEW_MY_SHOPPING_CART_LOCATOR)

    def return_purchase_data(self):
        self.page.waitForSelector(self.SINGLE_ITEM_IN_CART_LOCATOR)
        logger.info("Get title of the added item to cart")
        title = self.page.getAttribute(self.SINGLE_ITEM_IN_CART_LOCATOR, "title")
        logger.info("Get price of the added item to cart")
        price = self.page.textContent(self.SINGLE_ITEM_PRICE_IN_CART_LOCATOR)

        return title, price
