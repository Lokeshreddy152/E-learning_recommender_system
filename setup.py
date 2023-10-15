# Import necessary functions from setuptools and typing
from setuptools import setup, find_packages
from typing import List

# Define the package version
__version__ = "0.0.1"

# Define project-related information
REPO_NAME = "E-learning_recommender_system"  # Name of the repository
AUTHOR_USER_NAME = "lokeshreddy152"  # GitHub username of the author
SRC_REPO = "E-learning_recommender_system"  # Source repository name
AUTHOR_EMAIL = "lokeshreddy152@gmail.com"  # Author's email address

# Define the name of the requirements file
REQURIMENT_FILE_NAME = "requirements.txt"

# This is a string used later to filter out the "-e ." entry in requirements
HYPHEN_E_DOT = "-e ."

# Function to read and parse the requirements from the requirements file
def get_requirements_list() -> List[str]:
    with open(REQURIMENT_FILE_NAME) as files:
        requriment_list = files.readlines()
        requriment_list = [file.replace("\n", "") for file in requriment_list]

        # Check if "-e ." (editable install) is in the requirements and remove it
        if HYPHEN_E_DOT in requriment_list:
            requriment_list.remove(HYPHEN_E_DOT)

        return requriment_list

# Define package information for setup
setup(
    name=SRC_REPO,  # Package name
    version=__version__,  # Package version
    author=AUTHOR_USER_NAME,  # Author's GitHub username
    author_email=AUTHOR_EMAIL,  # Author's email address
    description="A Small python package for NLP app",  # Package description
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",  # URL to the package's repository
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },  # URLs to project-related pages
    package_dir={"": "src"},  # Directory where packages are located
    packages=find_packages(where="src"),  # Find and include packages in the "src" directory
    install_requires=get_requirements_list()  # List of required packages
)