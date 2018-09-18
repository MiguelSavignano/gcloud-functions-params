import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

VERSION = "0.0.2"

setuptools.setup(
    name="gcloud-functions-params",
    version=VERSION,
    author="Miguel Savignano",
    author_email="migue.masx@gmail.com",
    description="package for manage params in python gcloud functions",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
