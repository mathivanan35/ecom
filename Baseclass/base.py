from selenium import webdriver
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager


class Base1:
    def getDriver(self):
        self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        return self.driver

    def getUrl(self, url):
        self.driver.get(url)

    def type(self, element, text):
        element.send_keys(text)

    def button(self, element):
        element.click()

    def option(self, element, text):
        se = Select(element)
        se.select_by_visible_text(text)