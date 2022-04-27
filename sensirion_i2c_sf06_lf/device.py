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

from sensirion_i2c_adapter.transfer import execute_transfer
from sensirion_driver_support_types.mixin_access import MixinAccess
from sensirion_i2c_sf06_lf.commands import (EnterSleep, ExitSleep, ReadMeasurementDataRaw, ReadProductIdentifier,
                                            ReadProductIdentifierPrepare, ReadThermalConductivityMeasurementData,
                                            StartH2oContinuousMeasurement, StartIpaContinuousMeasurement,
                                            StartSingleThermalConductivityMeasurementAsync,
                                            StartSingleThermalConductivityMeasurementSync, StopContinuousMeasurement)

from sensirion_i2c_sf06_lf.result_types import (SignalDeltaTemperature, SignalFlow, SignalTemperature,
                                                SignalThermalConductivity)


class Sf06LfDeviceBase:
    """Low level API implementation of SF06-LF"""
    def __init__(self, channel):
        self._channel = channel

    @property
    def channel(self):
        return self._channel

    def start_h2o_continuous_measurement(self):
        """
        Starts continuous measurement mode using calibration values for H₂O.
        The sensor measures both the flow rate and the temperature. After the command has been sent, the chip
        continuously measures and updates the measurement results which can be read with *read_measurement_data_raw*.
        """
        transfer = StartH2oContinuousMeasurement()
        return execute_transfer(self._channel, transfer)

    def start_ipa_continuous_measurement(self):
        """
        Starts continuous measurement mode using calibration values for Isopropyl alcohol.
        The sensor measures both the flow rate and the temperature. After the command has been sent, the chip
        continuously measures and updates the measurement results which can be read with *read_measurement_data_raw*.
        Supported by products: SLF3C-1300F, SLF3S-1300F, SLF3S-0600F, SLF3S-4000B
        """
        transfer = StartIpaContinuousMeasurement()
        return execute_transfer(self._channel, transfer)

    def read_measurement_data_raw(self):
        """
        After the command *start_xx_continuous_measurement* has been sent, the chip continuously measures and updates
        the measurement results. New results (flow, temperature, and signaling flags) can be read continuously
        with this command.

        :return raw_flow:
            For SLF3C-1300F, SLF3S-1300F convert to ml/min by applying: flow = raw_flow / 500
            For SLF3S-4000B convert to ml/min by applying: flow = raw_flow / 32
            For SLF3S-0600F convert to μl/min by applying: flow = raw_flow / 10
            For LD20-0600L convert to ml/h by applying: flow = raw_flow / 1200
            For LD20-2600B convert to ml/h by applying: flow = raw_flow / 20
        :return raw_temperature:
            Convert to degrees celsius by temperature = raw_temperature / 200
        :return signaling_flags:
            Gives additional information about the measurement status. Refer to the
            sensor data sheet for detailed information. Following flags are defined:
            Air-in-Line flag (Bit 0), High Flow flag (Bit 1), Exponential smoothing active (Bit 5)
        """
        transfer = ReadMeasurementDataRaw()
        return execute_transfer(self._channel, transfer)

    def stop_continuous_measurement(self):
        """
        This command stops the continuous measurement and puts the sensor in idle mode.
        After it receives the stop command, the sensor needs up to 0.5ms to power down the heater,
        enter idle mode and be receptive for a new command.
        """
        transfer = StopContinuousMeasurement()
        return execute_transfer(self._channel, transfer)

    def start_single_thermal_conductivity_measurement_sync(self):
        """
        This command starts one thermal conductivity measurement and blocks for 2.3 seconds
        until the measurement results are ready.
        After completion of the measurement, the heater is switched off and the sensor enters idle mode and the results
        can be read anytime with *read_thermal_conductivity_measurement_data*.
        The sensor measures the thermal conductivity, the sensor temperature, and the
        delta-temperature (a measure for the temperature difference between the liquid and the sensor).
        Supported by products: SLF3C-1300F, SLF3S-4000B
        """
        transfer = StartSingleThermalConductivityMeasurementSync()
        return execute_transfer(self._channel, transfer)

    def start_single_thermal_conductivity_measurement_async(self):
        """
        This command starts one thermal conductivity measurement and returns immediately.
        Note that the sensor does not accept any other commands while the measurement is running, which takes
        approximately 2.3 seconds.
        After completion of the measurement, the heater is switched off and the sensor enters idle mode and the results
        can be read anytime with *read_thermal_conductivity_measurement_data*.
        The sensor measures the thermal conductivity, the sensor temperature, and the
        delta-temperature (a measure for the temperature difference between the liquid and the sensor).
        Supported by products: SLF3C-1300F, SLF3S-4000B
        """
        transfer = StartSingleThermalConductivityMeasurementAsync()
        return execute_transfer(self._channel, transfer)

    def read_thermal_conductivity_measurement_data(self):
        """
        Reads single thermal conductivity measurement after a measurement has been started with
        *start_single_thermal_conductivity_measurement_sync* or *start_single_thermal_conductivity_measurement_async*.
        Supported by products: SLF3C-1300F, SLF3S-4000B

        :return thermal_conductivity:
            Thermal conductivity signal read from the sensor in arbitary units.
        :return raw_temperature:
            Calibrated raw temperature signal read from the sensor.
        :return raw_delta_temperature:
            Calibrated raw delta temperature signal read from the sensor.
        """
        transfer = ReadThermalConductivityMeasurementData()
        return execute_transfer(self._channel, transfer)

    def enter_sleep(self):
        """
        In sleep mode the sensor uses a minimum amount of power. The mode can only be entered from idle mode,
        i.e. when the sensor is not measuring.
        This mode is particularly useful for battery operated devices. To minimize the current in this mode,
        the complexity of the sleep mode circuit has been reduced as much as possible, which is mainly reflected by
        the way the sensor exits the sleep mode. In sleep mode the sensor cannot be soft reset.
        Supported by products: LD20-0600L, LD20-2600B
        """
        transfer = EnterSleep()
        return execute_transfer(self._channel, transfer)

    def exit_sleep(self):
        """
        The sensor exits the sleep mode and enters the idle mode when it receives the valid I2C address and a write
        bit (‘0’).
        Note that the I2C address is not acknowledged. It is necessary to poll the sensor to see whether the sensor has
        received the address and has woken up. This should take typically 25ms.
        Supported by products: LD20-0600L, LD20-2600B
        """
        transfer = ExitSleep()
        return execute_transfer(self._channel, transfer)

    def read_product_identifier_prepare(self):
        """
        Prepare to read the product identifier and the serial number.
        The command can only be executed from the idle mode, i.e. when the sensor is not performing measurements.
        """
        transfer = ReadProductIdentifierPrepare()
        return execute_transfer(self._channel, transfer)

    def read_product_identifier(self):
        """
        This command allows to read product identifier and the serial number.
        The command can only be executed from the idle mode, i.e. when the sensor is not performing measurements
        and *read_product_identifier_prepare* is called before.

        :return product_identifier:
            Note that the last 8 bits are the sensor’s revision number and are subject to change in case of an
            update of the specifications.
        :return serial_number:
            64-bit unique serial number
        """
        transfer = ReadProductIdentifier()
        return execute_transfer(self._channel, transfer)


