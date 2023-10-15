# Import necessary libraries
import os
from pathlib import Path
import logging

# Configure logging to display information messages with a specific format
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

# Define the project name
project_name = "E_learning_recommender_system"

# List of files to be created or checked
list_of_files = [
    ".github/workflows/.gitkeep",  # Create or check the existence of a hidden folder
    f"src/{project_name}/__init__.py",  # Create or check '__init__.py' file in a package
    f"src/{project_name}/components/__init__.py",  # Create or check '__init__.py' in a subpackage
    f"src/{project_name}/utils/__init__.py",  # Create or check '__init__.py' in another subpackage
    f"src/{project_name}/utils/common.py",  # Create or check 'common.py' in the 'utils' subpackage
    f"src/{project_name}/exception/__init__.py",  # Create or check '__init__.py' in the 'exception' subpackage
    f"src/{project_name}/logging/__init__.py",  # Create or check '__init__.py' in the 'logging' subpackage
    f"src/{project_name}/config/__init__.py",  # Create or check '__init__.py' in the 'config' subpackage
    f"src/{project_name}/config/configuration.py",  # Create or check 'configuration.py' in the 'config' subpackage
    f"src/{project_name}/pipeline/__init__.py",  # Create or check '__init__.py' in the 'pipeline' subpackage
    f"src/{project_name}/entity/__init__.py",  # Create or check '__init__.py' in the 'entity' subpackage
    f"src/{project_name}/constants/__init__.py",  # Create or check '__init__.py' in the 'constants' subpackage
    "config/config.yaml",  # Create or check 'config.yaml' in the 'config' folder
    "params.yaml",  # Create or check 'params.yaml' in the root directory
    "app.py",  # Create or check 'app.py' in the root directory
    "main.py",  # Create or check 'main.py' in the root directory
    "Dockerfile",  # Create or check 'Dockerfile' in the root directory
    "requirements.txt",  # Create or check 'requirements.txt' in the root directory
    "setup.py",  # Create or check 'setup.py' in the root directory
    "research/trials.ipynb",  # Create or check 'trials.ipynb' in the 'research' folder
    "test.py"  # Create or check 'test.py' in the root directory
]

# Loop through the list of files and perform necessary actions
for filepath in list_of_files:
    filepath = Path(filepath)  # Convert the path as per the local system's requirements
    filedir, filename = os.path.split(filepath)  # Get the folder and filename from the path

    # If the file belongs to a subdirectory, create the folder if it doesn't exist
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)  # Create the folder if it does not exist
        logging.info(f"Created folder: {filedir} for the file {filename}")

    # Check if the file doesn't exist or is empty, and create an empty file if needed
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
        logging.info(f"Created empty file: {filepath}")
    else:
        logging.info(f"{filename} is already created")
