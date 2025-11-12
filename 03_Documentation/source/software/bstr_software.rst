=========================================
BSTR Arduino Control Script
=========================================

Overview
========

This Arduino script controls a Batch Stirred Tank Reactor (BSTR) photoreactor system by managing digital output pins for precise timing sequences.

Arduino Code
============

.. code-block:: cpp

    int A;
    int B;
    int C;
    int D;

    void setup() {
        pinMode(2, OUTPUT);
        pinMode(3, OUTPUT);
        pinMode(4, OUTPUT);
    }

    void loop() {
        A = (10UL * 1UL * 1000UL);
        B = (10UL * 1UL * 1000UL);
        D = (10UL * 1UL * 1000UL);
        
        digitalWrite(2, HIGH);
        digitalWrite(3, LOW);
        digitalWrite(4, LOW);
        delay(A);
        
        digitalWrite(2, LOW);
        digitalWrite(3, HIGH);
        delay(B);
        
        digitalWrite(2, HIGH);
        digitalWrite(3, LOW);
        delay(A);
        
        digitalWrite(2, LOW);
        digitalWrite(4, HIGH);
        delay(D);
        
        digitalWrite(4, LOW);
        digitalWrite(7, HIGH);
        delay(60UL * 12UL * 1000UL);
        
        digitalWrite(7, LOW);
        digitalWrite(LED_BUILTIN, HIGH);
    }

Code Description
================

**Pin Configuration:**

* Pin 2: Output control
* Pin 3: Output control  
* Pin 4: Output control
* Pin 7: Output control (activated later in sequence)
* LED_BUILTIN: Status indicator

**Timing Parameters:**

* Variable A: 10 seconds (10 × 1 × 1000 ms)
* Variable B: 10 seconds (10 × 1 × 1000 ms)
* Variable D: 10 seconds (10 × 1 × 1000 ms)
* Final delay: 12 minutes (60 × 12 × 1000 ms)

**Operation Sequence:**

1. Pin 2 HIGH, Pins 3 and 4 LOW for duration A
2. Pin 2 LOW, Pin 3 HIGH for duration B
3. Pin 2 HIGH, Pin 3 LOW for duration A
4. Pin 2 LOW, Pin 4 HIGH for duration D
5. Pin 4 LOW, Pin 7 HIGH for 12 minutes
6. Pin 7 LOW, Built-in LED HIGH (completion indicator)
