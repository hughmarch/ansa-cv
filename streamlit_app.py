import streamlit as st
from pathlib import Path

def read_markdown_file(markdown_file):
  return Path(markdown_file).read_text()

def caption(text):
  return f'<em style="text-align: center">{text}</em>'

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