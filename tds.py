!pip install streamlit
import streamlit as st
import numpy as np

st.header("Multiplication of Two Numbers")
a = st.number_input("Input First Number")
b = st.number_input("Input Second Number")
c = np.multiply(a,b)
st.subheader("Multiplication of two numbers is")
st.write(c)
