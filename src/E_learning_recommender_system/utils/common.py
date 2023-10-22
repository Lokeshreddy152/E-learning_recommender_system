import os  # Import the 'os' library for operating system-related functions.
from box.exceptions import BoxValueError  # Import an exception class from the 'box' library.
import yaml  # Import the 'yaml' library for working with YAML files.
from E_learning_recommender_system.logging import logging  # Import a custom logger from the 'E_learning_recommender_system.logging' module.
from ensure import ensure_annotations  # Import the 'ensure_annotations' decorator for type hint enforcement.
from box import ConfigBox  # Import the 'ConfigBox' class from the 'box' library.
from pathlib import Path  # Import the 'Path' class from the 'pathlib' library for working with file paths.
from typing import Any  # Import the 'Any' type hint for flexibility in function argument and return types.

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
import re

nltk.download('stopwords')
nltk.download('punkt')

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    This is a Python function that reads a YAML file and returns its content as a 'ConfigBox' object.

    Parameters:
        path_to_yaml (Path): The path to the YAML file to be read.

    Returns:
        ConfigBox: A structured object representing the YAML content.

    It uses the 'ensure_annotations' decorator to enforce type hints on the function arguments and return values.
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)  # Load the YAML content from the file.
            logging.info(f"yaml file:{path_to_yaml} loaded successfully")  # Log a success message.
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")  # If a BoxValueError occurs, raise a ValueError with a message.
    except Exception as e:
        raise e  # If any other exception occurs, raise that exception.

@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """
    This Python function creates a list of directories given their paths.

    Parameters:
        path_to_directories (list): A list of paths to the directories to be created.
        verbose (bool, optional): If True, log messages will be generated for each directory creation. Defaults to True.

    The 'ensure_annotations' decorator enforces type hints for the function arguments.

    The function iterates through the list of directory paths, creating each directory using 'os.makedirs'.
    If 'verbose' is True, it logs a message for each directory created.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)  # Create the directory, and 'exist_ok=True' ensures it doesn't throw an error if it already exists.
        if verbose:
            logging.info(f"created directory at: {path}")  # Log a message if 'verbose' is True.


@ensure_annotations
def get_size(path: Path) -> str:
    """
    This function calculates the size of a file in kilobytes (KB) and returns it as a string.

    Args:
        path (Path): The path to the file for which you want to calculate the size.

    Returns:
        str: A string representing the size in kilobytes, e.g., "1234 KB".
    """
    size_in_kb = round(os.path.getsize(path) / 1024)  # Calculate the size in KB by dividing by 1024.
    return f"~ {size_in_kb} KB"  # Return the size as a string with the "~" symbol for approximate size.

@ensure_annotations
def preprocess_text(text):
    # Remove special characters and numbers
    text = re.sub(r'[^a-zA-Z\s]', '', text)

    # Convert to lowercase
    text = text.lower()

    # Tokenization (split the text into words)
    tokens = word_tokenize(text)

    # Remove stopwords (common words like 'the', 'and', 'is')
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [word for word in tokens if word not in stop_words]

    # Stemming (reducing words to their root form)
    stemmer = PorterStemmer()
    stemmed_tokens = [stemmer.stem(word) for word in filtered_tokens]

    # Join the tokens back into a single string
    preprocessed_text = ' '.join(stemmed_tokens)

    return preprocessed_text