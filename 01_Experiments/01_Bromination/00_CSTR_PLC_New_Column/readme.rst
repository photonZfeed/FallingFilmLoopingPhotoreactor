HPLC Data After Column Replacement
==================================

This directory contains HPLC chromatogram data collected after replacing the HPLC Column. The data are organized based on experimental
conditions, external flow rates, and calibration measurements.

Each subfolder represents a specific experimental configuration, and the PDF
files within the folders correspond to time-resolved HPLC readings.

Folder Overview
---------------

EXP-3: 10 mL·min⁻¹ External Flow Rate
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This folder contains HPLC chromatograms recorded when the experiment was
performed at an external flow rate of **10 mL·min⁻¹**.

Each PDF file represents the reaction procress after a specific
reaction time.

**File naming convention:**

- ``1.pdf``  → HPLC Data corresponds to the reaction progress after **1 minute** of reaction  
- ``2.pdf``  → HPLC Data corresponds to the reaction progress after **2 minutes** of reaction  
- ``3.pdf``  → HPLC Data corresponds to the reaction progress after **3 minutes** of reaction  
- *and so on*

---

EXP-4: 20 mL·min⁻¹ External Flow Rate
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This folder contains HPLC data obtained at an external flow rate of
**20 mL·min⁻¹**.

- The experimental procedure and sampling method are identical to EXP-3.
- The file-naming strategy follows the same reaction-time-based convention.

---

EXP-5: 40 mL·min⁻¹ External Flow Rate
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This folder contains HPLC chromatograms collected at a higher external flow rate
of **40 mL·min⁻¹**.

- The experimental procedure and sampling method are identical to EXP-3.
- The file-naming strategy follows the same reaction-time-based convention.


---

Scale-Up
~~~~~~~~
This folder contains HPLC data **of the large scale experiment**.

- Although the reactor scale differs from laboratory experiments, the sampling
  method and file-naming strategy remain unchanged.
- File names represent the reaction progress time in minutes.

---

Std. Graph (Standard Calibration Data)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This folder contains HPLC standard chromatograms used for calibration curve and equation.

- Each PDF corresponds to a standard solution with a known concentration (µg·mL⁻¹) and their corresponding peek area.
  
- File names corresponds to the increasing order of the concentration of pure benzyl bromide starting from 1.25 µg·mL⁻¹ upto 320 µg·mL⁻¹ following a gp series with general mean of 2


**Examples:**

- ``BB1.pdf``, ``BB2.pdf``, ``BB3.pdf`` → Standard calibration runs  
- ``BLANK.pdf`` → Blank solvent run (zero concentration reference)

These standard graphs are used to generate calibration curves for converting
HPLC peak areas into concentration values.


Notes
-----
- All data were recorded after replacing the HPLC column.
- Experimental conditions other than flow rate were kept consistent unless
  stated otherwise.
