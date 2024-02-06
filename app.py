from fastai.vision.core import PILImage
from fastai.learner import load_learner
import streamlit as st

model = load_learner("./model.pkl")
file = st.file_uploader("Upload photo")
if file:
    st.image(file)
    img  = PILImage.create((file))
    st.write(model.predict(img))

st.checkbox('asdasd')
print("dd")
