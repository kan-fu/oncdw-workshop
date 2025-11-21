import streamlit as st
from oncdw import ONCDW

client = ONCDW() 

devices = [
    {
        "device_id": 21501,
        "device_code": "BPR-1027NW",
        "sensors": [
            {"sensor_id": 4182, "sensor_name": "Seafloor Pressure"},
            {"sensor_id": 7712, "sensor_name": "Uncompensated Seafloor Pressure"},
        ],
    },
    {
        "device_id": 12501,
        "device_code": "BPR_BC",
        "sensors": [{"sensor_id": 4176, "sensor_name": "Seafloor Pressure"}],
    },
]

with st.sidebar:
    for device in devices:
        client.ui.device(device)
        for sensor in device["sensors"]:
            client.section.sensor_sidebar(sensor)

for device in devices:
    client.ui.device(device)
    for sensor in device["sensors"]:
        client.section.time_series(sensor)