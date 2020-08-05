#! /usr/bin/env python3

"""
####################################################################
####################################################################
####################### GreenPonik_TSL2561 #########################
####################### Read TSL2561 sensor ########################
#################### with Python3 through i2c ######################
####################################################################
####################################################################
"""

import time
import board
import busio
import adafruit_tsl2561


def read_tsl2561():
    """
    @brief Read tsl 2561 sensor on raspberry pi i2c bus
    Get light spectre data
    """
    try:
        # Create the I2C bus
        i2c = busio.I2C(board.SCL, board.SDA)
        # Create the TSL2561 instance, passing in the I2C bus
        tsl = adafruit_tsl2561.TSL2561(i2c)
        # Print chip info
        print("Chip ID = {}".format(tsl.chip_id))
        print("Enabled = {}".format(tsl.enabled))
        print("Gain = {}".format(tsl.gain))
        print("Integration time = {}".format(tsl.integration_time))
        print("Configuring TSL2561...")
        print("Configuring TSL2561...")
        # Enable the light sensor
        tsl.enabled = True
        time.sleep(1)
        # Set gain 0=1x, 1=16x
        tsl.gain = 0
        # Set integration time (0=13.7ms, 1=101ms, 2=402ms, or 3=manual)
        tsl.integration_time = 1
        # print("Getting readings...")
        print("Getting readings....")
        # Get raw (luminosity) readings individually
        broadband = tsl.broadband
        infrared = tsl.infrared
        # Get raw (luminosity) readings using tuple unpacking
        # broadband, infrared = tsl.luminosity
        # Get computed lux value (tsl.lux can return None or a float)
        lux = tsl.lux
        # Print results
        # print("Enabled = {}".format(tsl.enabled))
        print("Enabled = {}".format(tsl.enabled))
        # print("Gain = {}".format(tsl.gain))
        print("Gain = {}".format(tsl.gain))
        # print("Integration time = {}".format(tsl.integration_time))
        print("Integration time = {}".format(tsl.integration_time))
        # print("Broadband = {}".format(broadband))
        print("Broadband = {}".format(broadband))
        # print("Infrared = {}".format(infrared))
        print("Infrared = {}".format(infrared))
        # if lux is not None:
        #    print("Lux = {}".format(lux))
        # else:
        #    print("Lux value is None. Possible \
        # sensor underrange or overrange.")
        # Disble the light sensor (to save power)
        tsl.enabled = False
        print('read light data: ')
        print(lux)
        print(infrared)
        print(broadband)
        return lux, infrared, broadband
    except BaseException as e:
        print('An exception occurred: {}'.format(e))