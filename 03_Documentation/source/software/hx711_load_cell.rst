============================================================
HX711 Load Cell Project
============================================================

Project Overview
================

This project contains two Arduino sketches designed for the **Continuous Stirred Tank Reactor (CSTR)**. Both sketches utilize the HX711_ADC library to interface with HX711 load cell amplifiers for precise weight measurement and mass monitoring.

The project integrates an I2C Liquid Crystal Display (LCD) for real-time display of sensor readings and system status messages. All sketches are programmed using the Arduino IDE and require installation of the HX711_ADC and LiquidCrystal_I2C libraries.

System Components
=================

**Arduino Sketches:**

* Continuous Stirred Tank Reactor with automated inlet/outlet valve control

**Hardware Requirements:**

* HX711 Load Cell Amplifier
* Digital Load Cell Sensor (weight transducer)
* 16x2 I2C LCD Display
* Arduino microcontroller (compatible board)
* Inlet and outlet control valves
* Tare/reset button

**Software Libraries:**

* HX711_ADC - Load cell amplifier interface library
* LiquidCrystal_I2C - I2C LCD display control library
* Wire - Arduino I2C communication protocol

Dependencies and Installation
=============================

The following libraries are required for this project:

**HX711_ADC Library**

The HX711_ADC library provides the interface for communicating with HX711 load cell amplifiers. This library is licensed under the MIT License.

Repository: https://github.com/olkal/HX711_ADC

**LiquidCrystal_I2C Library**

The LiquidCrystal_I2C library enables control of 16x2 LCD displays via I2C protocol, simplifying wiring and communication.

Repository: https://github.com/johnrickman/LiquidCrystal_I2C.git

**Installation:**

Install both libraries through the Arduino IDE Library Manager or by cloning the repositories into your local Arduino libraries directory.

Features
========

**Load Cell Measurement:**

* Precise mass monitoring using HX711 amplifier
* Calibration support with standard weights
* Real-time weight display on LCD

**Display Interface:**

* 16x2 LCD display with I2C address configuration (0x27)
* Unit conversion (grams to ounces)
* Status messages and system feedback

**CSTR Automated Control:**

* Automatic inlet/outlet valve regulation based on mass thresholds
* Configurable weight setpoints
* Overload protection and alarm functionality

**Data Processing:**

* Weight filtering and stabilization
* Conversion between measurement units
* Threshold-based control logic

Project Structure
=================

The project consists of the following files:

* bstr.ino - Batch Stirred Tank Reactor control sketch
* cstr.ino - Continuous Stirred Tank Reactor control sketch
* readme.md - Project documentation

License
=======

The HX711_ADC library is licensed under the MIT License. Please refer to the library repository for detailed license information and terms.

Notes
=====

* Calibrate the load cell using a standard 100g weight before deployment
* Configure the I2C LCD address (default: 0x27) according to your hardware setup
* Adjust the calibration factor in the code based on your specific load cell specifications
* Ensure proper wiring of all I2C devices to avoid communication errors
* Use appropriate power supply ratings for the Arduino and peripheral devices
