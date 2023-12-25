import streamlit as st
from df_handler import DataframeHandler

st.title("Dataframe Visualizer") # GUI title

# st.sidebar -> Left panel sidebar
st.sidebar.text_input("Dataframe Path", key="file_path", placeholder="data/filename.csv")
st.write("Dataframe:", st.session_state.file_path)

df_handler = DataframeHandler(st.session_state.file_path)

st.dataframe(df_handler.df) # Render Dataframe

st.write("Shape:", df_handler.get_shape())
st.write("Columns:", df_handler.get_columns())
