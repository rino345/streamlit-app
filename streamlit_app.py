import streamlit as st
import pandas as pd
import numpy as np

st.title('🎈 Hello world app')

st.write('Hello world!')

with st.sidebar:
  st.header("About app")
  st.write("This is my first app")

st.subheader("st.columns")
col1,col2 = st.columns(2)
with col1:
  x = st.slider("Choose an x value",1,10)
with col2:
  st.write("The value of :blue[x]",x)

st.subheader("st.area_chart")
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
st.area_chart(chart_data)

