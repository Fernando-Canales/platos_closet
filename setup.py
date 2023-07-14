## Setup.py for codeastro project
from setuptools import setup, find_packages

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
	name = "platos_closet",

	version = "1.1.1",
 
	author = "Fernando Gutierrez Canales and John Hood",
 
	author_email = "fernando.canales@obspm.fr",
 
	description = "Package that tells the user if a planet can be detected by PLATO space mission",

	long_description= """ The Planet class requires the following arguments for initialization
	- name (str): Name of the planet.
	- depth (int): Transit depth of the planet in parts per million (ppm).
	- duration (int): Transit duration of the planet in hours.
	- number (int, optional): Number of transits. Defaults to 3 if not provided.

	The Planet class provides the following methods:

	- noise_level(eta=7.1): Calculates the noise level of the planet transit signal at the detector level. The eta parameter is an optional statistical significance value (default: 7.1). Returns the calculated noise level as a float.

	- is_detectable(nsr, nsr_plato=34): Determines if the planet is detectable based on the noise level (nsr). The nsr_plato parameter is an optional threshold noise level for detection (default: 80). Returns a string indicating whether the planet is detectable or not.

	To use the package, create an instance of the Planet class by providing the required arguments (name, depth, and duration). Then, you can call the noise_level method to calculate the noise level and the is_detectable method to determine the detectability of the planet.

	Example usage: 
 
 	from package_name import Planet

	earth = Planet('Earth', 84, 13)
	nsr = earth.noise_level()
	detection_result = earth.is_detectable(nsr)
	print(f"{earth.name}: {detection_result}") """,
	
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