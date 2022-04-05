Quick Start
===========

Execute measurements with SensorBridge
--------------------------------------

Installing the SensorBridge Driver
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
The driver for the `Sensirion SEK-SensorBridge`_ can be installed with

.. sourcecode:: bash

    pip install sensirion-shdlc-sensorbridge

.. _Sensirion SEK-SensorBridge: https://developer.sensirion.com/sensirion-products/sek-sensorbridge/


The following script shows how to use this driver on a Windows system using the `Sensirion SEK-SensorBridge`_ to
execute a simple measurement.

.. sourcecode:: python

.. literalinclude:: ../examples/example_sensorbridge_sf06_lf.py
    :language: python

The same sequence can be executed on a Linux system just by changing the name of the used COM-port.

Execute measurements using internal Linux I2c driver
----------------------------------------------------

On Linux systems (e.g. Raspberry-PI) it is furthermore possible to use the Linux user space I2c driver directly.
How this can be done is shown in the following script.

.. sourcecode:: python

.. literalinclude:: ../examples/example_linux_sf06_lf.py
    :language: python


