from flask import Flask

api = Flask(__name__)
# design notes:
# 1. the api is a flask app
# 2. the api connects to a sqlite database
# 3. the api is a RESTful api
# 4. the api populates the database with data from the web
# 5. the api uses the database to serve data to the frontend
# 6. the api reads a json file to populate the database
# 7. the json file is a list of books and amazon links
# 8. the api reads the list of books and amazon links, and populates the database with data scraped from amazon
# 9. the api uses the database to serve data to the frontend
# 10. the scraper grabs the product image, title, author, price, and rating



@api.route('/profile')
def my_profile():
    response_body = {
        "name": "Nagato",
        "about" :"Hello! I'm a full stack developer that loves python and javascript"
    }

    return response_body