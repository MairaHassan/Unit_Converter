import streamlit as st

def convert_units(value, unit_from, unit_to):

    conversions = {
        "meter_kilometer": 0.001, # 1 meter = 0.001 kilometer
        "kilometer_meter": 1000,
        "gram_kilogram": 0.001,
        "kilogram_gram": 1000,
    }
     
    key = f"{unit_from}_{unit_to}" # Generate a key base on the input and output units
    
    if key in conversions:
        conversions = conversions[key]
        return value * conversions
    else:
        return "Conversion not found"

st.title("Unit Converter")

value = st.number_input("Enter a value", min_value=1.0, step=1.0)

unit_from = st.selectbox("Convert from", ["meter", "kilometer", "gram", "kilogram"])

unit_to = st.selectbox("Convert to", ["meter", "kilometer", "gram", "kilogram"])

if st.button("Convert"):
    result = convert_units(value, unit_from, unit_to)
    st.write(f"Converted value: {result}")


        
