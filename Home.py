import streamlit as st
from oncdw import ONCDW

client = ONCDW() 

with st.sidebar:
    client.ui.device_sidebar({"device_id": 21501, "device_code": "BPR-1027NW"})
    client.ui.sensor_sidebar({"sensor_id": 4182, "sensor_name": "Seafloor Pressure"})
    client.ui.sensor_sidebar(
        {"sensor_id": 7712, "sensor_name": "Uncompensated Seafloor Pressure"}
    )
    client.ui.device_sidebar({"device_id": 12501, "device_code": "BPR_BC"})
    client.ui.sensor_sidebar({"sensor_id": 4176, "sensor_name": "Seafloor Pressure"})

client.ui.device({"device_id": 21501, "device_code": "BPR-1027NW"})
sensor1 = {"sensor_id": 4182, "sensor_name": "Seafloor Pressure"}
client.section.time_series(sensor1)
sensor2 = {"sensor_id": 7712, "sensor_name": "Uncompensated Seafloor Pressure"}
client.section.time_series(sensor2)
client.ui.device({"device_id": 12501, "device_code": "BPR_BC"})
sensor1 = {"sensor_id": 4176, "sensor_name": "Seafloor Pressure"}
client.section.time_series(sensor1)