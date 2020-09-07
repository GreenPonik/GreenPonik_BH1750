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

import board
import busio


class GreenPonik_BH1750:
    # Constants taken from the datasheet
    DEFAULT_ADDR = 0x23       # Default device I2C address
    _POWER_DOWN = 0x00   # No active state
    _POWER_ON = 0x01     # Power on
    _RESET = 0x07        # Reset data register value
    # Start measurement at 4 lx resolution. Time typically 16ms.
    _CONTINUOUS_LOW_RES_MODE = 0x13
    # Start measurement at 1 lx resolution. Time typically 120ms
    _CONTINUOUS_HIGH_RES_MODE_1 = 0x10
    # Start measurement at 0.5 lx resolution. Time typically 120ms
    _CONTINUOUS_HIGH_RES_MODE_2 = 0x11
    # Start measurement at 1 lx resolution. Time typically 120ms
    # Device is automatically set to Power Down after measurement.
    _ONE_TIME_HIGH_RES_MODE_1 = 0x20
    # Start measurement at 0.5 lx resolution. Time typically 120ms
    # Device is automatically set to Power Down after measurement.
    _ONE_TIME_HIGH_RES_MODE_2 = 0x21
    # Start measurement at 1 lx resolution. Time typically 120ms
    # Device is automatically set to Power Down after measurement.
    _ONE_TIME_LOW_RES_MODE = 0x23

    def __init__(self, scl_pin=None, sda_pin=None):
        self._scl_pin = scl_pin if None is not scl_pin else board.SCL
        self._sda_pin = sda_pin if None is not sda_pin else board.SDA

    def _convert_to_number(self, data):
        # Simple function to convert 2 bytes of data
        # into a decimal number
        return ((data[1] + (256 * data[0])) / 1.2)

    def read_bh1750(self, addr=DEFAULT_ADDR):
        try:
            # bus = smbus.SMBus(0)    # Rev 1 Pi uses 0
            # bus = smbus.SMBus(1)    # Rev 2 Pi uses 1
            # data = bus.read_i2c_block_data(addr, \
            # self._ONE_TIME_HIGH_RES_MODE_2)
            # lux = self._convertToNumber(data)
            i2c = busio.I2C(self._scl_pin, self._sda_pin)
            buffer = bytearray(1)
            bh = i2c.readfrom_into(addr, buffer)
            lux = bh
            print('light: %.3f lx' % lux)
            i2c.deinit()
            return lux
        except BaseException as e:
            print('cannot read bh1750')
            print('An exception occurred: {}'.format(e))
