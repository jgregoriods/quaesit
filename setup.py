import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="quaesit-jgregoriods", # Replace with your own username
    version="0.0.1",
    author="Jonas Gregorio",
    author_email="jonas.gregorio@gmail.com",
    description="Quick and easy simulation tools",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jgregoriods/quaesit.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)