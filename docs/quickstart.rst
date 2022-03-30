Quick Start
===========

SensorBridge Setup
------------------

Following example shows how to instantiate this driver while a SF06-LF sensor is
connected to the computer using a `Sensirion SEK-SensorBridge`_.

The driver for the SensorBridge can be installed with

.. sourcecode:: bash

    pip install sensirion-shdlc-sensorbridge

.. _Sensirion SEK-SensorBridge: https://www.sensirion.com/sensorbridge/

SF06-LF
-------

.. sourcecode:: python

.. literalinclude:: ../examples/example_sensorbridge_sf06_lf.py
    :language: python



Execute measurements
--------------------

The following code except shows a simple measurement sequence using this driver.

.. literalinclude:: ../example_measurement_sf06_lf.py
    :language: python
