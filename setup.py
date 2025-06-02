# setup.py
from setuptools import setup, find_packages

setup(
    name="stnlib",
    version="0.1.0",
    packages=find_packages(),
    description="Библиотека для работы с семантическими троичными узлами",
    author="Your Name",
    author_email="your@email.com",
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)