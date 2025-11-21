import streamlit as st
from oncdw import ONCDW
import json

client = ONCDW() 

with open(f"data.json") as f:
    devices = json.load(f)


with st.sidebar:
    for device in devices:
        client.ui.device(device)
        for sensor in device["sensors"]:
            client.section.sensor_sidebar(sensor)

for device in devices:
    client.ui.device(device)
    for sensor in device["sensors"]:
        client.section.time_series(sensor)