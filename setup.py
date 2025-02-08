from setuptools import find_packages, setup
from typing import List

__version__ = "0.0.1"

HYPHEN_E_DOT = "-e ."

REPO_NAME = "NLP-Text-Summarizer"
AUTHOR_USER_NAME = "Omarkh98"
SRC_REPO = "TextSummarizer"
AUTHOR_EMAIL = "omarklotfy@gmail.com"

def get_requirements(file_path: str) -> List[str]:
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        for req in requirements:
            req.replace("/n", "")

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements

with open("README.md", "r", encoding = "utf-8") as f:
    long_description = f.read()

setup(
    name = REPO_NAME,
    version = __version__,
    author = AUTHOR_USER_NAME,
    author_email = AUTHOR_EMAIL,
    description = "A small python package for a NLP application",
    long_description = long_description,
    url = f"https://github.com/Omarkh98/NLP-Text-Summarizer",
    package_dir = {"": "src"},
    packages = find_packages(where = "src"),
    install_requires = get_requirements("requirements.txt")
)