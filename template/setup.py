#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open("README.rst") as readme_file:
    readme = readme_file.read()

requirements = [
    "click>=7.0",
]

setup(
    author="{{ username }}",
    author_email="{{ author_email }}",
    python_requires=">=3.8",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
    ],
    description="{{ project_description }}",
    entry_points={
        "console_scripts": ["{{ project_slug }}={{ project_snake }}.cli:main",],
    },
    install_requires=requirements,
    long_description=readme,
    include_package_data=True,
    keywords="{{ project_snake }}",
    name="{{ project_snake }}",
    packages=find_packages(include=["{{ project_snake }}", "{{ project_snake }}.*"]),
    url="https://github.com/{{ github_username }}/{{ project_snake }}",
    version="0.1.0",
    zip_safe=False,
)
