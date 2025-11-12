================================================================================
Continuous Stirred Tank Reactor (CSTR)
================================================================================

Software-assisted Geometrically Scalable CSTR
================================================================================

System Overview
================================================================================

The continuous operation control unit is a software-driven system engineered to maintain steady, predetermined inlet and outlet flow rates through precision-controlled pump operations. The flow rates are established based on experimentally determined residence times and are programmed prior to initiating the continuous reaction sequence.

The system comprises three primary pumps:

- **Inlet Pump (Pump 1)**: Delivers reaction mixture from the reagent reservoir
- **Outlet Pump (Pump 2)**: Withdraws product from the reaction chamber
- **Looping Pump (Pump 3)**: Auxiliary pump for internal circulation

Operational Sequence
================================================================================

1. System Start-up
================================================================================

Upon activation of the control circuit, the inlet pump (Pump 1) is engaged automatically. It delivers the reaction mixture from the reagent reservoir into the reaction chamber at a constant flow rate **x mL/min**, as specified by the operator.

2. Internal Looping
================================================================================

At the same time, the looping pump (Pump 3) is activated to recirculate a portion of the reactor effluent back to the top of the reaction chamber. Its flow rate is defined by a space-velocity setting entered by the operator.

This recirculation establishes and sustains a continuous falling film along the chamber walls, ensuring:

- Consistent film thickness
- Proper internal stirring

3. Outlet Pump Startup
================================================================================

As the inlet stream accumulates, the mass of the reaction chamber increases continuously. The integrated weighing scale displays real-time mass.

When the scale reading reaches the lower threshold **W1 g** (equivalently, **Y1 mL**), the outlet pump (Pump 2) is activated. It withdraws product at the same flow rate **x mL/min** as the inlet pump, thus maintaining a dynamic equilibrium.

4. Mass Regulation Logic
================================================================================

The control software enforces strict bounds on the chamber's contents: the mass must remain between **W1 g** (Y1 mL) and **W2 g** (Y2 mL).

Pumps 1 and 2 are modulated—starting or stopping as needed—to hold the chamber mass within this range.

5. Adaptive Pump Control
================================================================================

The system employs the following adaptive control logic:

a) **Low Mass Condition**: If the chamber mass falls below **W1 g** (Y1 mL), Pump 2 (outlet) is halted, allowing the mass to rise.
b) **High Mass Condition**: Conversely, if the mass exceeds **W2 g** (Y2 mL), Pump 1 (inlet) is deactivated until the mass returns to the acceptable range.

6. Parameter Customization
================================================================================

The parameters are determined experimentally during system calibration:

- **x**: Inlet and outlet flow rate (mL/min)
- **Y1**: Lower threshold volume (mL)
- **Y2**: Upper threshold volume (mL)
- **W1**: Lower threshold mass (g)
- **W2**: Upper threshold mass (g)

These values may be adjusted in the control software to accommodate different reaction conditions or objectives.

System Stability and Continuous Operation
================================================================================

This configuration ensures continuous, stable operation by dynamically balancing inlet and outlet flows, thereby sustaining the reaction chamber at the desired volume and mass throughout the process.

Key features:

- **Dynamic Flow Equilibrium**: Inlet and outlet flows are maintained at equal rates during steady state
- **Real-time Monitoring**: Integrated weighing scale provides continuous mass feedback
- **Automated Control**: Software-driven pump modulation eliminates manual intervention
- **Geometric Scalability**: System parameters can be adjusted to scale the reactor for different production volumes
- **Uniform Reaction Conditions**: Continuous falling film and looping pump ensure homogeneous mixing and consistent residence time distribution