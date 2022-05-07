from setuptools import setup

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="blurpify",
    version="0.1.0",
    description=(
        'A remake of a program that "blurpifies" images by converting them to shades of'
        " blurple."
    ),
    license="GPL-3.0",
    long_description=long_description,
    author="Astrea49",
    url="https://github.com/Astrea49/blurpify",
    packages=["blurpify"],
    install_requires=["pillow"],
    python_requires=">=3.8.0",
    entry_points={
        "console_scripts": "blurpify = blurpify.cli:main",
    },
)
