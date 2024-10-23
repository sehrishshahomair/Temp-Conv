import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Function to create a temperature visualization
def plot_temperature(temp, unit):
    fig, ax = plt.subplots(figsize=(2, 6))
    colors = plt.cm.coolwarm(np.linspace(0, 1, 100))
    ax.imshow([colors], aspect='auto', extent=[0, 10, -100, 100])

    if unit == "Celsius":
        temp_value = temp
    else:
        temp_value = fahrenheit_to_celsius(temp)

    ax.plot([0, 10], [temp_value, temp_value], color="black", lw=2)
    ax.set_xlim(0, 10)
    ax.set_ylim(-100, 100)
    ax.set_xticks([])
    ax.set_yticks(np.arange(-100, 101, 25))
    ax.set_title(f"{temp:.2f}° {unit}")
    st.pyplot(fig)

# Streamlit app
def temperature_converter():
    st.title("🌡️ Temperature Converter")
    st.write("Convert temperatures between Celsius and Fahrenheit.")

    # Two-way input system: single slider for conversion
    st.write("Use the slider to dynamically adjust and see the temperature in both Celsius and Fahrenheit.")
    temp_in_celsius = st.slider("Select Temperature (in Celsius):", min_value=-100.0, max_value=100.0, value=0.0)

    # Calculate Fahrenheit equivalent
    temp_in_fahrenheit = celsius_to_fahrenheit(temp_in_celsius)

    # Display both Celsius and Fahrenheit
    col1, col2 = st.columns(2)
    col1.metric(label="Celsius", value=f"{temp_in_celsius:.2f}°C")
    col2.metric(label="Fahrenheit", value=f"{temp_in_fahrenheit:.2f}°F")

    # Interactive visualization of the temperature
    plot_temperature(temp_in_celsius, "Celsius")

    # Provide warning based on extreme temperatures
    if temp_in_celsius >= 50:
        st.warning("🔥 It's extremely hot! Be cautious.")
    elif temp_in_celsius <= -30:
        st.warning("❄️ It's freezing cold! Stay warm.")

    # Allow users to switch units for the thermometer plot
    selected_unit = st.radio("Display temperature as:", ("Celsius", "Fahrenheit"))

    if selected_unit == "Celsius":
        plot_temperature(temp_in_celsius, "Celsius")
    else:
        plot_temperature(temp_in_fahrenheit, "Fahrenheit")

    # Provide an option to reset the slider
    if st.button("Reset"):
        st.experimental_rerun()

if __name__ == "__main__":
    temperature_converter()
