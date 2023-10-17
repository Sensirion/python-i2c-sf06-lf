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
"""
The signal classes specify transformations of the raw sensor signals into a meaningful units.
The generated signal types are used by the driver class and not intended for direct use.
"""

from sensirion_driver_support_types.signals import AbstractSignal


class SignalFlow(AbstractSignal):
    """
    As the flow scaling differs for specific sensor types the scaling factor
    must be passed as an argument. See the enum *inv_flow_scale_factors* for
    scaling factors of supported sensors.
    The raw value is converted by: flow = raw_flow / inv_flow_scale_factor
    Resulting unit depends on your specific sensor type.
    """

    def __init__(self, raw_flow, inv_flow_scale_factor):
        self._flow = float(raw_flow)
        self._flow = self._flow / int(inv_flow_scale_factor)

    @property
    def value(self):
        return self._flow

    def __str__(self):
        return '{0:.2f}'.format(self.value)


class SignalTemperature(AbstractSignal):
    """temperature in degree celsius"""

    def __init__(self, raw_temperature):
        self._temperature = raw_temperature / 200.0

    @property
    def value(self):
        return self._temperature

    def __str__(self):
        return '{0:.2f}'.format(self.value)


class SignalDeltaTemperature(AbstractSignal):
    """delta temperature in degree celsius"""

    def __init__(self, raw_delta_temperature):
        self._delta_temperature = raw_delta_temperature / 1000.0

    @property
    def value(self):
        return self._delta_temperature

    def __str__(self):
        return '{0:.2f}'.format(self.value)


class SignalThermalConductivity(AbstractSignal):
    """thermal conductivity in arbitary unit"""

    def __init__(self, raw_thermal_conductivity):
        self._thermal_conductivity = raw_thermal_conductivity

    @property
    def value(self):
        return self._thermal_conductivity

    def __str__(self):
        return '{0}'.format(self.value)

