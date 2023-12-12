from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

from dotenv import dotenv_values

env = dotenv_values(".env")
path = env["CHROME_DRIVER_PATH"]

class GetProductsCdiscount():
    def __init__(self):
        self.driver = self.init_webdriver()
        self.wait = WebDriverWait(self.driver, 5)

    def init_webdriver(self):
        # setup headless chrome driver
        print(path)
        driver = webdriver.Chrome()
        return driver

    def get_products(self, searched_products):
        url = "https://www.cdiscount.com/search/10/%s.html#_his_" % searched_products
        self.driver.get(url)

