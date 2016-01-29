import chemlib

element = "C"
mm = chemlib.getMolarMass(element)
name = chemlib.getName(element)
an = chemlib.getAtomicNumber(element)
print (name, "has a molar mass of", mm,  "and atomic number of", an)
compound = "C6H12O6" #of course glucose :P
glucose = chemlib.Compound(compound)
text = glucose.getMolarMass()
print(text)
