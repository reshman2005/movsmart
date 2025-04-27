import streamlit as st
import json
import os

st.set_page_config(layout="wide")
st.title("Movsmart")

DATA_FILE = "/home/movsmart/bus_data.json"

def load_data():
    try:
        if not os.path.exists(DATA_FILE):
            return {"seats": [False] * 5}
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return {"seats": [False] * 5}


# Load data
data = load_data()

# Safety check
if not data or "seats" not in data:
    data = {"seats": [False] * 5}

# Display seat occupancy
st.subheader("Seat Occupancy")
cols = st.columns(len(data['seats']))

for idx, status in enumerate(data["seats"]):
    color = "green" if not status else "red"
    label = "Vacant" if not status else "Occupied"
    icon = "✔" if not status else "❌"
    cols[idx].markdown(
      f"### seat {idx +1} {icon}\n"
      f"**status:** <span style='color:{color}'>{label}</span>",
      unsafe_allow_html=True
    )