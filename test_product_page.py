import pytest

from .pages.product_page import MainPage
from .pages.base_page import BasePage
import time  


@pytest.mark.parametrize('x', ["?promo=offer0", 
                                "?promo=offer1", 
                                "?promo=offer2", 
                                "?promo=offer3",
                                "?promo=offer4",
                                "?promo=offer5",
                                "?promo=offer6",
                                pytest.param("?promo=offer7", marks=pytest.mark.xfail),
                                "?promo=offer8",
                                "?promo=offer9"
                                ])
def test_guest_can_add_product_to_basket(browser, x):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/{x}"
    page = MainPage(browser, link)
    page.open()
    page.add_to_cart()
    page.solve_quiz_and_get_code()
    page.should_be_product_name()
    page.should_be_sum_basket()
    time.sleep(2)



    

