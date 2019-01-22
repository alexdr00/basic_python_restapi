# Dependencies
from flask import Flask
from mongoengine import connect

# Resources
from resources.posts import posts_api

# Constants definition
URL_PREFIX = '/api/v1'

# Flask app
app = Flask(__name__)

# Connection to the database via mongoengine
connect('python_restapi_db')

# Registering resources
app.register_blueprint(posts_api, url_prefix=URL_PREFIX)


# Main function
def main():
    app.run(port=3001, debug=True)


if __name__ == '__main__':
    main()
