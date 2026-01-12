# Falling Film Looping Photoreactor and Residence Time Distribution Measurement Cells

A modular and characterized open source Falling Film Looping Photoreactor (FFLPR) concept for Automated Batch Stirred Tank Reactor (ABSTR) and Contineous Stirred Tank Reactor (CSTR) operation. And a Residence Time Distribution (RTD) cell for puls tracer measurements.

## Documentation

3D CAD files for the RTD cell manufacturing are documented in the [CAD section](./00_CAD/).

Experimental raw data on the RTD and bromination experiments are provided in the [Experiments section](./01_Experiments/).

A detailed documentation of the RTD cells and photoreactor including its control software as well as the RTD model are available under https://photonzfeed.github.io/FallingFilmLoopingPhotoreactor/.

## Folder Structure

```
📦Falling_Film_Loop_Photoreactor_RTD
┣ 📂 00_CAD
┃  ┣ 📜 RTD_cell_bottom_1mm_tubing.ipt
┃  ┣ 📜 RTD_cell_bottom_1mm_tubing.stl
┃  ┣ 📜 RTD_cell_bottom_2mm_tubing.ipt
┃  ┣ 📜 RTD_cell_bottom_2mm_tubing.stl
┃  ┣ 📜 RTD_cell_bottom_3mm_tubing.ipt
┃  ┣ 📜 RTD_cell_bottom_3mm_tubing.stl
┃  ┣ 📜 RTD_cell_top_1mm_tubing.ipt
┃  ┣ 📜 RTD_cell_top_1mm_tubing.stl
┃  ┣ 📜 RTD_cell_top_2mm_tubing.ipt
┃  ┣ 📜 RTD_cell_top_2mm_tubing.stl
┃  ┣ 📜 RTD_cell_top_3mm_tubing.ipt
┃  ┗ 📜 RTD_cell_top_3mm_tubing.stl
┣ 📂 01_Experiments
┃  ┣ 📂 00_RTD
┃  ┃  ┣ 📂 00_External_Flow_Rate_Variation
┃  ┃  ┃  ┣ 📜 03.3 mL per min.csv
┃  ┃  ┃  ┣ 📜 05 mL per min.csv
┃  ┃  ┃  ┣ 📜 10 mL per min.csv
┃  ┃  ┃  ┣ 📜 20 mL per min.csv
┃  ┃  ┃  ┗ 📜 40 mL per min.csv
┃  ┃  ┗ 📂 01_Space_Velocity_Variation
┃  ┃     ┣ 📜 0spv.csv
┃  ┃     ┣ 📜 15spv.csv
┃  ┃     ┣ 📜 30spv.csv
┃  ┃     ┗ 📜 5spv.csv
┃  ┗ 📂 01_Bromination
┃     ┣ 📂 00_CSTR_PLC_New_Column
┃     ┃  ┣ 📂 EXP-3 10 mLmin-1 external flow rate
┃     ┃  ┃  ┣ 📜 1.pdf
┃     ┃  ┃  ┣ 📜 10.pdf
┃     ┃  ┃  ┣ 📜 11.pdf
┃     ┃  ┃  ┣ 📜 12.pdf
┃     ┃  ┃  ┣ 📜 13.pdf
┃     ┃  ┃  ┣ 📜 14.pdf
┃     ┃  ┃  ┣ 📜 15.pdf
┃     ┃  ┃  ┣ 📜 2.pdf
┃     ┃  ┃  ┣ 📜 3.pdf
┃     ┃  ┃  ┣ 📜 4.pdf
┃     ┃  ┃  ┣ 📜 5.pdf
┃     ┃  ┃  ┣ 📜 6.pdf
┃     ┃  ┃  ┣ 📜 7.pdf
┃     ┃  ┃  ┣ 📜 8.pdf
┃     ┃  ┃  ┗ 📜 9.pdf
┃     ┃  ┣ 📂 EXP-4 20 mLmin-1 external flow rate
┃     ┃  ┃  ┣ 📜 1.pdf
┃     ┃  ┃  ┣ 📜 10.pdf
┃     ┃  ┃  ┣ 📜 11.pdf
┃     ┃  ┃  ┣ 📜 12.pdf
┃     ┃  ┃  ┣ 📜 13.pdf
┃     ┃  ┃  ┣ 📜 14.pdf
┃     ┃  ┃  ┣ 📜 15.pdf
┃     ┃  ┃  ┣ 📜 2.pdf
┃     ┃  ┃  ┣ 📜 3.pdf
┃     ┃  ┃  ┣ 📜 4.pdf
┃     ┃  ┃  ┣ 📜 5.pdf
┃     ┃  ┃  ┣ 📜 6.pdf
┃     ┃  ┃  ┣ 📜 7.pdf
┃     ┃  ┃  ┣ 📜 8.pdf
┃     ┃  ┃  ┗ 📜 9.pdf
┃     ┃  ┣ 📂 EXP-5 40 mLmin-1 external flow rate
┃     ┃  ┃  ┣ 📜 1.pdf
┃     ┃  ┃  ┣ 📜 10.pdf
┃     ┃  ┃  ┣ 📜 11`.pdf
┃     ┃  ┃  ┣ 📜 12.pdf
┃     ┃  ┃  ┣ 📜 13.pdf
┃     ┃  ┃  ┣ 📜 14.pdf
┃     ┃  ┃  ┣ 📜 15.pdf
┃     ┃  ┃  ┣ 📜 2.pdf
┃     ┃  ┃  ┣ 📜 3.pdf
┃     ┃  ┃  ┣ 📜 4.pdf
┃     ┃  ┃  ┣ 📜 5.pdf
┃     ┃  ┃  ┣ 📜 6.pdf
┃     ┃  ┃  ┣ 📜 7.pdf
┃     ┃  ┃  ┣ 📜 8.pdf
┃     ┃  ┃  ┗ 📜 9.pdf
┃     ┃  ┣ 📂 Scale-Up
┃     ┃  ┃  ┣ 📜 1.pdf
┃     ┃  ┃  ┣ 📜 10.pdf
┃     ┃  ┃  ┣ 📜 11.pdf
┃     ┃  ┃  ┣ 📜 12.pdf
┃     ┃  ┃  ┣ 📜 13.pdf
┃     ┃  ┃  ┣ 📜 14.pdf
┃     ┃  ┃  ┣ 📜 15.pdf
┃     ┃  ┃  ┣ 📜 2.pdf
┃     ┃  ┃  ┣ 📜 3.pdf
┃     ┃  ┃  ┣ 📜 4.pdf
┃     ┃  ┃  ┣ 📜 5.pdf
┃     ┃  ┃  ┣ 📜 6.pdf
┃     ┃  ┃  ┣ 📜 7.pdf
┃     ┃  ┃  ┣ 📜 8.pdf
┃     ┃  ┃  ┣ 📜 9.pdf
┃     ┃  ┃  ┗ 📜 BLANK.pdf
┃     ┃  ┣ 📂 Std. Graph
┃     ┃  ┃  ┣ 📜 BB1.1.pdf
┃     ┃  ┃  ┣ 📜 BB1.pdf
┃     ┃  ┃  ┣ 📜 BB2.pdf
┃     ┃  ┃  ┣ 📜 BB3.pdf
┃     ┃  ┃  ┣ 📜 BB4.pdf
┃     ┃  ┃  ┣ 📜 BB5.pdf
┃     ┃  ┃  ┣ 📜 BB6.pdf
┃     ┃  ┃  ┣ 📜 BB7.pdf
┃     ┃  ┃  ┣ 📜 BB8.pdf
┃     ┃  ┃  ┣ 📜 BB9.pdf
┃     ┃  ┃  ┗ 📜 BLANK.pdf
┃     ┃  ┗ 📜 readme.md
┃     ┣ 📂 01_CSTR_UV_VIS
┃     ┃  ┣ 📂 3 mLmin-1
┃     ┃  ┃  ┣ 📜 500 mM 3 mL-min.opju
┃     ┃  ┃  ┣ 📜 M1.txt
┃     ┃  ┃  ┣ 📜 R1.txt
┃     ┃  ┃  ┣ 📜 t=18.txt
┃     ┃  ┃  ┣ 📜 t=2.txt
┃     ┃  ┃  ┣ 📜 t=28.txt
┃     ┃  ┃  ┣ 📜 t=38.txt
┃     ┃  ┃  ┣ 📜 t=4.txt
┃     ┃  ┃  ┣ 📜 t=48.txt
┃     ┃  ┃  ┣ 📜 t=58.txt
┃     ┃  ┃  ┣ 📜 t=6.txt
┃     ┃  ┃  ┗ 📜 t=8.txt
┃     ┃  ┗ 📂 5 mLmin-1
┃     ┃     ┣ 📜 500mM 5mL-min.opju
┃     ┃     ┣ 📜 M2.txt
┃     ┃     ┣ 📜 R2.txt
┃     ┃     ┣ 📜 t=0.txt
┃     ┃     ┣ 📜 t=14.txt
┃     ┃     ┣ 📜 t=2.txt
┃     ┃     ┣ 📜 t=24.txt
┃     ┃     ┣ 📜 t=34.txt
┃     ┃     ┣ 📜 t=4.txt
┃     ┃     ┣ 📜 t=44.txt
┃     ┃     ┣ 📜 t=54.txt
┃     ┃     ┗ 📜 t=64.txt
┃     ┣ 📂 02_ABSTR_HPLC_Old_Column
┃     ┃  ┣ 📂 1 h reaction
┃     ┃  ┃  ┣ 📂 500 mM
┃     ┃  ┃  ┃  ┣ 📜 1.pdf
┃     ┃  ┃  ┃  ┣ 📜 10.pdf
┃     ┃  ┃  ┃  ┣ 📜 2.pdf
┃     ┃  ┃  ┃  ┣ 📜 3.pdf
┃     ┃  ┃  ┃  ┣ 📜 4.pdf
┃     ┃  ┃  ┃  ┣ 📜 5.pdf
┃     ┃  ┃  ┃  ┣ 📜 6.pdf
┃     ┃  ┃  ┃  ┣ 📜 7.pdf
┃     ┃  ┃  ┃  ┣ 📜 8.pdf
┃     ┃  ┃  ┃  ┗ 📜 9.pdf
┃     ┃  ┃  ┗ 📂 815 mM
┃     ┃  ┃     ┣ 📜 1.pdf
┃     ┃  ┃     ┣ 📜 2.pdf
┃     ┃  ┃     ┣ 📜 3.pdf
┃     ┃  ┃     ┣ 📜 4.pdf
┃     ┃  ┃     ┣ 📜 5.pdf
┃     ┃  ┃     ┣ 📜 6.pdf
┃     ┃  ┃     ┣ 📜 7.pdf
┃     ┃  ┃     ┗ 📜 8.pdf
┃     ┃  ┣ 📂 24 h reactions
┃     ┃  ┃  ┣ 📂 500 mM scale
┃     ┃  ┃  ┃  ┣ 📜 1.pdf
┃     ┃  ┃  ┃  ┣ 📜 2.pdf
┃     ┃  ┃  ┃  ┣ 📜 3.pdf
┃     ┃  ┃  ┃  ┣ 📜 4.pdf
┃     ┃  ┃  ┃  ┣ 📜 5.pdf
┃     ┃  ┃  ┃  ┣ 📜 6.pdf
┃     ┃  ┃  ┃  ┗ 📜 7.pdf
┃     ┃  ┃  ┗ 📂 815 mM scale
┃     ┃  ┃     ┣ 📜 1.pdf
┃     ┃  ┃     ┣ 📜 2.pdf
┃     ┃  ┃     ┣ 📜 3.pdf
┃     ┃  ┃     ┣ 📜 4.pdf
┃     ┃  ┃     ┣ 📜 5.pdf
┃     ┃  ┃     ┣ 📜 6.pdf
┃     ┃  ┃     ┗ 📜 7.pdf
┃     ┃  ┣ 📂 different internal flow rate
┃     ┃  ┃  ┣ 📂 500 mM with out looping operation
┃     ┃  ┃  ┃  ┣ 📜 1.pdf
┃     ┃  ┃  ┃  ┣ 📜 2.pdf
┃     ┃  ┃  ┃  ┣ 📜 3.pdf
┃     ┃  ┃  ┃  ┣ 📜 4.pdf
┃     ┃  ┃  ┃  ┣ 📜 5.pdf
┃     ┃  ┃  ┃  ┗ 📜 6.pdf
┃     ┃  ┃  ┣ 📂 500 mM-space velocity 150 min-1
┃     ┃  ┃  ┃  ┣ 📜 1.pdf
┃     ┃  ┃  ┃  ┣ 📜 2.pdf
┃     ┃  ┃  ┃  ┣ 📜 3.pdf
┃     ┃  ┃  ┃  ┣ 📜 4.pdf
┃     ┃  ┃  ┃  ┣ 📜 5.pdf
┃     ┃  ┃  ┃  ┗ 📜 6.pdf
┃     ┃  ┃  ┣ 📂 500 mM-space velocity 300 min-1
┃     ┃  ┃  ┃  ┣ 📜 1.pdf
┃     ┃  ┃  ┃  ┣ 📜 2.pdf
┃     ┃  ┃  ┃  ┣ 📜 3.pdf
┃     ┃  ┃  ┃  ┣ 📜 4.pdf
┃     ┃  ┃  ┃  ┣ 📜 5.pdf
┃     ┃  ┃  ┃  ┗ 📜 6.pdf
┃     ┃  ┃  ┗ 📂 800 mM with out looping operation
┃     ┃  ┃     ┣ 📜 1.pdf
┃     ┃  ┃     ┣ 📜 2.pdf
┃     ┃  ┃     ┣ 📜 3.pdf
┃     ┃  ┃     ┣ 📜 4.pdf
┃     ┃  ┃     ┣ 📜 5.pdf
┃     ┃  ┃     ┗ 📜 6.pdf
┃     ┃  ┣ 📂 Optimization with respect to different concentration
┃     ┃  ┃  ┣ 📂 500 mM
┃     ┃  ┃  ┃  ┣ 📜 1.1.pdf
┃     ┃  ┃  ┃  ┣ 📜 1.2.pdf
┃     ┃  ┃  ┃  ┣ 📜 1.3.pdf
┃     ┃  ┃  ┃  ┣ 📜 1.4.pdf
┃     ┃  ┃  ┃  ┣ 📜 1.5.pdf
┃     ┃  ┃  ┃  ┗ 📜 1.6.pdf
┃     ┃  ┃  ┗ 📂 815 mM
┃     ┃  ┃     ┣ 📜 4.1.pdf
┃     ┃  ┃     ┣ 📜 4.2.pdf
┃     ┃  ┃     ┣ 📜 4.3.pdf
┃     ┃  ┃     ┣ 📜 4.4.pdf
┃     ┃  ┃     ┣ 📜 4.5.pdf
┃     ┃  ┃     ┗ 📜 4.7.pdf
┃     ┃  ┣ 📂 Scale-Up
┃     ┃  ┃  ┣ 📜 1.pdf
┃     ┃  ┃  ┣ 📜 2.pdf
┃     ┃  ┃  ┣ 📜 3.pdf
┃     ┃  ┃  ┣ 📜 4.pdf
┃     ┃  ┃  ┣ 📜 5.pdf
┃     ┃  ┃  ┣ 📜 6.pdf
┃     ┃  ┃  ┣ 📜 7.pdf
┃     ┃  ┃  ┣ 📜 8.pdf
┃     ┃  ┃  ┣ 📜 9.pdf
┃     ┃  ┃  ┗ 📜 BLANK.pdf
┃     ┃  ┗ 📂 Std. Graph
┃     ┃     ┣ 📜 1.25.pdf
┃     ┃     ┣ 📜 10.pdf
┃     ┃     ┣ 📜 160.pdf
┃     ┃     ┣ 📜 2.5.pdf
┃     ┃     ┣ 📜 20.pdf
┃     ┃     ┣ 📜 320.pdf
┃     ┃     ┣ 📜 40.pdf
┃     ┃     ┣ 📜 5.pdf
┃     ┃     ┣ 📜 80.pdf
┃     ┃     ┗ 📜 blank.pdf
┃     ┗ 📂 03_ABSTR_UV_Vis
┃        ┣ 📂 500 mM
┃        ┃  ┣ 📜 1.0.txt
┃        ┃  ┣ 📜 1.1.txt
┃        ┃  ┣ 📜 1.2.txt
┃        ┃  ┣ 📜 1.3.txt
┃        ┃  ┣ 📜 1.4.txt
┃        ┃  ┣ 📜 1.5.txt
┃        ┃  ┣ 📜 1.6.txt
┃        ┃  ┣ 📜 benzyl bromide.txt
┃        ┃  ┣ 📜 reaction kinetics 500mM.opju
┃        ┃  ┗ 📜 toluene.txt
┃        ┣ 📂 515 mM scale
┃        ┃  ┣ 📜 1.txt
┃        ┃  ┣ 📜 2.txt
┃        ┃  ┣ 📜 3.txt
┃        ┃  ┣ 📜 4.txt
┃        ┃  ┣ 📜 5.txt
┃        ┃  ┣ 📜 6.txt
┃        ┃  ┣ 📜 reaction kinetics 815 mM final.opju
┃        ┃  ┗ 📜 reaction mixture.txt
┃        ┗ 📂 BB and Toluene
┃           ┣ 📜 benzyl bromide.txt
┃           ┗ 📜 toluene.txt
┣ 📂 02_Software
┃  ┣ 📂 00_RTD_Model
┃  ┃  ┣ 📂 00_Processed_Data
┃  ┃  ┃  ┣ 📜 10 mL per min processed.csv
┃  ┃  ┃  ┣ 📜 20 mL per min processed.csv
┃  ┃  ┃  ┣ 📜 3.3 mL per min processed.csv
┃  ┃  ┃  ┣ 📜 40 mL per min processed.csv
┃  ┃  ┃  ┣ 📜 5 mL per min processed.csv
┃  ┃  ┃  ┗ 📜 summary_table.csv
┃  ┃  ┣ 📂 01_Figures
┃  ┃  ┃  ┣ 📜 all_simulated_RTDs_plot.png
┃  ┃  ┃  ┣ 📜 comparison_plot.png
┃  ┃  ┃  ┗ 📜 tau_Bo_plot.png
┃  ┃  ┣ 📜 main.ipynb
┃  ┃  ┗ 📜 README.md
┃  ┣ 📂 01_Arduino_Control
┃  ┃  ┣ 📂 lib
┃  ┃  ┃  ┣ 📜 HX711_ADC-master.zip
┃  ┃  ┃  ┗ 📜 LiquidCrystal_I2C-master.zip
┃  ┃  ┣ 📜 bstr.ino
┃  ┃  ┣ 📜 cstr.ino
┃  ┃  ┗ 📜 readme.md
┃  ┗ 📜 02_RTD_Cell_Control.py
┣ 📂 03_Documentation
┃  ┗ 📜 RTD_cell_Dani_merge.rst
┣ 📜 .gitignore
┣ 📜 README.md
┗ 📜 requirements.txt
```

## Publications
The FFLPR concept was verfied using the light-driven and N-Bromsuccinimid mediated allyic bromination of toluene as model reaction.

A detailed documentation of the FFLPR modules and optical charazterization data can be found in the following publication:
* [Making photochemistry scalable – an operationally simple falling film looping photoreactor](https://pubs.rsc.org/en/content/articlelanding/2023/re/d3re00107e)

A comparative evaluation of scale up strategies of the FFLPR for ABSTR and CSTR operation is described in the following publication:
* [A Comparative Experimental Evaluation of an Automated Batchwise and Continuous Operation Mode for Scaling Up a Falling Film Looping Photoreactor](https://fill_in_the_blank)