class Sf06LfDevice(Sf06LfDeviceBase):
    """Driver class implementation of SF06-LF"""
    sf06_lf = MixinAccess()

    def __init__(self, channel):
        super().__init__(channel)

    def read_measurement_data(self, inv_flow_scale_factor):
        """
        Reads the raw measurement values and converts them to their physcial units where applicable.
        For the flow the scaling factor and resulting flow unit depends on the specific sensor.
        The scaling factor is passed as an argument and the raw flow value is converted by applying:
        flow = raw_flow / inv_flow_scale_factor
        The scaling factors for the supported sensor are defined in enum *inv_flow_scale_factors*

        :param inv_flow_scale_factor:
            used to convert raw flow value

        :return a_flow:
            As the flow scaling differs for specific sensor types the scaling factor
            must be passed as an argument. See the enum *inv_flow_scale_factors* for
            scaling factors of supported sensors.
            The raw value is converted by: flow = raw_flow / inv_flow_scale_factor
            Resulting unit depends on your specific sensor type.
        :return a_temperature:
            temperature in degree celsius
        :return a_signaling_flags:

        """
        (raw_flow, raw_temp, signaling_flags
         ) = self.sf06_lf.read_measurement_data_raw()
        return (SignalFlow(raw_flow, inv_flow_scale_factor), SignalTemperature(raw_temp), signaling_flags)

    def read_thermal_conductivity_measurement_data(self):
        """
        Reads single thermal conductivity measurement after a measurement has been started with
        *start_single_thermal_conductivity_measurement*.
        Supported by products: SLF3C-1300F, SLF3S-4000B

        :return a_thermal_conductivity:
            thermal conductivity in arbitary unit
        :return a_temperature:
            temperature in degree celsius
        :return a_delta_temperature:
            delta temperature in degree celsius
        """
        (th_cond, raw_temp, raw_delta_temp
         ) = self.sf06_lf.read_thermal_conductivity_measurement_data()
        return (SignalThermalConductivity(th_cond), SignalTemperature(raw_temp),
                SignalDeltaTemperature(raw_delta_temp))

    def read_product_identifier(self):
        """
        Read product identifier and the serial number.
        The command can only be executed from the idle mode, i.e. when the sensor is not performing measurements.

        :return product_identifier:
            Note that the last 8 bits are the sensor’s revision number and are subject to change in case of an
            update of the specifications.
        :return serial_number:
            64-bit unique serial number
        """
        self.sf06_lf.read_product_identifier_prepare()
        return self.sf06_lf.read_product_identifier()
