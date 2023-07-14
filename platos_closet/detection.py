import numpy as np

class Planet:
    """
    Defines a set of parameters for planets in our solar system.

    Args:
        name (str): Name of the planet.
        depth (int): Transit depth in ppm.
        duration (int): Transit duration in hours.
        number (int): Number of transits.
    """

    def __init__(self, name, depth, duration, number=3):
        """
        Initializes a planet object.

        Args:
            name (str): Name of the planet.
            depth (int): Transit depth in parts per million (ppm).
            duration (int): Transit duration in hours.
            number (int): Number of transits.
        """
        self.name = name
        self.depth = depth
        self.duration = duration
        self.number = number

    def noise_level(self, eta=7.1):
        """
        Calculates the noise level of the planet transit signal at detector level.

        Args:
            eta (float, optional): Statistical significance value adopted for PLATO.
                Defaults to 7.1.

        Returns:
            float: The noise level of the planet transit signal at detector level.
        """
        nsr = self.depth * np.sqrt(self.duration * self.number) / eta
        return nsr

    def is_detectable(self, nsr, nsr_plato=34):
        """
        Determines if the planet is detectable based on the noise level.

        Args:
            nsr (float): Noise level of the planet transit signal at detector level.
            nsr_plato (float, optional): Threshold noise level for detection.
                Defaults to 34 ppm sqrt(hr).

        Returns:
            str: 'Detectable planet' or 'Non-detectable planet'.
        """
        if nsr > nsr_plato:
            return 'Detectable planet'
        else:
            return 'Non-detectable planet'

    def detectability_check(self):
        """
        Performs the detectability check for an array of planet data.

        Args:
            planets_data (list): List of tuples containing planet data
                in the format (name, depth, duration).

        Returns:
            None. Prints the detection results on the screen.
        """
        nsr = self.noise_level()
        detection_result = self.is_detectable(nsr)
        print(f"{self.name}: {detection_result}")
        