from .base_page import BasePage
from .locators import LoginPageLocators, BasePageLocators

class LoginPage(BasePage):

    def should_be_login_page(self):
        
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "Подстрока 'login' отсутствует в текущем урле"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Нет формы для входа"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Нет формы для регистрации"

    def register_new_user(self, email, password):

        id_reg_email = self.browser.find_element(*BasePageLocators.ID_REGISTRATION_EMAIL)
        id_reg_email.send_keys(email)

        id_reg_pas_1 = self.browser.find_element(*BasePageLocators.ID_REGISTRATION_PASSWORD1)
        id_reg_pas_1.send_keys(password)

        id_reg_pas_2 = self.browser.find_element(*BasePageLocators.ID_REGISTRATION_PASSWORD2)
        id_reg_pas_2.send_keys(password)

        but_reg = self.browser.find_element(*BasePageLocators.BUTTON_REG)
        but_reg.click()



