from setuptools import setup
import os.path

setup(
    name='drugs',
    version='2.0.0',
    py_modules=['drugs'],
    data_files=[('', [
        "./drugs.data"
    ])]
)
