from setuptools import setup

setup(
    name="convcolors",
    version="2.2.0",
    description="Convert colors between different color spaces.",
    long_description=open("README.rst").read(),
    long_description_content_type="text/x-rst",
    url="https://github.com/CairX/convert-colors-py",
    author="Thomas Cairns",
    author_email="thomas@cairns.se",
    license="MIT",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3",
        "Topic :: Multimedia :: Graphics :: Graphics Conversion",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities",
    ],
    python_requires=">=3.7",
    keywords="convert colors",
    packages=["convcolors"],
    extras_require={
        "dev": [
            "pytest ==5.4.3",
            "tox ==3.16.0",
            "yapf ==0.30.0",
        ]
    },
)
