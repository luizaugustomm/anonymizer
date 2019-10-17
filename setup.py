import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="anonymizer",
    version="0.0.1",
    author="Luiz Morais",
    author_email="luizaugustomm@gmail.com",
    description="A tool to anonymize documents",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/luizaugustomm/anonymizer",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
