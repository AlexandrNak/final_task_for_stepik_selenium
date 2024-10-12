from .base_page import BasePage
from .locators import MainPageLocators


class BasketPage(BasePage):

    def should_not_be_success_message(self):
        assert not self.is_not_element_present(*MainPageLocators.EMPTY_BASKET), "Сообщение об успехе представлено, но его не должно было быть"

    def should_be_success_message(self):
        assert not self.is_disappeared(*MainPageLocators.EMPTY_BASKET), "Сообщение об успехе представлено"
        