
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

st.header("Quantum Dot Size Simulator")

st.write("Explore how quantum dot size affects the energy band gap.")

dot_size = st.slider(
    "Choose quantum dot diameter (nm)",
    min_value=2.0,
    max_value=10.0,
    value=5.0,
    step=0.5
)

bulk_gap = st.number_input(
    "Bulk material band gap (eV)",
    min_value=0.1,
    max_value=3.0,
    value=1.1,
    step=0.1
)

# Illustrative model only; not calibrated to a specific material
effective_gap = bulk_gap + (3.0 / (dot_size ** 2))

st.metric(
    "Illustrative effective band gap",
    f"{effective_gap:.3f} eV"
)

st.header("Quantum Dot Size vs Band Gap")

dot_sizes = np.linspace(2.0, 10.0, 100)
band_gaps = bulk_gap + (3.0 / (dot_sizes ** 2))

fig2 = go.Figure()

fig2.add_trace(go.Scatter(
    x=dot_sizes,
    y=band_gaps,
    mode="lines",
    name="Band Gap"
))

fig2.add_trace(go.Scatter(
    x=[dot_size],
    y=[effective_gap],
    mode="markers",
    marker=dict(size=12),
    name="Selected Dot Size"
))

fig2.update_layout(
    xaxis_title="Quantum Dot Diameter (nm)",
    yaxis_title="Illustrative Band Gap (eV)",
    title="Effect of Quantum Dot Size on Band Gap"
)

st.plotly_chart(fig2, use_container_width=True)

st.info(
    "Smaller quantum dots generally have a larger band gap. "
    "This is a simplified demonstration model, not a material-calibrated prediction."
)

st.header("Theory of QuantumLED")

st.subheader("1. What is a Band Gap?")
st.write(
    "The band gap is the energy difference between the valence band "
    "and the conduction band in a semiconductor. It is measured in electron volts (eV)."
)

st.subheader("2. What is Quantum Confinement?")
st.write(
    "Quantum confinement occurs when semiconductor particles become very small. "
    "Their energy levels change, and the effective band gap generally increases "
    "as the particle size decreases."
)

st.subheader("3. How Does an LED Produce Light?")
st.write(
    "When electrons combine with holes in a semiconductor, energy can be released "
    "as light. The band gap influences the wavelength and colour of the emitted light."
)

st.subheader("4. Applications")
st.markdown("""
- **LED displays:** Producing different colours of light.
- **Quantum dot displays:** Improving display colour and brightness.
- **Solar cells:** Studying light absorption and energy conversion.
- **Sensors:** Detecting changes in the surrounding environment.
""")

st.subheader("5. Important Formula")

st.latex(r"E_g = \frac{1240}{\lambda}")

st.write(
    "Here, Eg is the photon energy in eV and wavelength is in nanometres (nm). "
    "This formula relates photon energy to wavelength."
)

st.header("LED Colour Indicator")

st.write("See the approximate visible-light colour for your selected band gap.")

if wavelength >= 620 and wavelength <= 750:
    st.markdown("### 🔴 Red")
elif wavelength >= 590:
    st.markdown("### 🟠 Orange")
elif wavelength >= 570:
    st.markdown("### 🟡 Yellow")
elif wavelength >= 495:
    st.markdown("### 🟢 Green")
elif wavelength >= 450:
    st.markdown("### 🔵 Blue")
elif wavelength >= 380:
    st.markdown("### 🟣 Violet")
else:
    st.markdown("### Outside the visible-light range")

st.write(f"Calculated wavelength: {wavelength:.2f} nm")

st.header("About This Project")

st.write("**Project Title:** QuantumLED — Quantum-Confined LED and Semiconductor Band-Gap Demonstrator")

st.write("""
**Objective:** To demonstrate the relationship between semiconductor band-gap
energy, wavelength, and quantum dot size using an interactive website.

**Technology Used:**
- Python
- Streamlit
- NumPy
- Plotly

**Main Features:**
- Band-gap energy and wavelength calculator
- Energy versus wavelength graph
- Quantum dot size simulator
- Band gap versus dot size graph
- LED colour indicator
- Semiconductor theory and applications
""")

st.info(
    "This website is an educational simulation. "
    "Its simplified quantum-dot model is illustrative and is not calibrated "
    "to a specific semiconductor material."
)

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

