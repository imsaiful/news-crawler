from setuptools import setup, find_packages

setup(
    name         = 'newsfetch',
    version      = '1.0',
    packages     = find_packages(),
    entry_points = {'scrapy': ['settings = newsfetch.settings']},
    scripts = ['bin/testargs.py']
    
)
