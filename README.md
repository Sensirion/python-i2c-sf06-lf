# Python I2C Driver for Sensirion SF06-LF

This repository contains the Python driver to communicate with a Sensirion sensor of the SF06-LF family over I2C. 

<img src="https://raw.githubusercontent.com/Sensirion/python-i2c-sf06-lf/master/images/sensor_SLF3C_1300F.png"
    width="300px" alt="SF06-LF picture">


Click [here](https://sensirion.com/products/product-categories/liquid-flow/) to learn more about the Sensirion SF06-LF sensor family.


Not all sensors of this driver family support all measurements.
In case a measurement is not supported by all sensors, the products that
support it are listed in the API description.



## Supported sensor types

| Sensor name   | I²C Addresses  |
| ------------- | -------------- |
|[SLF3C-1300F](https://sensirion.com/products/catalog/SLF3C-1300F/)| **0x08**|
|[SLF3S-1300F](https://sensirion.com/products/catalog/SLF3S-1300F/)| **0x08**|
|[SLF3S-0600F](https://sensirion.com/products/catalog/SLF3S-0600F/)| **0x08**|
|[SLF3S-4000B](https://sensirion.com/products/catalog/SLF3S-4000B/)| **0x08**|
|[LD20-0600L](https://sensirion.com/products/catalog/LD20-0600L/)| **0x08**|
|[LD20-2600B](https://sensirion.com/products/catalog/LD20-2600B/)| **0x08**|

The following instructions and examples use a *SLF3C-1300F*.



## Connect the sensor

You can connect your sensor over a [SEK-SensorBridge](https://developer.sensirion.com/sensirion-products/sek-sensorbridge/).
For special setups you find the sensor pinout in the section below.

<details><summary>Sensor pinout</summary>
<p>
<img src="https://raw.githubusercontent.com/Sensirion/python-i2c-sf06-lf/master/images/SLF3x_Pinout.png"
     width="300px" alt="sensor wiring picture">

| *Pin* | *Cable Color* | *Name* | *Description*  | *Comments* |
|-------|---------------|:------:|----------------|------------|
| 1 |  | NC | Do not connect | 
| 2 | green | SDA | I2C: Serial data input / output | 
| 3 | red | VDD | Supply Voltage | 3.2V to 3.8V
| 4 | black | GND | Ground | 
| 5 | yellow | SCL | I2C: Serial clock input | 
| 6 |  | NC | Do not connect | 


</p>
</details>


## Documentation & Quickstart

See the [documentation page](https://sensirion.github.io/python-i2c-sf06-lf) for an API description and a 
[quickstart](https://sensirion.github.io/python-i2c-sf06-lf/execute-measurements.html) example.


## Contributing

We develop and test this driver using our company internal tools (version
control, continuous integration, code review etc.) and automatically
synchronize the `master` branch with GitHub. But this doesn't mean that we
don't respond to issues or don't accept pull requests on GitHub. In fact,
you're very welcome to open issues or create pull requests :-)

### Check coding style

The coding style can be checked with [`flake8`](http://flake8.pycqa.org/):

```bash
pip install -e .[test]  # Install requirements
flake8                  # Run style check
```

In addition, we check the formatting of files with
[`editorconfig-checker`](https://editorconfig-checker.github.io/):

```bash
pip install editorconfig-checker==2.0.3   # Install requirements
editorconfig-checker                      # Run check
```

## License

See [LICENSE](LICENSE).
