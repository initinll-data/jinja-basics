from jinja2 import Environment

env = Environment()
template = env.from_string("Hello {{ name }} !")
result = template.render(name="World")
print(result)
