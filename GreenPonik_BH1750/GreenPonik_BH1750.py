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


class GreenPonik_BH1750:
    # Constants taken from the datasheet
    DEFAULT_BUS = 1
    DEFAULT_ADDR = 0x23       # Default device I2C address
    # _POWER_DOWN = 0x00   # No active state
    # _POWER_ON = 0x01     # Power on
    # _RESET = 0x07        # Reset data register value
    # # Start measurement at 4 lx resolution. Time typically 16ms.
    # _CONTINUOUS_LOW_RES_MODE = 0x13
    # # Start measurement at 1 lx resolution. Time typically 120ms
    # _CONTINUOUS_HIGH_RES_MODE_1 = 0x10
    # # Start measurement at 0.5 lx resolution. Time typically 120ms
    # _CONTINUOUS_HIGH_RES_MODE_2 = 0x11
    # # Start measurement at 1 lx resolution. Time typically 120ms
    # # Device is automatically set to Power Down after measurement.
    # _ONE_TIME_HIGH_RES_MODE_1 = 0x20
    # # Start measurement at 0.5 lx resolution. Time typically 120ms
    # # Device is automatically set to Power Down after measurement.
    # _ONE_TIME_HIGH_RES_MODE_2 = 0x21
    # # Start measurement at 1 lx resolution. Time typically 120ms
    # # Device is automatically set to Power Down after measurement.
    # _ONE_TIME_LOW_RES_MODE = 0x23

    def __init__(self, bus=None):
        self._bus = bus if None is not bus else self.DEFAULT_BUS

    @property
    def bus(self):
        return self._bus

    def _convert_to_number(self, data):
        # Simple function to convert 2 bytes of data
        # into a decimal number
        return ((data[1] + (256 * data[0])) / 1.2)

    def read_bh1750(self, addr=DEFAULT_ADDR):
        try:
            # data = bus.read_i2c_block_data(addr, \
            # self._ONE_TIME_HIGH_RES_MODE_2)
            # lux = self._convertToNumber(data)
            with I2C(self._bus) as i2c:
                buffer = bytearray(1)
                bh = i2c.readfrom_into(addr, buffer)
                lux = bh
                print('Light: %.3f lx' % lux)
                return lux
        except BaseException as e:
            print('cannot read bh1750')
            print('An exception occurred: {}'.format(e))
