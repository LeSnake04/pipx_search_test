import pathlib
from setuptools import setup, find_packages

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

setup(
    name="pipx_search_test",
    version="0.0.7",
    author="LeSnake",
    author_email="dev.lesnake@posteo.de",
    url='https://github.com/LeSnake04/pipx_search_test',
    description="A package to search like pip used to via PyPi",
    long_description=README,
    long_description_content_type='text/markdown',
    packages=find_packages(exclude=("tests",)),
    install_requires=['bs4', 'requests', 'rich'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.',
    entry_points={
        "console_scripts": [
            "pipx_search_test=pipx_search_test.__main__:main",
        ],
    },
)
