import streamlit as st
import pickle
import pandas as pd

# Page config
st.set_page_config(page_title="Apriori Results Viewer", layout="wide")

st.title("🛒 Apriori / ECLAT Results Viewer")

# Load PKL file
PKL_PATH = "all_apriori_data.pkl"

@st.cache_data
def load_pkl(path):
    with open(path, "rb") as f:
        return pickle.load(f)

try:
    data = load_pkl(PKL_PATH)
    st.success("PKL file loaded successfully ✅")
except Exception as e:
    st.error(f"Error loading PKL file: {e}")
    st.stop()

# ---- Display Logic ----

st.subheader("📦 PKL File Content")

# Case 1: Pandas DataFrame
if isinstance(data, pd.DataFrame):
    st.write("Detected type: **Pandas DataFrame**")
    st.dataframe(data)

# Case 2: Dictionary
elif isinstance(data, dict):
    st.write("Detected type: **Dictionary**")
    st.write(f"Total keys: {len(data)}")

    selected_key = st.selectbox("Select a key to view", list(data.keys()))
    st.write(data[selected_key])

# Case 3: List
elif isinstance(data, list):
    st.write("Detected type: **List**")
    st.write(f"Total items: {len(data)}")

    st.write("First 10 items:")
    st.write(data[:10])

# Case 4: Other object
else:
    st.write("Detected type:", type(data))
    st.write(data)
