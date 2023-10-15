from flask import Flask
from E_learning_recommender_system.logging import logging
from E_learning_recommender_system.exception import CustomException
import os, sys

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def index():

    try:
        raise Exception("we are testing our Exception file") # Error
    except Exception as e:
        ML = CustomException(e, sys)
        logging.info(ML.error_message)
        
        logging.info("Exception test as done")

        return "Test of exception is done Successfully"

if __name__ == "__main__":
    app.run(debug = True) # 5000