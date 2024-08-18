from setuptools import setup, find_packages
from typing import List

HYPHEN_E_DOT = "-e ."


def get_requirements(filepath: str) -> List[str]:
    requirements = []
    with open(filepath) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements


setup(
    name="DreamAIAgent",
    version="0.0.1",
    author="Suryansh Pandey",
    author_email="suryanshghazipur@gmail.com",
    install_requires=get_requirements("requirements.txt"),
    packages=find_packages(),
)
