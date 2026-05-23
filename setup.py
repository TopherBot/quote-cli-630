from pathlib import Path
from setuptools import setup, find_packages

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding="utf8")

setup(
    name="quote-cli",
    version="0.1.0",
    description="Random inspirational quote CLI",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="TopherBot",
    packages=find_packages(exclude=("tests",)),
    entry_points={"console_scripts": ["quote-cli=quote_cli.__main__:main"]},
    python_requires=">=3.8",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
