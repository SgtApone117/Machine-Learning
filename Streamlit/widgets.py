import streamlit as st
import pandas as pd

st.title("Streamlit Text Input")

name = st.text_input("Enter your name:")

age = st.slider("Select your age:",0,100,25)

st.write(f"Your age is {age}.")

options = ["Halo Combat Evolved", "Halo 2", "Halo 3", "Halo 3:ODST", "Halo: Reach"]
choice = st.selectbox("Choose your favorite Halo game:", options)
st.write(f"You selected {choice}.")

if name:
    st.write(f"Hello, {name}!")


data = {
    "Name": ["Dhaumya", "Dhrishtadyumna","Dhananjaya", "Kripa"],
    "Weapons": ["Kaumodaki", "Kodanda", "Gada", "Chakra"],
    "City": ["Indraprastha","Brindavana","Mathura", "Mithila"]
}

df = pd.DataFrame(data)
df.to_csv("sampledata.csv")
st.write(df)

uploaded_files = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_files is not None:
    df = pd.read_csv(uploaded_files)
    st.write(df)
