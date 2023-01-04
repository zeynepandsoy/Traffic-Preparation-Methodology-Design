from setuptools import find_packages, setup

setup(
name="comp0035-cw2",
version="1.0.0",
packages=["src"],
package_dir={
"src": "./coursework2/src",
},
include_package_data=True,
zip_safe=False,
install_requires=[
        "pandas",
        "openpyxl",
        "matplotlib",
    ],
)
