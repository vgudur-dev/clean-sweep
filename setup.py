from setuptools import setup, find_packages

setup(
    name="clean-sweep",
    version="0.1.0",
    description="Digital clutter cleaner – find duplicates and reclaim disk space",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="CleanSweep Contributors",
    license="Apache-2.0",
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "cleansweep=clean_sweep.cli:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)
