#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# (c) Copyright 2022 Sensirion AG, Switzerland
#
#     THIS FILE IS AUTOMATICALLY GENERATED!
#
# Generator:    sensirion-driver-generator 0.9.0
# Product:      sf06_lf
# Version:      1.0
#
import time

import pytest
from sensirion_i2c_driver import I2cConnection, CrcCalculator
from sensirion_i2c_driver.errors import I2cTimeoutError
from sensirion_shdlc_sensorbridge import (SensorBridgePort,
                                          SensorBridgeI2cProxy)
from sensirion_i2c_adapter.i2c_channel import I2cChannel
from sensirion_i2c_sf06_lf.device import Sf06LfDevice

from sensirion_i2c_sf06_lf.commands import (InvFlowScaleFactors)


@pytest.fixture
def sensor(bridge):
    # Configure SensorBridge port 1
    bridge.set_i2c_frequency(SensorBridgePort.ONE, frequency=100e3)
    bridge.set_supply_voltage(SensorBridgePort.ONE, voltage=3.3)
    bridge.switch_supply_on(SensorBridgePort.ONE)

    # Create SFM-Device device
    i2c_transceiver = SensorBridgeI2cProxy(bridge, port=SensorBridgePort.ONE)
    channel = I2cChannel(I2cConnection(i2c_transceiver),
                         slave_address=0x08,
                         crc=CrcCalculator(8, 0x31, 0xff, 0x0))
    dev = Sf06LfDevice(channel)
    yield dev
    # make sure the channel is powered off after executing tests
    bridge.switch_supply_off(SensorBridgePort.ONE)


@pytest.mark.needs_device
def test_stop_continuous_measurement1(sensor):
    sensor.stop_continuous_measurement()


@pytest.mark.needs_device
def test_read_product_identifier1(sensor):
    (product_identifier, serial_number
     ) = sensor.read_product_identifier()
    print(f"product_identifier: {product_identifier}; " f"serial_number: {serial_number}; ")


@pytest.mark.needs_device
def test_enter_sleep1(sensor):
    sensor.enter_sleep()
    sensor.exit_sleep()


@pytest.mark.needs_device
def test_start_h2o_continuous_measurement1(sensor):
    sensor.start_h2o_continuous_measurement()
    time.sleep(0.1)
    (a_flow, a_temperature, a_signaling_flags
     ) = sensor.read_measurement_data(InvFlowScaleFactors.SLF3C_1300F)
    print(f"a_flow: {a_flow}; " f"a_temperature: {a_temperature}; " f"a_signaling_flags: {a_signaling_flags}; ")
    sensor.stop_continuous_measurement()


@pytest.mark.needs_device
def test_start_ipa_continuous_measurement1(sensor):
    sensor.start_ipa_continuous_measurement()
    time.sleep(0.1)
    (a_flow, a_temperature, a_signaling_flags
     ) = sensor.read_measurement_data(InvFlowScaleFactors.SLF3C_1300F)
    print(f"a_flow: {a_flow}; " f"a_temperature: {a_temperature}; " f"a_signaling_flags: {a_signaling_flags}; ")
    sensor.stop_continuous_measurement()


@pytest.mark.needs_device
def test_start_single_thermal_conductivity_measurement_async1(sensor):
    sensor.start_single_thermal_conductivity_measurement_async()
    with pytest.raises(I2cTimeoutError):
        (_thermal_conductivity, _temperature, _delta_temperature
         ) = sensor.read_thermal_conductivity_measurement_data()


@pytest.mark.needs_device
def test_start_single_thermal_conductivity_measurement_sync1(sensor):
    sensor.start_single_thermal_conductivity_measurement_sync()
    (a_thermal_conductivity, a_temperature, a_delta_temperature
     ) = sensor.read_thermal_conductivity_measurement_data()
    print(f"a_thermal_conductivity: {a_thermal_conductivity}; " f"a_temperature: {a_temperature}; "
          f"a_delta_temperature: {a_delta_temperature}; ")

