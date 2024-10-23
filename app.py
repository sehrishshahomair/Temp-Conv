import streamlit as st

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

# Streamlit app
def temperature_converter():
    st.title("Temperature Converter")

    # Select conversion type
    option = st.selectbox(
        "Choose conversion type:",
        ("Celsius to Fahrenheit", "Fahrenheit to Celsius")
    )

    # Based on user selection, take input and perform conversion
    if option == "Celsius to Fahrenheit":
        celsius = st.number_input("Enter temperature in Celsius:")
        if st.button("Convert"):
            fahrenheit = celsius_to_fahrenheit(celsius)
            st.success(f"{celsius}°C is equal to {fahrenheit}°F")
    
    elif option == "Fahrenheit to Celsius":
        fahrenheit = st.number_input("Enter temperature in Fahrenheit:")
        if st.button("Convert"):
            celsius = fahrenheit_to_celsius(fahrenheit)
            st.success(f"{fahrenheit}°F is equal to {celsius}°C")

if __name__ == "__main__":
    temperature_converter()
