from setuptools import setup


with open("README.md", "r") as file:
	long_description = file.read()

requirements = ["pymorphy2", "pymorphy2-dicts-ru", "regex"]

setup(
	name="filtermat",
	version="1.5.3",
	author="qxtony",
	author_email="AntonSharafiev3866@gmail.com",
	description="This Python library is needed in order to search for Russian mat in text.",
	long_description=long_description,
	long_description_content_type="text/markdown",
	url="https://github.com/qxtony/filtermat",
	packages=["filtermat", "filtermat/files", "filtermat/functions"],
	install_requires=requirements,
	classifiers=[
		"Programming Language :: Python :: 3.8",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
	],
	python_requires='>=3.6',
)

