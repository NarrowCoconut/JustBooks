#  runs tests for webscraper.py
#  run with: python -m unittest tests.scraper_tests
from backend.webscraper import Scraper
import pytest

def test_get_product_image():
    url = "https://www.amazon.com/Python-Crash-Course-Hands-Project-Based/dp/1593279280"
    scraper = Scraper(url)
    assert scraper.get_product_image() == "https://images-na.ssl-images-amazon.com/images/I/51ZywvH1NWL._SX379_BO1,204,203,200_.jpg"

def test_get_title():
    url = "https://www.amazon.com/Python-Crash-Course-Hands-Project-Based/dp/1593279280"
    scraper = Scraper(url)
    assert scraper.get_title() == "Python Crash Course, 2nd Edition: A Hands-On, Project-Based Introduction to Programming"

def test_get_author():
    url = "https://www.amazon.com/Python-Crash-Course-Hands-Project-Based/dp/1593279280"
    scraper = Scraper(url)
    assert scraper.get_author() == "Eric Matthes"

def test_get_price():
    url = "https://www.amazon.com/Python-Crash-Course-Hands-Project-Based/dp/1593279280"
    scraper = Scraper(url)
    assert scraper.get_price() == "$29.99"

def test_get_rating():
    url = "https://www.amazon.com/Python-Crash-Course-Hands-Project-Based/dp/1593279280"
    scraper = Scraper(url)
    assert scraper.get_rating() == "4.8 out of 5 stars"

def test_get_data():
    url = "https://www.amazon.com/Python-Crash-Course-Hands-Project-Based/dp/1593279280"
    scraper = Scraper(url)
    assert scraper.get_data() == ("Python Crash Course, 2nd Edition: A Hands-On, Project-Based Introduction to Programming", "Eric Matthes", "$29.99", "4.8 out of 5 stars", "https://images-na.ssl-images-amazon.com/images/I/51ZywvH1NWL._SX379_BO1,204,203,200_.jpg")

def test_get_url():
    url = "https://www.amazon.com/Python-Crash-Course-Hands-Project-Based/dp/1593279280"
    scraper = Scraper(url)
    assert scraper.get_url() == "https://www.amazon.com/Python-Crash-Course-Hands-Project-Based/dp/1593279280"