import streamlit as st
import pandas as pd
from df_handler import DataframeHandler

st.title("Dataframe Visualizer") # GUI title

# st.sidebar -> Left panel sidebar
input_file = st.sidebar.file_uploader("Upload Dataframe", key="file_uploader", type=["csv"])

if input_file: 
    df_handler = DataframeHandler(df=pd.read_csv(input_file))
else: 
    df_handler = DataframeHandler(df=pd.DataFrame())

st.dataframe(df_handler.df) # Render Dataframe

st.write("Shape:", df_handler.get_shape())
st.write("Columns:", df_handler.get_columns())
