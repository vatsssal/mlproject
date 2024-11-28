from setuptools import setup, find_packages

# Function to load requirements from requirements.txt
def parse_requirements(file_name):
    with open(file_name) as file:
        return [line.strip() for line in file if line.strip() and not line.startswith("-e.")]

setup(
    name="mypackage",
    version="0.1.1",
    author="Vatsal Trivedi",
    description="A sample package",
    packages=find_packages(),
    install_requires=parse_requirements("requirements.txt"),
)
