import numpy as np

class planets:
    """_Defines a set of parameters for planets in our solar system_

    Args:
        name (str): _name of the planet_
        depth (int): _transit depth in ppm_
        duration (int): _transit duration in hours_
        number (int): _number of transits_
    """
    def __init__(self, name, depth, duration, number=3):
        """
        name (str): _name of the planet_
        depth (int): _transit depth in parts per million(ppm)_
        duration (int): _transit duration in hours_
        number (int): _number of transits_
        """
        super().__init__()
        
        self.name = name
        self.depth = depth
        self.duration = duration
        self.number = number
        
    def noise_level(self, eta=7.1):
        """_Function that implements equation 23 in Marchiori et al (2019) paper_

        Args:
            eta (float, optional): _Statistical significance value adopted for PLATO_. Defaults to 7.1.

        Returns:
            _nsr_: _noise level of the planet transit signal at detector level_
        """
        nsr = self.depth * np.sqrt(self.duration * self.number) / eta
        return nsr
    
    def is_detectable(self, nsr, nsr_plato = 80):
        """_Function lets user know if object is detectable

        Args:
            nsr (int): _int value from .noise_level function_
        
        Returns:
            print statement of: 'Detectable planet' or 
            'Non detectable planet'
        """
        if nsr > nsr_plato:
            return print('Detectable planet')
        else:
            return print('Non detectable planet')