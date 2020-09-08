#! /usr/bin/env python3

"""
####################################################################
####################################################################
####################### GreenPonik_BH1750 ##########################
####################### Read BH1750 sensor #########################
#################### with Python3 through i2c ######################
####################################################################
####################################################################
"""

from adafruit_extended_bus import ExtendedI2C as I2C
import adafruit_bh1750


class GreenPonik_BH1750:

    DEFAULT_ADDR = 0x23
    DEFAULT_BUS = 1

    def __init__(self, bus=None):
        self._bus = bus if None is not bus else self.DEFAULT_BUS

    @property
    def bus(self):
        return self._bus

    def read_bh1750(self, addr=DEFAULT_ADDR):
        """
        @brief Read bh1750 raspberry pi i2c bus
        Get lux
        """
        try:
            with I2C(self._bus) as i2c:
                sensor = adafruit_bh1750.BH1750(i2c)
                lux = sensor.lux
                print('Light: %.3f lx' % lux)
                return lux
        except BaseException as e:
            print('cannot read bh1750')
            print('An exception occurred: {}'.format(e))
