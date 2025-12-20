Time controller
---------------

The time controller device governs the entire operation by triggering each pump according to predefined timings and flow durations. At the start of the cycle, the controller activates Pump 1 for a set time to introduce the required volume of reaction mixture into the reactor. After the reaction time elapses, the controller switches to Pump 3, which runs for a specific duration to remove the processed product from the reactor. Once product removal is completed, the controller enables Pump 2 to supply a calculated amount of solvent for washing. Following solvent introduction, Pump 3 is again activated by the controller to expel the solvent and any residual materials. This time-based switching sequence forms one complete operating cycle, and the controller continues to loop through these pump operations automatically until the system is stopped.

.. figure:: ../../../_static/shibu_figure/time_controller.jpeg
   :alt: time controller block diagram
   :width: 400px
   :align: center

Circuit Diagram
---------------
The circuit diagram of the time controller module illustrates the electronic components and their interconnections that facilitate the timing and control functions. It includes microcontrollers, relays, resistors, capacitors, and other essential elements that work together to manage the pump operations based on the programmed timing sequences.

.. figure:: ../../../_static/shibu_figure/abstr_ckt.png
   :alt: time controller circuit diagram
   :width: 400px
   :align: center