pip install streamlit
pip install protobuf==3.20.*
import streamlit as st

st.header("Multiplication of Two Numbers")
a = st.number_input("Input First Number")
b = st.number_input("Input Second Number")
c = a*b
st.subheader("Multiplication of two numbers is")
st.write(c)
