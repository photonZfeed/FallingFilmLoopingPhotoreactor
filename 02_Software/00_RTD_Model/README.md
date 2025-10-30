# Falling Film Loop Photoreactor RTD

## Summary

This repository contains the residence time distribution (RTD) analysis of a Falling Film Loop Photoreactor.

## Contents

- `00_Processed_Data/`: Processed and evaluated `.csv` files.
- `01_Figures/`: Plots of the RTD analysis.
- `main.ipynb`: Jupyter Notebook with RTD analysis code.

## Installation

Install the required Python packages using:

```bash
pip install --only-binary :all: -r requirements.txt
```

## Requirements

- Python < 3.12
- All required Python packages are listed in `requirements.txt`


## Models and Equations

To determine the Bodenstein number from the RTD experiments, an axial dispersion model with **closed–closed boundary conditions**[^1] is fitted to the experimental data. The input signal is modeled as an ideal Dirac pulse, since injection time ≪ residence time.

The implementation is based on the `rtdpy` package[^2]. Detailed equations and boundary conditions can be found in the [rtdpy documentation](https://merck.github.io/rtdpy/AxialDispersion_cc.html).

The mean residence time $\bar{\tau}$ is calculated as the first moment of the experimental residence time density function $E_\mathrm{exp}(t)$:

$$
\bar{\tau} = \int_0^\infty t \cdot E_\mathrm{exp}(t) \, dt
$$

## Results

The figures and table below summarize the results of the RTD analysis as a function of external flow rate.

### Mean Residence Time and Bodenstein number

<table>
     <thead>
    <tr>
      <th>Flow Rate (mL min⁻¹)</th>
      <th>Mean Residence Time (s)</th>
      <th>Hydrodynamic Mean Residence Time (s)</th>
      <th>Bodenstein Number (1)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>3.3</td>
      <td>272.02</td>
      <td>363.64</td>
      <td>0.56</td>
    </tr>
    <tr>
      <td>5.0</td>
      <td>174.05</td>
      <td>240.00</td>
      <td>1.13</td>
    </tr>
    <tr>
      <td>10.0</td>
      <td>119.29</td>
      <td>120.00</td>
      <td>0.53</td>
    </tr>
    <tr>
      <td>20.0</td>
      <td>80.91</td>
      <td>60.00</td>
      <td>0.58</td>
    </tr>
    <tr>
      <td>40.0</td>
      <td>73.21</td>
      <td>30.00</td>
      <td>0.44</td>
    </tr>
  </tbody>
</table>

<img src="01_Figures/tau_Bo_plot.png" alt="Figure 1" width="400">
<br>
<br>

### Comparison of Experimental Data and Simulation

<img src="01_Figures/comparison_plot.png" alt="Figure 1" width="800">
<br>
<br>

### Simulated RTD Functions at Increasing Flow Rates


<img src="01_Figures/all_simulated_RTDs_plot.png" alt="Figure 2" width="800">


## References

[^1]: O. Levenspiel, Chemical reaction engineering. Hauptbd., 3. ed, Wiley, New York Weinheim, 1999.
[^2]: Flamm, M. rtdpy: A python package for residence time distributions. Journal of Open Source Software. , 4(40) , 1621. (2019).





