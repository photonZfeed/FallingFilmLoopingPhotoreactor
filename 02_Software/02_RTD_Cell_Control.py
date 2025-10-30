import sys
import pandas as pd
import csv
import time
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QHBoxLayout, QFileDialog
from PyQt5.QtCore import QTimer
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_industrial_dual_analog_in_v2 import BrickletIndustrialDualAnalogInV2
from tinkerforge.bricklet_industrial_analog_out_v2 import BrickletIndustrialAnalogOutV2
import datetime
import numpy as np


# Konfigurationsparameter für das Tinkerforge-Setup
HOST = "localhost"
PORT = 4223
UID_DUAL_ANALOG_IN = "Mmj"  # Ändere XYZ zu deiner UID für den Industrial Dual Analog In 2.1
UID_ANALOG_OUT = "Ygt"      # Ändere ABC zu deiner UID für den Analog Out 2.0

class DynamicPlot(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Dynamischer Plot mit PyQt5 und Tinkerforge')
        self.setGeometry(100, 100, 800, 600)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)

        self.figure, self.ax = plt.subplots()
        self.canvas = FigureCanvas(self.figure)
        self.layout.addWidget(self.canvas)

        self.button_layout = QHBoxLayout()

        self.start_button = QPushButton('Start Measurement')
        self.start_button.clicked.connect(self.start_acquisition)
        self.button_layout.addWidget(self.start_button)

        self.start_button = QPushButton('Start LED')
        self.start_button.clicked.connect(self.start_LED)
        self.button_layout.addWidget(self.start_button)
        
        self.stop_button = QPushButton('Stop LED')
        self.stop_button.clicked.connect(self.stop_LED)
        self.button_layout.addWidget(self.stop_button)

        self.save_button = QPushButton('Save data')
        self.save_button.clicked.connect(self.save_values)
        self.button_layout.addWidget(self.save_button)

        self.layout.addLayout(self.button_layout)

        self.voltage_at_c_max = 2699,3300 # values in mV for 1mm diameter (for a conc of 0.01 g/L)       # changed on 06/06/2024
        self.dConc_dVoltage_constant = 2240/2889,2900/3584 #voltage change for a concentration of 2 g/L determined with Photoresistor for 1mm


        self.x_data = []
        self.timestamps = []
        self.y_data_channel_0 = []
        self.y_data_channel_1 = []
        self.data_conc_1 =[]
        self.data_conc_2 =[]
        self.data_signal_0 = []
        self.data_signal_1 = []

        self.initial_voltage_0 = None
        self.initial_voltage_1 = None

        self.timer = QTimer()
        self.timer.setInterval(200)  # 200 ms = 0.2 s
        self.timer.timeout.connect(self.update_plot)

        self.start_time = None

        # Tinkerforge Initialisierung
        self.ipcon = IPConnection()

        # Industrial Dual Analog In V2 Initialisierung
        self.ida = BrickletIndustrialDualAnalogInV2(UID_DUAL_ANALOG_IN, self.ipcon)

        # Analog Out V2 Initialisierung
        self.analog_out_v2 = BrickletIndustrialAnalogOutV2(UID_ANALOG_OUT, self.ipcon)

        self.ipcon.connect(HOST, PORT)
    


    def start_LED(self):
        self.analog_out_v2.set_enabled(True)  # LED starten
        print('LED on. Please wait 60 seconds before you start the measurement.')
        time.sleep(2)
        # print('You can start the measurement now.')


    def start_acquisition(self):
        self.start_time = time.time()
        # self.set_reference()
        voltage_0, voltage_1 = self.get_voltage()
        self.initial_voltage_0 = voltage_0
        self.initial_voltage_1 = voltage_1
        self.timer.start()
        print('The Measurement started.')
        print('Reference signal at the start:' + str(self.initial_voltage_0) + 'mV and ' + str(self.initial_voltage_1)+ 'mV')

    def stop_LED(self):
            self.analog_out_v2.set_enabled(False)  # LED starten
            print('LED off.')
        

    def get_voltage(self):
        voltage_0 = self.ida.get_voltage(0)   # Kanal 0 in mV
        voltage_1 = self.ida.get_voltage(1)   # Kanal 1 in mV
        return voltage_0, voltage_1
    
    def get_concentration(self):
        voltage0 = self.ida.get_voltage(0)  
        voltage1 = self.ida.get_voltage(1)      
        # conc1 = (- self.dConc_dVoltage_constant[0] * voltage0 + self.dConc_dVoltage_constant[0] *self.initial_voltage_0)/1000 #Concentration of Product VIS 1 in mol / L
        # conc2 = (- self.dConc_dVoltage_constant[1] * voltage1 + self.dConc_dVoltage_constant[1] *self.initial_voltage_1)/1000 #Concentration of Product VIS 2 in mol / L

        # conc1 = (2/319.85) * ((voltage0-self.initial_voltage_0)/(self.voltage_at_c_max[0]-self.initial_voltage_0)) 
        # conc2 = (2/319.85) * ((voltage1-self.initial_voltage_1)/(self.voltage_at_c_max[1]-self.initial_voltage_1)) 


        conc1 = (0.01/319.85) * ((voltage0-self.initial_voltage_0)/(self.voltage_at_c_max[0]-self.initial_voltage_0)) 
        conc2 = (0.01/319.85) * ((voltage1-self.initial_voltage_1)/(self.voltage_at_c_max[1]-self.initial_voltage_1)) 
        return conc1, conc2


    def get_signal(self):
        voltage_0 = self.ida.get_voltage(0)
        voltage_1 = self.ida.get_voltage(1)

        adj_vol_0 = self.initial_voltage_0 - voltage_0
        adj_vol_1 = self.initial_voltage_1 - voltage_1
        return adj_vol_0, adj_vol_1



    
    def update_plot(self):
        current_time = time.time() - self.start_time
        voltage_0, voltage_1 = self.get_voltage()
        # concentration1, concentration2 = self.get_concentration()
        signal_0, signal_1 = self.get_signal()

        self.x_data.append(current_time)
        self.timestamps.append(datetime.datetime.now())
        self.y_data_channel_0.append(voltage_0)
        self.y_data_channel_1.append(voltage_1)
        # self.data_conc_1.append(concentration1)
        # self.data_conc_2.append(concentration2)
        self.data_signal_0.append(signal_0)
        self.data_signal_1.append(signal_1)

        self.ax.clear()
        self.ax.plot(self.x_data, self.data_signal_0, label='Signal Cell 0')
        self.ax.plot(self.x_data, self.data_signal_1, label='Signal Cell 1')
        self.ax.tick_params(direction='in', left=True, right=True, bottom=True, top=True, labelsize=12)
        # self.ax.set_ylim(-0.0005, 0.003)
        self.ax.legend(fontsize=14)
        self.ax.set_xlabel('Time / s', fontsize=14)
        self.ax.set_ylabel('Adjusted Voltage / mV', fontsize=14)

        self.canvas.draw()

    def save_values(self):
        # Öffne einen Dialog, um den Speicherort und Dateinamen zu wählen
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_path, _ = QFileDialog.getSaveFileName(self, "Speichern unter", "", "CSV Files (*.csv);;All Files (*)", options=options)
        
        if file_path:
            # Organisiere die Daten in einem Dictionary
            data = {
                'Timestamp': self.timestamps,
                'Time': self.x_data,
                'Voltage Channel 0': self.y_data_channel_0,
                'Voltage Channel 1': self.y_data_channel_1,
                'Adjusted Voltage Channel 0': self.data_signal_0,
                'Adjusted Voltage Channel 1': self.data_signal_1
                # 'Concentration Channel 0': self.data_conc_1,
                # 'Concentration Channel 1': self.data_conc_2
            }
            
            # Konvertiere das Dictionary in ein pandas DataFrame
            df = pd.DataFrame(data)
            
            # Speichere das DataFrame als CSV-Datei
            df.to_csv(file_path, index=False, decimal=',')
            
            print(f"Data successfully saved in: {file_path}")           # IMPORTANT: When saving the file, put .csv in the file name to gain the right data-type!


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = DynamicPlot()
    window.show()
    sys.exit(app.exec_())
