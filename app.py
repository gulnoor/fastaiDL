import streamlit as st
import pandas as pd
st.header('asdas')
st.write('gg')
b = st.button('click me')
if b:
    st.write('thanks')
else:
    st.write('ok')
st.write('Hello, *World!* :sunglasses:')
data = pd.DataFrame({'name':['aa','gg'],'value':[1,2]})
st.write(data)
