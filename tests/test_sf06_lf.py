#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# (c) Copyright 2023 Sensirion AG, Switzerland
#
#     THIS FILE IS AUTOMATICALLY GENERATED!
#
# Generator:     sensirion-driver-generator 0.32.0
# Product:       sf06_lf
# Model-Version: 1.1.0
#

import pytest
import time
from sensirion_i2c_driver.errors import I2cTimeoutError
from sensirion_i2c_sf06_lf.device import Sf06LfDevice

from sensirion_i2c_sf06_lf.commands import (InvFlowScaleFactors)


@pytest.fixture
def sensor(channel_provider):
    channel_provider.i2c_frequency = 100e3
    channel_provider.supply_voltage = 3.3
    with channel_provider:
        channel = channel_provider.get_channel(slave_address=0x08,
                                               crc_parameters=(8, 0x31, 0xff, 0x0))
        yield Sf06LfDevice(channel)


def test_stop_continuous_measurement1(sensor):
    sensor.stop_continuous_measurement()


def test_read_product_identifier1(sensor):
    (product_identifier, serial_number
     ) = sensor.read_product_identifier()
    print(f"product_identifier: {product_identifier}; "
          f"serial_number: {serial_number}; "
          )


def test_enter_sleep1(sensor):
    sensor.enter_sleep()
    sensor.exit_sleep()


def test_start_h2o_continuous_measurement1(sensor):
    sensor.start_h2o_continuous_measurement()
    time.sleep(0.1)
    (a_flow, a_temperature, a_signaling_flags
     ) = sensor.read_measurement_data(InvFlowScaleFactors.SLF3C_1300F)
    print(f"a_flow: {a_flow}; "
          f"a_temperature: {a_temperature}; "
          f"a_signaling_flags: {a_signaling_flags}; "
          )
    sensor.stop_continuous_measurement()


def test_start_ipa_continuous_measurement1(sensor):
    sensor.start_ipa_continuous_measurement()
    time.sleep(0.1)
    (a_flow, a_temperature, a_signaling_flags
     ) = sensor.read_measurement_data(InvFlowScaleFactors.SLF3C_1300F)
    print(f"a_flow: {a_flow}; "
          f"a_temperature: {a_temperature}; "
          f"a_signaling_flags: {a_signaling_flags}; "
          )
    sensor.stop_continuous_measurement()


def test_start_single_thermal_conductivity_measurement_async1(sensor, requires_hw):
    # as we currently cannot emulate the I2cTimeoutError on the mocked channel
    # the test runs only if HW is attached, which is checked by the requires_hw fixture
    sensor.start_single_thermal_conductivity_measurement_async()
    with pytest.raises(I2cTimeoutError):
        (a_thermal_conductivity, a_temperature, a_delta_temperature
         ) = sensor.read_thermal_conductivity_measurement_data()
        print(f"a_thermal_conductivity: {a_thermal_conductivity}; "
              f"a_temperature: {a_temperature}; "
              f"a_delta_temperature: {a_delta_temperature}; "
              )


def test_start_single_thermal_conductivity_measurement_sync1(sensor):
    sensor.start_single_thermal_conductivity_measurement_sync()
    (a_thermal_conductivity, a_temperature, a_delta_temperature
     ) = sensor.read_thermal_conductivity_measurement_data()
    print(f"a_thermal_conductivity: {a_thermal_conductivity}; "
          f"a_temperature: {a_temperature}; "
          f"a_delta_temperature: {a_delta_temperature}; "
          )