st.header("Quantum Dot Size Simulator")

st.write("Explore how quantum dot size affects the energy band gap.")

dot_size = st.slider(
    "Choose quantum dot diameter (nm)",
    min_value=2.0,
    max_value=10.0,
    value=5.0,
    step=0.5
)

bulk_gap = st.number_input(
    "Bulk material band gap (eV)",
    min_value=0.1,
    max_value=3.0,
    value=1.1,
    step=0.1
)

# Illustrative model only; not calibrated to a specific material
effective_gap = bulk_gap + (3.0 / (dot_size ** 2))

st.metric(
    "Illustrative effective band gap",
    f"{effective_gap:.3f} eV"
)

st.header("Quantum Dot Size vs Band Gap")

dot_sizes = np.linspace(2.0, 10.0, 100)
band_gaps = bulk_gap + (3.0 / (dot_sizes ** 2))

fig2 = go.Figure()

fig2.add_trace(go.Scatter(
    x=dot_sizes,
    y=band_gaps,
    mode="lines",
    name="Band Gap"
))

fig2.add_trace(go.Scatter(
    x=[dot_size],
    y=[effective_gap],
    mode="markers",
    marker=dict(size=12),
    name="Selected Dot Size"
))

fig2.update_layout(
    xaxis_title="Quantum Dot Diameter (nm)",
    yaxis_title="Illustrative Band Gap (eV)",
    title="Effect of Quantum Dot Size on Band Gap"
)

st.plotly_chart(fig2, use_container_width=True)

st.info(
    "Smaller quantum dots generally have a larger band gap. "
    "This is a simplified demonstration model, not a material-calibrated prediction."
)

st.header("Theory of QuantumLED")

st.subheader("1. What is a Band Gap?")
st.write(
    "The band gap is the energy difference between the valence band "
    "and the conduction band in a semiconductor. It is measured in electron volts (eV)."
)

st.subheader("2. What is Quantum Confinement?")
st.write(
    "Quantum confinement occurs when semiconductor particles become very small. "
    "Their energy levels change, and the effective band gap generally increases "
    "as the particle size decreases."
)

st.subheader("3. How Does an LED Produce Light?")
st.write(
    "When electrons combine with holes in a semiconductor, energy can be released "
    "as light. The band gap influences the wavelength and colour of the emitted light."
)

st.subheader("4. Applications")
st.markdown("""
- **LED displays:** Producing different colours of light.
- **Quantum dot displays:** Improving display colour and brightness.
- **Solar cells:** Studying light absorption and energy conversion.
- **Sensors:** Detecting changes in the surrounding environment.
""")

st.subheader("5. Important Formula")

st.latex(r"E_g = \frac{1240}{\lambda}")

st.write(
    "Here, Eg is the photon energy in eV and wavelength is in nanometres (nm). "
    "This formula relates photon energy to wavelength."
)

st.header("LED Colour Indicator")

st.write("See the approximate visible-light colour for your selected band gap.")

if wavelength >= 620 and wavelength <= 750:
    st.markdown("### 🔴 Red")
elif wavelength >= 590:
    st.markdown("### 🟠 Orange")
elif wavelength >= 570:
    st.markdown("### 🟡 Yellow")
elif wavelength >= 495:
    st.markdown("### 🟢 Green")
elif wavelength >= 450:
    st.markdown("### 🔵 Blue")
elif wavelength >= 380:
    st.markdown("### 🟣 Violet")
else:
    st.markdown("### Outside the visible-light range")

st.write(f"Calculated wavelength: {wavelength:.2f} nm")

st.header("About This Project")

st.write("**Project Title:** QuantumLED — Quantum-Confined LED and Semiconductor Band-Gap Demonstrator")

st.write("""
**Objective:** To demonstrate the relationship between semiconductor band-gap
energy, wavelength, and quantum dot size using an interactive website.

**Technology Used:**
- Python
- Streamlit
- NumPy
- Plotly

**Main Features:**
- Band-gap energy and wavelength calculator
- Energy versus wavelength graph
- Quantum dot size simulator
- Band gap versus dot size graph
- LED colour indicator
- Semiconductor theory and applications
""")

st.info(
    "This website is an educational simulation. "
    "Its simplified quantum-dot model is illustrative and is not calibrated "
    "to a specific semiconductor material."
)
