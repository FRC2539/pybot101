from wpilib.analoginput import AnalogInput

class AnalogUltrasonic(AnalogInput):
    '''Simple wrapper to treat an analog signal like a distance sensor.'''

    def __init__(self, channel):
        super().__init__(channel)

        self.scalingFactor = 1


    def getDistance(self):
        return self.getAverageVoltage() * self.scalingFactor
