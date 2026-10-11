
import streamlit as st

st.set_page_config(page_title="QuantumLED", page_icon="💡")

st.title("💡 QuantumLED Simulator")
st.subheader("Semiconductor Band Gap and LED Colour")

st.write("Welcome to my ECE capstone project!")

energy = st.slider(
    "Choose band-gap energy (eV)",
    1.0, 3.5, 2.0, 0.1
)

wavelength = 1240 / energy

st.metric("Band Gap", f"{energy:.2f} eV")
st.metric("Wavelength", f"{wavelength:.1f} nm")

if wavelength < 450:
    colour = "Violet"
elif wavelength < 495:
    colour = "Blue"
elif wavelength < 570:
    colour = "Green"
elif wavelength < 590:
    colour = "Yellow"
elif wavelength < 620:
    colour = "Orange"
elif wavelength <= 750:
    colour = "Red"
else:
    colour = "Infrared"

st.success(f"Predicted light colour: {colour}")

st.write("Formula: wavelength = 1240 / band-gap energy")

st.info("This is an educational semiconductor simulation.")

import plotly.graph_objects as go
import numpy as np

st.header("Band Gap vs Wavelength Graph")

energy_values = np.linspace(1.0, 3.5, 100)
wavelength_values = 1240 / energy_values

fig = go.Figure()

fig.add_trace(go.Scatter(
    x=energy_values,
    y=wavelength_values,
    mode="lines",
    name="Band Gap Relationship"
))

fig.add_trace(go.Scatter(
    x=[energy],
    y=[wavelength],
    mode="markers",
    marker=dict(size=12),
    name="Your Selection"
))

fig.update_layout(
    xaxis_title="Band Gap Energy (eV)",
    yaxis_title="Wavelength (nm)",
    title="Relationship Between Energy and Wavelength"
)

st.plotly_chart(fig, use_container_width=True)
