import json
import sys
from jinja2 import Environment, FileSystemLoader, select_autoescape
import jinja2.utils


def main():
	# checking the number of arguments
	if len(sys.argv) < 2:
		print("You need to supply some recipes to be converted")
		exit()

	with open(sys.argv[1], "r") as f:
		recipes = json.load(f)

	env = Environment(
		loader=FileSystemLoader(searchpath="templates/"),
		enable_async=True,
		auto_reload=False  # should only load and render once
	)
	env.filters["escapetex"] = escapetex
	template = env.get_template("required.tex")
	
	
	with open("output/result.tex", "w") as f:
		f.write(template.render(recipes=recipes))
	
def escapetex(input):
	replacements = [
		("{", r"\{"),
		("]", r"\}"),
		("\\", r"\textbackslash{}"),
		('$',  r'\$'),
		('%',  r'\%'),
		('&',  r'\&'),
		('#',  r'\#'),
		('_',  r'\_')
	]
	mapping = dict((ord(char), replace) for char, replace in replacements)
	return input.translate(mapping)

if __name__ == '__main__':
	main()
