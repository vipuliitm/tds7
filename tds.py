!pip install streamlit
import streamlit as st
PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION=python

st.header("Multiplication of Two Numbers")
a = st.number_input("Input First Number")
b = st.number_input("Input Second Number")
c = a*b
st.subheader("Multiplication of two numbers is")
st.write(c)
