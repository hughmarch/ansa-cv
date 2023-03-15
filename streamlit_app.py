import streamlit as st
from pathlib import Path
import time
import model
import numpy as np

def read_markdown_file(markdown_file):
  return Path(markdown_file).read_text()

def caption(text):
  return f'<em style="text-align: center">{text}</em>'

@st.cache_data
def import_data(filepath):
    return model.ImportTifData(filepath)

st.markdown(read_markdown_file("markdown/intro1.md"))
st.image("figs/hivstats.png")
st.markdown(caption("Data from WHO"), unsafe_allow_html=True)
st.markdown(read_markdown_file("markdown/intro2.md"))
st.markdown(caption("Top: number of copies of HIV DNA. A higher copy number means higher viral load."), unsafe_allow_html=True)
st.image("figs/membranespots.png")
st.markdown(caption("RPA Performed on fiber membrane. Quantification becomes difficult at higher copy numbers."), unsafe_allow_html=True)


st.header("Objective")
st.markdown(read_markdown_file("markdown/objective1.md"))
st.image("figs/glass_slide_data_1e5cps.png")
st.markdown(caption("RPA Performed on glass slides with 10,000cps HIV DNA. Left: low viscosity, Right: high viscosity. " + 
                    "This demonstrates that it may be possible to quantify at higher copy numbers."), unsafe_allow_html=True)

st.header("Methods")
st.markdown(read_markdown_file("markdown/data_collection1.md"), unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
  with st.spinner("Importing data..."):
    data = import_data("experiments/1.5% PEG.tiff")
    t = st.slider('1.5% PEG', 0, 900, 0, 10)
    t = int(t / 10)

    x = data[t]
    st.image((x-np.min(x))/(np.max(x)-np.min(x)))

with col2:
  with st.spinner("Importing data..."):
    data = import_data("experiments/6.78% PEG.tiff")
    t = st.slider('6.78% PEG', 0, 900, 0, 10)
    t = int(t / 10)

    x = data[t]
    st.image((x-np.min(x))/(np.max(x)-np.min(x)))

st.markdown(caption("Note: these images have normalized intensities based on extrema, so even though they look like they " +
                    "have different intensities, they are actually about the same (as we will see later)!"), unsafe_allow_html=True)

st.markdown(read_markdown_file("markdown/methods1.md"))