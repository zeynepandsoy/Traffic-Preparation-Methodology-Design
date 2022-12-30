from setuptools import find_packages, setup

#setup(
#    name='comp0035-cw-2022-23',
#    version='1.0.0',
#   packages=find_packages(),
#    include_package_data=True,
#    zip_safe=False,
#    install_requires=[
#        'pandas',
#        'seaborn'
#        'numpy',
#        'matplotlib',
#        'openpyxl'
#    ],
#)

setup(
name="comp0035-cw2",
version="1.0.0",
packages=["src"],
package_dir={
"src": "./coursework2/src",
},
include_package_data=True,
zip_safe=False,
install_requires=[],
)