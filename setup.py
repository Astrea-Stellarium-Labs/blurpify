from setuptools import setup

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="blurpify",
    version="0.0.1",
    description='A remake of a program that "blurpifies" images by converting them to shades of blurple.',
    license="GPL v3",
    long_description=long_description,
    author="Sonic49",
    url="https://github.com/Sonic4999/blurpify",
    packages=["blurpify"],
    install_requires=["pillow"],
    python_requires=">=3.8.0",
)
