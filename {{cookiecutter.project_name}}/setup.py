import os
import sys
import re

version_re = re.compile("""__version__[\s]*=[\s]*['|"](.*)['|"]""")

with open("{{cookiecutter.project_name}}.py") as f:
    content = f.read()
    match = version_re.search(content)
    version = match.group(1)

readme = os.path.join(os.path.dirname(__file__), "README.md")
with open(readme) as f:
    long_description = f.read()

SETUP_ARGS = dict(
    name="{{cookiecutter.project_name}}.py",
    version=version
    descriptions=("Description of {{cookiecutter.project_name}}"),
    long_description=long_description,
    url="https://github.com/<login>/{{cookiecutter.project_name}},
    author="<AUTHOR>",
    email="<EMAIL>",
    license="MIT",
    include_package_data=True,
    classifiers = [
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.8"
    ],
    py_modules = ["{{cookiecutter.project_name}}"],
    install_requires = [
        "requests>=2.22"
    ]
)


if __name__ == "__main__":
    from setuptools import setup, find_packages

    SETUP_ARGS["packages"] = find_packages()
    setup(**SETUP_ARGS)