from setuptools import setup, find_packages

setup(
    name='webscrapper',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        'requests',
        'beautifulsoup4',
        'aiohttp'
    ],
    description='Web scrapper',
    author='Shadow7x',
    author_email='loginvlad1000@gmail.com',
    
)