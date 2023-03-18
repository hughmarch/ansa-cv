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

@st.cache_data
def center_crop(img):
  return model.centerCrop(img)

@st.cache_data
def moving_avg(img):
  return model.averageImg(img)

@st.cache_data
def background_sub(img):
  return model.backgroundSub(img)

@st.cache_data
def box_blur(img):
  return model.averageBlur(img)

st.markdown(read_markdown_file("markdown/intro1.md"), unsafe_allow_html=True)
st.image("figs/hivstats.png")
st.markdown(caption("Data from WHO"), unsafe_allow_html=True)
st.markdown(read_markdown_file("markdown/intro2.md"), unsafe_allow_html=True)
st.markdown(caption("Viral load in this work is measured as number of viral DNA " +
                    "copies per reaction, abbreviated as \"cps/rxn\" or just \"cps.\""), unsafe_allow_html=True)
st.image("figs/membranespots.png")
st.markdown(caption("RPA Performed on fiber membrane<sup>1</sup>. At lower copy numbers (<3000cps), the number of sites " +
                    "to the number of copies follows a power-law relationship. Quantification becomes difficult " +
                    "at higher copy numbers."), unsafe_allow_html=True)


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

st.markdown(read_markdown_file("markdown/methods1.md"), unsafe_allow_html=True)
st.image("figs/pipeline.png")
st.markdown(read_markdown_file("markdown/methods2.md"), unsafe_allow_html=True)

options = ["Moving average", "Background subtraction", "Box blur filter"]
steps = [moving_avg, background_sub, box_blur]

option = st.slider(f"Look at different steps (1 for moving average, 2 for background subtraction, 3 for box blur filter):", 1, 3, 1, 1)
st.markdown(f"**Current images: {' + '.join([o for o in options[:option]])}**")

col1, col2 = st.columns(2)

with col1:
  with st.spinner("Loading data..."):
    img = import_data("experiments/1.5% PEG avg.tiff")
    for i in range(1, option):
      img = steps[i](img)
    
    t = st.slider('1.5% PEG ', 0, 900, 900, 10)
    t = int(t / 10)
    x = img[t]
    st.image((x-np.min(x))/(np.max(x)-np.min(x)))

with col2:
  with st.spinner("Loading data..."):
    img = import_data("experiments/6.78% PEG avg.tiff")
    for i in range(1, option):
      img = steps[i](img)
    
    t = st.slider('6.78% PEG ', 0, 900, 900, 10)
    t = int(t / 10)
    x = img[t]
    st.image((x-np.min(x))/(np.max(x)-np.min(x)))

st.markdown(read_markdown_file("markdown/methods3.md"), unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
  st.image("figs/1.5% PEG sites.png")
  st.markdown(caption("1.5% PEG selected nucleation sites"), unsafe_allow_html=True)

with col2:
  st.image("figs/6.78% PEG sites.png")
  st.markdown(caption("6.78% PEG selected nucleation sites"), unsafe_allow_html=True)

st.markdown("#### Site analysis")

col1, col2 = st.columns(2)

with col1:
  st.markdown(read_markdown_file("markdown/methods4.md"))

with col2:
  st.image("figs/site_surface_plot.png")
  st.markdown("*Surface plot image of a nucleation site @ t=900s, 1.5% PEG*")

col1, col2 = st.columns(2)

with col1:
  st.image("figs/gaussian_high.png")

with col2:
  st.image("figs/gaussian_low.png")

st.markdown(caption("An example of what two nucleation sites with similar radii but different intensities might " +
                    "look like. If we define radius with a threshold or cutoff value, the site with lower intensity " +
                    "(right) will be measured to have a lower radius."), unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
  st.markdown(read_markdown_file("markdown/methods5.md"))

with col2:
  st.image("figs/gaussian_approximation.png")
  st.markdown("*Surface plot (blue) with gaussian approximation (red)*")

st.markdown("For our purposes, we'll define our radius to be 2 * standard deviation, or at the 95% confidence interval.")

st.header("Results")
st.image("figs/radius_plot.png")
st.image("figs/intensity_plot.png")

st.markdown(caption("Measurements of individual sites (dotted lines) and averages of all sites in an experiment (solid lines). "),
                    unsafe_allow_html=True)

st.markdown(read_markdown_file("markdown/results1.md"))

st.header("Next steps")
st.markdown(read_markdown_file("markdown/nextsteps.md"), unsafe_allow_html=True)

st.header("References")
st.markdown(read_markdown_file("markdown/references.md"), unsafe_allow_html=True)