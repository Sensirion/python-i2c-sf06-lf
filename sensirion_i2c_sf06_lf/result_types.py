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

from sensirion_driver_support_types.signals import AbstractSignal


class SignalFlow(AbstractSignal):

    def __init__(self, raw_flow, inv_flow_scale_factor):
        self._flow = float(raw_flow)
        self._flow = self._flow / int(inv_flow_scale_factor)

    @property
    def value(self):
        return self._flow

    def __str__(self):
        return '{0:.2f}'.format(self.value)


class SignalTemperature(AbstractSignal):

    def __init__(self, raw_temperature):
        self._temperature = raw_temperature / 200.0

    @property
    def value(self):
        return self._temperature

    def __str__(self):
        return '{0:.2f}'.format(self.value)


class SignalDeltaTemperature(AbstractSignal):

    def __init__(self, raw_delta_temperature):
        self._delta_temperature = raw_delta_temperature / 1000.0

    @property
    def value(self):
        return self._delta_temperature

    def __str__(self):
        return '{0:.2f}'.format(self.value)


class SignalThermalConductivity(AbstractSignal):

    def __init__(self, raw_thermal_conductivity):
        self._thermal_conductivity = raw_thermal_conductivity

    @property
    def value(self):
        return self._thermal_conductivity

    def __str__(self):
        return '{0}'.format(self.value)

