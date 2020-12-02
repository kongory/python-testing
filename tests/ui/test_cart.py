from playwright.sync_api import Page

from pages.HomePage import HomePage


def test_confirmation(page: Page):
    home_page = HomePage(page)
    home_page.open_main_page()
    home_page.add_thing_to_cart_by_name("Blouse")
    text = home_page.get_confirmation_text()

    assert "Product successfully added to your shopping cart" in text


def test_cart(page: Page):
    home_page = HomePage(page)
    home_page.open_main_page()
    home_page.add_thing_to_cart_by_name("Printed Dress")
    home_page.close_confirmation_modal()
    home_page.expand_cart()
    data = home_page.return_purchase_data()

    assert ("Printed Dress", "$26.00") == data
