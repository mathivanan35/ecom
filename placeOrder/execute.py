import time

from placeOrder.elements import *
from Baseclass.base import Base1
from data_sheet.read import read
import pytest


def test_launch():
    base = Base1()
    driver = base.getDriver()
    driver.maximize_window()
    driver.implicitly_wait(20)
    base.getUrl("https://www.flipkart.com/")

    product = search_product(driver)
    base.button(product.get_button_clickclose())
    base.type(product.gettext_search(), read(4, 2))
    base.button(product.getbutton_searchIcon())
    base.button(product.getclick_SelectProduct())
    base.button(product.getbutton_buyNow())
    base.type(product.gettext_email(),read(1, 2))
    base.button(product.getbutton_continue())
    base.type(product.gettext_password(),read(2, 2))
    base.button(product.getbutton_login())

    address = add_Address(driver)
    base.button(address.getclick_addnewAddress())
    base.type(address.gettext_name(),read(6,2))
    base.type(address.gettext_mobileno(),read(7, 2))
    base.type(address.gettext_pincode(),read(8, 2))
    base.type(address.gettext_locality(),read(9,2))
    base.type(address.gettext_areaAddress(),read(10,2))
    base.type(address.gettext_city(),read(11, 2))
    base.option(address.gettext_state(),"Tamil Nadu")
    base.button(address.getbutton_addressType())
    base.button(address.getbutton_save())
    base.button(address.getbutton_continue())

    pay = payment(driver)
    base.button(pay.getbutton_creditcard())
    base.type(pay.gettext_cardNo(),read(14, 2))
    base.option(pay.gettext_expMonth(),read(15, 2))
    base.option(pay.gettext_expYear(),read(16, 2))
    base.type(pay.gettext_CVV(),read(17, 2))



