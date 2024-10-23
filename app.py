import streamlit as st

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

# Streamlit app
def temperature_converter():
    st.title("🌡️ Temperature Converter")

    st.write("Use this tool to convert temperatures between Celsius and Fahrenheit.")

    # Select conversion type
    option = st.radio(
        "Select conversion type:",
        ("Celsius to Fahrenheit", "Fahrenheit to Celsius")
    )

    # Initialize temperature value and the slider ranges based on the selection
    if option == "Celsius to Fahrenheit":
        celsius = st.slider("Select temperature in Celsius:", min_value=-100.0, max_value=100.0, value=0.0)
        fahrenheit = celsius_to_fahrenheit(celsius)
        st.metric(label="Converted Temperature", value=f"{fahrenheit:.2f}°F")
    else:
        fahrenheit = st.slider("Select temperature in Fahrenheit:", min_value=-100.0, max_value=212.0, value=32.0)
        celsius = fahrenheit_to_celsius(fahrenheit)
        st.metric(label="Converted Temperature", value=f"{celsius:.2f}°C")

    # Provide an option to reset the slider
    if st.button("Reset"):
        st.experimental_rerun()

if __name__ == "__main__":
    temperature_converter()
