import os
import setuptools
from pathlib import Path

__VERSION__ = (Path(__file__).parent / ".github/scripts/__VERSION__").read_text()
long_description = Path("README.md").read_text()

setuptools.setup(
    name="vule-magics",
    version=__VERSION__,
    author="Le Tuan Vu",
    author_email="ltnv24@gmail.com",
    description="Vu's custom magic commands",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=['vule_sparkmagic'],
    install_requires=['ipython', 'pyspark'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.9',
)