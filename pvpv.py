import tkinter as tk
from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plt

def simulate():
    G = float(irradiance_entry.get())      # W/m²
    T = float(temp_entry.get()) + 273.15   # Kelvin

    # PV parameters (example panel)
    Isc_ref = 8.21
    Voc_ref = 37
    G_ref = 1000
    T_ref = 298
    Kv = -0.123  # Voc temp coefficient
    Ki = 0.03    # Isc temp coefficient

    Isc = Isc_ref * (G/G_ref) + Ki*(T-T_ref)
    Voc = Voc_ref + Kv*(T-T_ref)

    V = np.linspace(0, Voc, 200)
    # Simple exponential PV model
    I = Isc * (1 - np.exp((V - Voc)/Voc))
    P = V * I

    Vmp = V[np.argmax(P)]
    Imp = I[np.argmax(P)]
    Pmax = np.max(P)

    result_label.config(text=f"MPPT → Vmp={Vmp:.2f} V, Imp={Imp:.2f} A, Pmax={Pmax:.2f} W")

    plt.figure()
    plt.plot(V, I)
    plt.title("I-V Curve")
    plt.xlabel("Voltage (V)")
    plt.ylabel("Current (A)")
    plt.show()

    plt.figure()
    plt.plot(V, P)
    plt.title("P-V Curve")
    plt.xlabel("Voltage (V)")
    plt.ylabel("Power (W)")
    plt.show()

# ================= GUI =================
root = tk.Tk()
root.title("PV I-V & P-V Simulator with MPPT")

tk.Label(root, text="Irradiance (W/m²):").grid(row=0, column=0)
irradiance_entry = tk.Entry(root)
irradiance_entry.grid(row=0, column=1)

tk.Label(root, text="Temperature (°C):").grid(row=1, column=0)
temp_entry = tk.Entry(root)
temp_entry.grid(row=1, column=1)

simulate_btn = tk.Button(root, text="Simulate", command=simulate)
simulate_btn.grid(row=2, column=0, columnspan=2, pady=10)

result_label = tk.Label(root, text="MPPT → Results will appear here")
result_label.grid(row=3, column=0, columnspan=2)

root.mainloop()
