==================================================
CSTR Arduino Control System with Load Cell
==================================================

Overview
========

This Arduino sketch controls a Continuous Stirred Tank Reactor (CSTR) system with a digital weighing scale interface. It integrates a load cell (HX711 amplifier) for mass measurement and an LCD display for real-time monitoring, with automated inlet and outlet valve control based on weight thresholds.

Libraries and Components
=========================

**Required Libraries:**

* HX711_ADC - Load cell weight sensor interface
* Wire - I2C communication protocol
* LiquidCrystal_I2C - LCD display control via I2C

**Hardware Components:**

* HX711 Load Cell Amplifier (pins 4, 5)
* 16x2 LCD Display (I2C address 0x27)
* Inlet Valve Control (Pin 7)
* Outlet Valve Control (Pin 8)
* Tare Button (Pin 6, INPUT_PULLUP)

Arduino Code
============

.. code-block:: cpp

    #include <HX711_ADC.h>
    #include <Wire.h>
    #include <LiquidCrystal_I2C.h>  // LiquidCrystal_I2C library

    HX711_ADC LoadCell(4, 5);  // dt pin, sck pin
    LiquidCrystal_I2C lcd(0x27, 16, 2);  // LCD HEX address 0x27

    int taree = 6;
    int a = 0;
    float b = 0;
    int inlet = 7;
    int outlet = 8;

    void setup() {
        pinMode(inlet, OUTPUT);
        pinMode(outlet, OUTPUT);
        pinMode(taree, INPUT_PULLUP);

        LoadCell.begin();  // start connection to HX711
        LoadCell.start(1000);  // load cells get 1000ms of time to stabilize

        ///////////////////////////////////////////
        LoadCell.setCalFactor(375);  // Calibrate your LOAD CELL with 100g weight,
        // and change the value according to readings
        ///////////////////////////////////////////

        // initialize the LCD
        lcd.begin();  // begins connection to the LCD module
        lcd.backlight();  // turns on the backlight

        lcd.setCursor(1, 0);  // set cursor to first row
        lcd.print("Digital Scale ");  // print out to LCD

        lcd.setCursor(0, 1);  // set cursor to first row
        lcd.print(" SHIBU NASKAR ");  // print out to LCD

        delay(3000);
        lcd.clear();
    }

    void loop() {
        lcd.setCursor(1, 0);  // set cursor to first row
        lcd.print("Digital Scale ");  // print out to LCD

        LoadCell.update();  // retrieves data from the load cell
        float i = LoadCell.getData();  // get output value

        if (i < 0) {
            i = i * (-1);
            lcd.setCursor(0, 1);
            lcd.print(" ");
            lcd.setCursor(8, 1);
            lcd.print(" ");
        } else {
            lcd.setCursor(0, 1);
            lcd.print(" ");
            lcd.setCursor(8, 1);
            lcd.print(" ");

            lcd.setCursor(1, 1);  // set cursor to second row
            lcd.print(i);  // print out the retrieved value to the second row
            lcd.print("g ");

            float z = i / 28.3495;  // convert grams to ounces
            lcd.setCursor(9, 1);
            lcd.print(z, 2);
            lcd.print("oz ");

            if (i > 5000) {
                i = 0;
                lcd.setCursor(0, 0);  // set cursor to second row
                lcd.print(" Over loaded ");
                delay(200);
            }
        }

        // Control logic based on weight thresholds
        if (i > 20.5) {
            digitalWrite(outlet, HIGH);
            delay(10);
            digitalWrite(inlet, LOW);
            delay(800);

        } else if (i < 18.5) {
            digitalWrite(inlet, HIGH);
            delay(10);
            digitalWrite(outlet, LOW);
            delay(800);

        } else if (i >= 18.5 && i <= 20.5) {
            digitalWrite(outlet, HIGH);
            digitalWrite(inlet, HIGH);
            delay(800);

        } else {
            digitalWrite(outlet, LOW);
            digitalWrite(inlet, LOW);
            delay(800);
        }
    }

Code Description
================

**Pin Configuration:**

* Pin 4: HX711 Data (DT) Pin
* Pin 5: HX711 Clock (SCK) Pin
* Pin 6: Tare Button (INPUT_PULLUP)
* Pin 7: Inlet Valve Control (OUTPUT)
* Pin 8: Outlet Valve Control (OUTPUT)
* I2C LCD Address: 0x27

**Global Variables:**

* taree: Tare button pin assignment
* inlet: Inlet valve control pin
* outlet: Outlet valve control pin
* LoadCell: HX711 ADC object for weight measurement
* lcd: LiquidCrystal_I2C object for display control

**Calibration:**

* Load cell calibration factor: 375 (requires calibration with 100g standard weight)
* Adjust this value based on actual load cell readings

**Display Features:**

* Real-time weight display in grams (g) and ounces (oz)
* Conversion factor: 1 gram = 0.0353 ounces (using 28.3495 divisor)
* Two-line 16-character LCD display
* Overload warning when weight exceeds 5000g

**Control Logic - Weight Thresholds:**

* **Weight > 20.5g:** Outlet valve ON, inlet valve OFF (drain excess)
* **Weight < 18.5g:** Inlet valve ON, outlet valve OFF (fill to desired level)
* **Weight 18.5g - 20.5g:** Both valves ON (maintenance mode)
* **Other conditions:** Both valves OFF (standby)

**System Operation:**

The system maintains continuous stirred tank reactor operation by automatically controlling inlet and outlet flows based on reactor mass. The LCD display provides real-time feedback on system status, enabling monitoring of the CSTR process parameters.

**Timing and Delays:**

* 1000ms stabilization period for load cell after initialization
* 10ms valve actuation delay
* 800ms cycle delay between control checks
* 3000ms initial display splash screen
* 200ms overload condition delay
