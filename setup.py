from setuptools import setup, find_packages

setup(
    name="blockchain-research-system",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        line.strip()
        for line in open("requirements.txt").readlines()
    ],
    python_requires=">=3.8",
)