from setuptools import setup, find_packages
from typing import List

__version__ = "0.0.1"

REPO_NAME = "E-learning_recommender_system"
AUTHOR_USER_NAME = "lokeshreddy152"
SRC_REPO = "E-learning_recommender_system"
AUTHOR_EMAIL = "lokeshreddy152@gmail.com"

REQURIMENT_FILE_NAME = "requirements.txt"

HYPHEN_E_DOT = "-e ."

def get_requirements_list()->List[str]:
    with open(REQURIMENT_FILE_NAME) as files:
        requriment_list = files.readlines()
        requriment_list = [file.replace("\n","")for file in requriment_list]

        if HYPHEN_E_DOT in requriment_list:
            requriment_list.remove(HYPHEN_E_DOT)
        
        return requriment_list
    
setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A Small python package for NLP app",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir = {"":"src"},
    packages = find_packages(where="src"),
    install_requires = get_requirements_list())