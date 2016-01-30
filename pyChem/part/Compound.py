from Ptable import getMolarMass
from re import findall, search


class Compound():
	def __init__(self, compound_string):
		self.elements = {}
		raw_elements = findall("[A-Z][a-z]?[a-z]?[1-9]?[0-9]?", compound_string)
		for element in raw_elements:
			if element[-1].isdigit():
				self.elements[search("[A-Z][a-z]?[a-z]?", element).group(0)] = int(search("[1-9][0-9]?", element).group(0))
			else:
				self.elements[search("[A-Z][a-z]?[a-z]?", element).group(0)] = 1

	def getMolarMass(self):
		mm = 0.0
		for element in self.elements.keys():
			mm += getMolarMass(element) * self.elements[element]
		return mm