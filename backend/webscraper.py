# scrapes the inputed url for the book title, author, and price
# uses the beautiful soup library
import requests
from bs4 import BeautifulSoup
import json
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Scraper:
    def __init__(self, url):
        self.url = url
        # get the url
        page = requests.get(url)
        # parse the page

        soup = BeautifulSoup(page.content, 'html.parser')
        # get the title

        title = soup.find(id="productTitle").get_text().strip()
        # get the author
        author = soup.find(id="bylineInfo").get_text().strip()
        # get the price
        price = soup.find(id="priceblock_ourprice").get_text().strip()
        # get the rating
        rating = soup.find(id="acrPopover").get_text().strip()
        # return the data
        image = soup.find(id="imgBlkFront").get_text().strip()

    
    def soup_finder_util(self, id):
        return self.soup.find(id=id).get_text().strip()
    
    def get_title(self):
        return self.title
    
    def get_author(self):
        return self.author
    
    def get_price(self):
        return self.price
    
    def get_rating(self):
        return self.rating
    
    def get_product_image(self):
        return self.image
    
    def get_data(self):
        return self.title, self.author, self.price, self.rating, self.image
    
    def get_url(self):
        return self.url
    
    def get_soup(self):
        return self.soup
    