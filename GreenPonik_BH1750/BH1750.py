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


class BH1750:

    DEFAULT_ADDR = 0x23
    DEFAULT_BUS = 1

    def __init__(self, bus=DEFAULT_BUS, addr=DEFAULT_ADDR):
        self._bus = bus
        self._addr = addr
        self._debug = False

    def __enter__(self):
        """Context manager enter function."""
        # Just return this object so it can be used in a with statement, like
        # with WaterPumpDriver(bus=1, addr=100) as driver:
        #     # do stuff!
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit function, ensures resources are cleaned up."""
        return False  # Don't suppress exceptions.

    @property
    def bus(self):
        return self._bus

    @property
    def address(self):
        return self._addr

    @property
    def debug(self):
        return self._debug

    @debug.setter
    def debug(self, d):
        self._debug = d

    def read_bh1750(self):
        """
        @brief Read bh1750 raspberry pi i2c bus
        Get lux
        """
        try:
            with I2C(self._bus) as i2c:
                sensor = adafruit_bh1750.BH1750(i2c, address=self._addr)
                lux = sensor.lux
                if self._debug:
                    print('Light: %.3f lx' % lux)
                return lux
        except Exception as e:
            print('cannot read bh1750, An exception occurred: {}'.format(e))
