## Setup.py for codeastro project
from setuptools import setup, find_packages

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
	name = "platos_closet",

	version = "1.1.4",
 
	author = "Fernando Gutierrez Canales and John Hood",
 
	author_email = "fernando.canales@obspm.fr",
 
	description = "Package that tells the user if a planet can be detected by PLATO space mission",

	long_description= """
 	===============================================================================
  							PLATO'S CLOSET
 	===============================================================================

  	Overview

	Plato's Closet provides astronomers and researchers with tools to assess whether
	planets of our Solar System meet the detection criteria for the PLATO (PLAnetary Transits and Oscillations of stars)
	space mission. The package calculates noise levels and determines detectability based
	on mission parameters.

	Features

	- Calculate noise levels for planetary transits
	- Determine detectability based on PLATO mission specifications
	- Simple, intuitive API with a Planet class
	- Customizable detection thresholds

	Installation

	pip install platos_closet
  	 """,
	long_description_content_type="text/plain",
	
 	license = "MIT",
 
 	url = "https://github.com/Fernando-Canales/platos_closet",
 
	packages=find_packages(),
     classifiers=[
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
     
    install_requires=required,

	)
