from setuptools import find_packages, setup

setup(
    name="fossd",
    version="0.1.0",
    packages=find_packages(exclude=("tests",)),
    entry_points={
        "console_scripts": [
            "foss-decrypt=fossd.cli:decrypt",
            "foss-encrypt=fossd.cli:encrypt",
        ]
    },
    install_requires=["cryptography", "click"],
)
