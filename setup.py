import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

requirements = []
with open("requirements.txt", "r") as requirements_file:
    requirements = [l.strip() for l in requirements_file]

setuptools.setup(
    name="jwscraper",
    version="1.0",
    author="morpheusthewhite",
    author_email="zffromGerace@hotmail.it",
    description="A JW Player video scraper",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/morpheusthewhite/jwscraper",
    packages=setuptools.find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MPL",
        "Operating System :: OS Independent",
    ],
)