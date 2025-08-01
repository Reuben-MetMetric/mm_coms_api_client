from setuptools import setup, find_packages

# Read the README file
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="mmComsClient",
    version="0.1.0",
    author="Reuben",
    author_email="reuben@metmetric.co.za",
    description="Python client for MetMetric Communications API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Reuben-MetMetric/mm_coms_api_client",
    project_urls={
        "Bug Tracker": "https://github.com/Reuben-MetMetric/mm_coms_api_client/issues",
        "Repository": "https://github.com/Reuben-MetMetric/mm_coms_api_client",
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    packages=find_packages(),
    python_requires=">=3.7",
    install_requires=[
        "requests>=2.25.0",
    ],
    include_package_data=True,
)