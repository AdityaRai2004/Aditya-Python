from setuptools import setup, find_packages

setup(
    name="my_package",                # Package name
    version="0.1",                    # Version number
    author="Your Name",               # Author name
    description="A simple test package", # Description of the package
    packages=find_packages(),         # Automatically find sub-packages
    install_requires=[],              # Dependencies (empty for now)
)