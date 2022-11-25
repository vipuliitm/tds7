#pip install streamlit
#pip install protobuf==3.19.*
import streamlit as st
#export PROTOCOLS_BUFFERS_PYTHON_IMPLEMENTATION = python

st.header("Multiplication of Two Numbers by Vipul Arora IITM (21f1005862)")
a = st.number_input("Input First Number")
b = st.number_input("Input Second Number")
c = a*b
st.subheader("Multiplication of two numbers is")
st.write(c)
