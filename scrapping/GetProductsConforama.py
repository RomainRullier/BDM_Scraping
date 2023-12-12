from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from dotenv import dotenv_values

env = dotenv_values(".env")
path = env["CHROME_DRIVER_PATH"]

selector = {
    'accept-cookies' : 'onetrust-accept-btn-handler',
    'seller' : 'c-r_seller',
    'rating' : 'stars',
    'name' : 'c-r_product_name',
    'image' : 'image-product',
    'price' : 'wrapper-price',
}

class GetProductsConforama():
    def __init__(self, handless=False):
        self.handless = handless
        self.driver = self.init_webdriver()
        self.wait = WebDriverWait(self.driver, 5)

    def accept_cookies(self):
        self.wait.until(EC.element_to_be_clickable((By.ID, selector['accept-cookies']))).click()

    def init_webdriver(self):
        options = webdriver.ChromeOptions()
        if self.handless:
            options.add_argument("--headless")
        driver = webdriver.Chrome(options=options)
        return driver

    def get_products(self, searched_products):
        url = "https://www.conforama.fr/recherche-conforama/%s?fromSearch=%s" % (searched_products, searched_products)
        self.driver.get(url)
        data = []

        if not self.handless:
            self.accept_cookies()

        self.wait.until(EC.presence_of_element_located((By.CLASS_NAME,  selector['price'])))

        products = self.driver.find_elements(By.TAG_NAME, 'article')

        for article in products:
            curr_data = {}
            try:
                curr_data['seller'] = article.find_element(By.CLASS_NAME, selector['seller']).text
            except:
                curr_data['seller'] = 'Conforama'
            try:
                curr_data['rating'] = article.find_element(By.CLASS_NAME, selector['rating']).get_attribute('data')
            except:
                curr_data['rating'] = ''
            try:
                curr_data['name'] = article.find_element(By.CLASS_NAME, selector['name']).text
            except:
                curr_data['name'] = ''
            try:
                curr_data['link'] = article.find_element(By.TAG_NAME, 'a').get_attribute('href')
            except:
                curr_data['link'] = ''
            try:
                curr_data['image'] = article.find_element(By.CLASS_NAME, selector['image']).find_element(By.TAG_NAME, 'img').get_attribute('src')
            except:
                curr_data['image'] = ''
            try:
                curr_data['price'] = article.find_element(By.CLASS_NAME, selector['price']).text
            except:
                curr_data['price'] = ''

            data.append(curr_data)

        self.close()
        return data

    def close(self):
        self.driver.close()


