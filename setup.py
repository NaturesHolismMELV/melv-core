"""
Setup configuration for MELV-Core package.

Install with: pip install -e .
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="melv-core",
    version="0.1.0",
    author="Zaid Osman",
    author_email="zaid@ecotao.com",  # Update with actual email
    description="Mathematical Ecology of Cooperation - Calculate cooperation dynamics",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/YOUR-USERNAME/melv-core",  # Update after creating repo
    project_urls={
        "Bug Tracker": "https://github.com/YOUR-USERNAME/melv-core/issues",
        "Documentation": "https://github.com/YOUR-USERNAME/melv-core",
        "Source Code": "https://github.com/YOUR-USERNAME/melv-core",
    },
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Education",
        "Topic :: Scientific/Engineering :: Mathematics",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.8",
    install_requires=[
        "numpy>=1.23.0",
        "scipy>=1.9.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0",
            "pytest-cov>=3.0",
        ],
        "tutorials": [
            "jupyter>=1.0",
            "matplotlib>=3.5.0",
            "pandas>=1.5.0",
        ],
    },
    keywords="cooperation, ecology, mathematics, MELV, interaction-factor, systems-theory",
    license="MIT",
)
