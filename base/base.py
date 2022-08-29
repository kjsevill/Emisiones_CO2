# Import python libraries
import streamlit as st
import pandas as pd
from PIL import Image
import numpy as pd
import matplotlib.pyplot as plt


icon = Image.open("resources/co2.jpg")
# Page Layout
st.set_page_config(page_title="CO2 APP", page_icon=icon)
# CSS code to improve the design of the web app
st.markdown(
    """
<style>
h1 {text-align: center;
}
body {background-color: #DCE3D5;
      width: 1400px;t
      margin: 15px auto;
}
</style>""",
    unsafe_allow_html=True,
)

# Title of app
st.title("Emisiones de Co2 de fuentes estacionarias ")
st.write("---")
st.markdown(
    """This project consists of creating an application for the management of CO2 emissions from stationary sources such as those produced in refineries and thermoelectric plants.
 - **Python Libraries:** streamlit, pandas, numpy, plotly, PIL, sqlalchemy, seaborn
 """
)
image = Image.open("resources/co2-min-e1523637195662-800x394.jpg")
st.image(image, width=100, use_column_width=True)
with st.sidebar:
    options = option_menu(
        menu_title="Main Menu",
        options=[
            "Home",
            "Data",
            "Plots",
        ],
        icons=["house", "droplet-fill", "droplet"],
    )
