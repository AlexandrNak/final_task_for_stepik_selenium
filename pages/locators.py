from selenium.webdriver.common.by import By  

class MainPageLocators():
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".alertinner > strong")
    SUM_BASKET = (By.CSS_SELECTOR, ".alert.alert-safe.alert-noicon.alert-info.fade.in > div > p > strong")
    REAL_PRODUCT_NAME = (By.CSS_SELECTOR, ".col-sm-6.product_main > h1")
    PRICE_BASKET = (By.CSS_SELECTOR, ".col-sm-6.product_main .price_color")

# class LoginPageLocators():
#     LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
#     REGISTER_FORM =(By.CSS_SELECTOR, "#register_form1")



