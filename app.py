
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

def break_even_tab():
    st.header("Analisis Titik Impas (Break-Even Analysis)")

    # Input dari user
    fixed_cost = st.number_input("Biaya Tetap (Fixed Cost)", min_value=0.0, value=10000.0, step=100.0)
    variable_cost = st.number_input("Biaya Variabel per Unit", min_value=0.0, value=20.0, step=1.0)
    selling_price = st.number_input("Harga Jual per Unit", min_value=0.0, value=50.0, step=1.0)

    if selling_price <= variable_cost:
        st.error("Harga jual harus lebih besar dari biaya variabel agar bisa untung.")
        return

    # Hitung break-even point
    break_even_point = fixed_cost / (selling_price - variable_cost)
    st.success(f"Titik Impas (Break-Even Point): {break_even_point:.2f} unit")

    # Visualisasi
    units = np.arange(0, break_even_point * 2, 1)
    total_cost = fixed_cost + variable_cost * units
    total_revenue = selling_price * units

    fig, ax = plt.subplots()
    ax.plot(units, total_cost, label="Total Biaya", color='red')
    ax.plot(units, total_revenue, label="Total Pendapatan", color='green')
    ax.axvline(x=break_even_point, color='blue', linestyle='--', label="Titik Impas")

    ax.set_xlabel("Jumlah Unit")
    ax.set_ylabel("Rupiah")
    ax.set_title("Grafik Break-Even Point")
    ax.legend()
    st.pyplot(fig)
 
