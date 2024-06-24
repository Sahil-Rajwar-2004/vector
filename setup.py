import setuptools

with open("README.md","r") as file:
    long_desc = file.read()

setuptools.setup(
    name = "vector",
    version = "0.1.0",
    author = "Sahil Rajwar",
    description = "A python lib for vector calculation that's it",
    long_description = long_desc,
    long_description_content_type = "text/markdown",
    url = "https://github.com/Sahil-Rajwar-2004/vector",
    packages = setuptools.find_packages(),
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    license = "MIT",
    python_requires = ">=3.6",
)

