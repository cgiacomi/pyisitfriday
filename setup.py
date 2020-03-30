# pylint: disable=C0103,C0114
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyisitfriday",
    version="1.0.0",
    author="cgiacomi",
    author_email="cgiacomi@gmail.com",
    description="is it friday?",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/cgiacomi/pyisitfriday",
    packages=setuptools.find_packages(),
    install_requires=[],
    python_requires='>=3.6',
)
