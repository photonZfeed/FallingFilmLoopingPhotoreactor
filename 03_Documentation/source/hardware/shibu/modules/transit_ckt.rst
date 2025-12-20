TRANSIT Circuit 
================

OVERVIEW
--------
The transit circuit functions as a switching interface that allows the system to choose between ABSTR and CSTR operation. It uses a relay and two selector switches to route control signals to the desired reactor setup. When ABSTR is selected, the relay directs the controller output to the batch operation modules; when switched to CSTR, it redirects signals to the continuous reactor hardware. This arrangement ensures safe, isolated, and convenient switching between modes without changing wiring.



.. figure:: ../../../_static/shibu_figure/transit_ckt.jpeg
   :alt: circuit diagram of CSTR
   :width: 500px
   :align: center

   Figure: CSTR circuit

Components Used:
----------------

:doc:`Relay <../components/relay>`

Switch

3mm Leds

