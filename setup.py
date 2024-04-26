from setuptools import find_packages, setup

setup(
    name="espwifiarduino",
    version="0.0.2",
    description="espwifiarduino python lib",
    url="https://github.com/2taras/espwifiarduino_py_lib",
    author="Taras E",
    author_email="2taras2006@gmail.com",
    packages=find_packages(),
    install_requires=["websockets"]
)