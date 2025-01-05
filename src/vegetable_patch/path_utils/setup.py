from setuptools import setup, find_packages

setup(
    name="project",
    version="0.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[],  # List dependencies if needed
)
