import streamlit as st
import json
from jinja2 import Template
from streamlit_ace import st_ace

st.set_page_config(layout="wide")

st.title("Jinja2 Playground")

st.header("Boilerplate jinja2 script file")

st.code(
    """
import jinja2
import json

environment = jinja2.Environment(loader=jinja2.FileSystemLoader("./"))
template = environment.get_template("./template.txt")

with open("./data.json") as f:
    context = json.load(f)

content = template.render(context)

print(content)
"""
)

template_string_value = """
{% for device in devices %}
Generating device {{ device.device_id }} with device code {{ device.device_code }}.
  {% for sensor in device.sensors %}
    {% if "Uncompensated" in sensor.sensor_name %}
    - Plotting Uncompensated sensor time series for sensor ID: {{ sensor.sensor_id }}, Name: {{ sensor.sensor_name }}
    {% else %}
    - Plotting sensor time series for sensor ID: {{ sensor.sensor_id }}, Name: {{ sensor.sensor_name }}
    {% endif %}
  {% endfor %}
{% endfor %}"""

context_string_value = """
{
  "devices": [
    {
      "device_id": 21501,
      "device_code": "BPR-1027NW",
      "sensors": [
        { "sensor_id": 4182, "sensor_name": "Seafloor Pressure" },
        { "sensor_id": 7712, "sensor_name": "Uncompensated Seafloor Pressure" }
      ]
    },
    {
      "device_id": 12501,
      "device_code": "BPR_BC",
      "sensors": [{ "sensor_id": 4176, "sensor_name": "Seafloor Pressure" }]
    }
  ]
}
"""

col1, col2 = st.columns(2)

with col1:
    st.text("data.json")
    context = st_ace(value=context_string_value, language="json")
    st.text("template.txt")
    template_string = st_ace(value=template_string_value, language="python")


# Create a Template object
template = Template(template_string)

# Render the template with data
rendered_output = template.render(json.loads(context))

with col2:
    if st.button("Render Template"):
        st.text(rendered_output)
