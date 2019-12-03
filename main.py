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
	env.filters["escape"] = escape
	template = env.get_template("required.tex")
	
	
	with open("output/result.tex", "w") as f:
		f.write(template.render(recipes=recipes))

def escape(in_text):
	"""Function to escape any characters that may cause trouble in the latex file"""
	mapping = {
		ord('#'):  r"\#",
		ord('$'):  r"\$",
		ord('%'):  r"\%",
		ord('&'):  r"\&",
		ord("\\"): r"\textbackslash{}",
		ord("^"):  r"\textasciicircum{}",
		ord('_'):  r"\_",
		ord("{"):  r"\{",
		ord("}"):  r"\}",
		ord("~"):  r"\textasciitilde{}"
	}
	return in_text.translate(mapping)

if __name__ == '__main__':
	main()
