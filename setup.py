import setuptools

with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name="iscontain",
    version="0.1",
    author="SHYChePi",
    description="It can check if A is a subset of B based on python 3.10",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/SHYChePi/iscontain/",
    packages=setuptools.find_packages(),
    install_requires=[''],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
