from setuptools import setup


with open("README.md", "r") as readme_file:
    long_description = readme_file.read()

requirements = ["pymorphy2", "pymorphy2-dicts-ru", "regex"]

setup(
    name="roughfilter",
    version="2.0.2",
    author="qxtony",
    author_email="qxtonydev@gmail.com",
    description="With this library, you can easily catch rude expressions in text.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/qxtony/roughfilter",
    packages=["roughfilter", "roughfilter/bases", "roughfilter/functions"],
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)
