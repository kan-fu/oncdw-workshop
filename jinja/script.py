import jinja2
import json

environment = jinja2.Environment(loader=jinja2.FileSystemLoader("./"))
template = environment.get_template("jinja/template.txt")

with open("jinja/data.json") as f:
    context = json.load(f)

content = template.render(context)

print(content)

# Write the rendered content to output.txt
# with open("output.txt", "w") as f:
#     f.write(content)