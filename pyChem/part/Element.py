from re import search


class Element():
	def __init__(self, element_string):
		self.count = search("[0-9][1-9]", element_string)