Automated Batch Stirred Tank Reactor (ABSTR)
============================================

OVERVIEW
--------

The automated batch stirred tank reactor (ABSTR) is a software-controlled system that performs cyclic pump operations for continuous photoreactor processing. It sequentially delivers reaction mixture, collects product, washes with solvent, and repeats automatically. Programmable control enables precise timing, adaptable parameters, and reliable, continuous reactor operation.       

.. figure:: ../../../_static/shibu_figure/ABSTR.png
   :alt: complete image
   :width: 300px
   :align: center

   Figure 1: Complete diagram of the machine

MODULES USED
------------
:doc:`Time controller module <../modules/time_controller>`

.. figure:: ../../../_static/shibu_figure/time_controller.jpeg
   :alt: time controller module
   :width: 200px
   :align: center

:doc:`Transit Circuit <../modules/transit_ckt>`

.. figure:: ../../../_static/shibu_figure/transit_ckt.jpeg
   :alt: transit circuit module
   :width: 300px
   :align: center

:doc:`Power Supply <../components/12V_10A_powersupply>`

.. figure:: ../../../_static/shibu_figure/powersupply2.png
   :width: 200px
   :align: center


Connection Instructions
-----------------------
1.Connect the output terminal of the controller to the input terminal of the pump controller to enable software-based actuation.

2.Connect the output terminals of the pump controller individually to each pump for independent operation.

3.Connect the ground of each pump and combine them to form a common ground, then interface this common ground with the power supply ground.

4.Connect the power supply to the pump controller to provide stable operating power.

5.Connect the power supply to the timing controller module to ensure proper timing and sequencing functionality.

6.Refer to the block diagram provided below for a clearer understanding of the overall system architecture and signal flow.

7.After that uplod the arduino code given below after adjusting the parameters required for the timers.


Block Diagram
-------------
.. figure:: ../../../_static/shibu_figure/abstr_block_dgm.png
   :alt: block diagram
   :width: 400px
   :align: center

Arduino code For ABSTR
----------------------

.. code-block:: cpp
   :linenos:

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