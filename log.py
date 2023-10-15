from flask import Flask
from E_learning_recommender_system.logging import logging

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def index():
    logging.info("We are testing our logging file")

    return "logging test is done"

if __name__ == "__main__":
    app.run(debug = True) # 5000