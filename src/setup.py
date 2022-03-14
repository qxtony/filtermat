from setuptools import setup, find_packages


with open("README.md", "r") as file:
	long_description = file.read()

requirements = ["pymorphy2", "pymorphy2-dicts-ru", "regex"]

setup(
	name="filtermat",
	version="1.2",
	author="qxtony",
	author_email="qxtonydev@gmail.com",
	description="This Python library is needed in order to search for Russian mat in text.",
	long_description=long_description,
	long_description_content_type="text/markdown",
	url="https://github.com/qxtony/filtermat",
	packages=find_packages(),
	install_requires=requirements,
	classifiers=[
		"Programming Language :: Python :: 3.8",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
	],
	python_requires='>=3.6',
)

