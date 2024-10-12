from selenium.webdriver.common.by import By  

class MainPageLocators():
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".alertinner > strong")
    SUM_BASKET = (By.CSS_SELECTOR, ".alert.alert-safe.alert-noicon.alert-info.fade.in > div > p > strong")
    REAL_PRODUCT_NAME = (By.CSS_SELECTOR, ".col-sm-6.product_main > h1")
    PRICE_BASKET = (By.CSS_SELECTOR, ".col-sm-6.product_main .price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alertinner")
    VIEW_BASKET = (By.CSS_SELECTOR, ".btn-group > .btn.btn-default")
    EMPTY_BASKET = (By.CSS_SELECTOR, "#content_inner > p")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    ID_REGISTRATION_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    ID_REGISTRATION_PASSWORD1 = (By.CSS_SELECTOR, "#id_registration-password1")
    ID_REGISTRATION_PASSWORD2 = (By.CSS_SELECTOR, "#id_registration-password2")
    BUTTON_REG = (By.CSS_SELECTOR, "#register_form > .btn.btn-lg.btn-primary")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM =(By.CSS_SELECTOR, "#register_form")



