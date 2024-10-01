from .base_page import BasePage
from .locators import MainPageLocators

class MainPage(BasePage):
    def add_to_cart(self):
        add_cart_button = self.browser.find_element(*MainPageLocators.ADD_TO_CART_BUTTON)
        add_cart_button.click()

    def should_be_product_name(self):
        book_name = self.browser.find_element(*MainPageLocators.PRODUCT_NAME)
        real_book_name = self.browser.find_element(*MainPageLocators.REAL_PRODUCT_NAME)
        assert real_book_name.text == book_name.text, "Название книги не совпадает"

    def should_be_sum_basket(self):
        sum_bas = self.browser.find_element(*MainPageLocators.SUM_BASKET)
        price_bas = self.browser.find_element(*MainPageLocators.PRICE_BASKET)
        assert price_bas.text == sum_bas.text, "Цена в корзине не совпадает"




    # def should_be_login_link(self):
    #     assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Ссылка для входа в систему не представлена"



