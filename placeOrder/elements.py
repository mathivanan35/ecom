from selenium.webdriver.common.by import By
from placeOrder import Locators


# class login:
#     def __init__(self, driver):
#         self.driver = driver
#
#         self.button_clickLogin = driver.find_element(By.XPATH, Locators.login1_xpath)
#         self.text_Username = driver.find_element(By.XPATH, Locators.userName_xpath)
#         self.text_Password = driver.find_element(By.XPATH, Locators.password_xpath)
#         self.button_Login2 = driver.find_element(By.XPATH, Locators.login2_xpath)
#
#     def getbutton_clickLogin(self):
#         return self.button_clickLogin
#
#     def gettext_Username(self):
#         return self.text_Username
#
#     def gettext_Password(self):
#         return self.text_Password
#
#     def getbutton_Login2(self):
#         return self.button_Login2


class search_product:
    def __init__(self, driver):
        self.driver = driver
        self.button_clickClose = driver.find_element(By.XPATH, Locators.closePopUp_xpath)
        self.text_search = driver.find_element(By.XPATH, Locators.search_xpath)
        self.button_searchIcon = driver.find_element(By.XPATH, Locators.clickSearch_xpath)
        self.click_SelectProduct = driver.find_element(By.XPATH, Locators.product_xpath)
        self.button_buyNow = driver.find_element(By.XPATH, Locators.buyNow_xpath)
        self.text_email = driver.find_element(By.XPATH, Locators.email_xpath)
        self.button_continue = driver.find_element(By.XPATH, Locators.continuebutton_xpath)
        self.text_password = driver.find_element(By.XPATH, Locators.password_xpath)
        self.button_login = driver.find_element(By.XPATH, Locators.loginbutton_xpath)

    def get_button_clickclose(self):
        return self.button_clickClose

    def gettext_search(self):
        return self.text_search

    def getbutton_searchIcon(self):
        return self.button_searchIcon

    def getclick_SelectProduct(self):
        return self.click_SelectProduct

    def getbutton_buyNow(self):
        return self.button_buyNow

    def gettext_email(self):
        return self.text_email

    def getbutton_continue(self):
        return self.button_continue

    def gettext_password(self):
        return self.text_password

    def getbutton_login(self):
        return self.button_login


class add_Address:
    def __init__(self, driver):
        self.driver = driver
        self.click_addnewAddress = driver.find_element(By.XPATH, Locators.address_xpath)
        self.text_name = driver.find_element(By.XPATH, Locators.name_xpath)
        self.text_mobileno = driver.find_element(By.XPATH, Locators.mobile_xpath)
        self.text_pincode = driver.find_element(By.XPATH, Locators.pincode_xpath)
        self.text_locality = driver.find_element(By.XPATH, Locators.locality_xpath)
        self.text_areaAddress = driver.find_element(By.XPATH, Locators.address_Area_xpath)
        self.text_city = driver.find_element(By.XPATH, Locators.city_xpath)
        self.text_state = driver.find_element(By.XPATH, Locators.state_xpath)
        self.button_addressType = driver.find_element(By.XPATH, Locators.addressType_button_xpath)
        self.button_save = driver.find_element(By.XPATH, Locators.saveAndDelivery_xpath)
        self.button_continue = driver.find_element(By.XPATH, Locators.click_Continue_xpath)

    def getclick_addnewAddress(self):
        return self.click_addnewAddress

    def gettext_name(self):
        return self.text_name

    def gettext_mobileno(self):
        return self.text_mobileno

    def gettext_pincode(self):
        return self.text_pincode

    def gettext_locality(self):
        return self.text_locality

    def gettext_areaAddress(self):
        return self.text_areaAddress

    def gettext_city(self):
        return self.text_city

    def gettext_state(self):
        return self.text_state

    def getbutton_addressType(self):
        return self.button_addressType

    def getbutton_save(self):
        return self.button_save

    def getbutton_continue(self):
        return self.button_continue


class payment:

    def __init__(self, driver):
        self.driver = driver
        self.button_creditcard = driver.find_element(By.XPATH, Locators.creditCard_xpath)
        self.text_cardNo = driver.find_element(By.XPATH, Locators.cardNo_xpath)
        self.text_expMonth = driver.find_element(By.XPATH, Locators.expMonth_xpath)
        self.text_expYear = driver.find_element(By.XPATH, Locators.expYear_xpath)
        self.text_CVV = driver.find_element(By.XPATH, Locators.CVV_xpath)

    def getbutton_creditcard(self):
        return self.button_creditcard

    def gettext_cardNo(self):
        return self.text_cardNo

    def gettext_expMonth(self):
        return self.text_expMonth

    def gettext_expYear(self):
        return self.text_expYear

    def gettext_CVV(self):
        return self.text_CVV
