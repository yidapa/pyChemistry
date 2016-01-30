pyChemistry
----------------

A lightweight Python library for chemistry.
This library only currently supports basic periodic table stuff like molar masses, chemicals and atomic numbers.... So just check this repository for updates every so often.

To begin using this library navigate to the pyChemistry directory and run:
```
python setup.py install
```
This installs all appropriate files that are required to use this library and sets everything up for you.
Examples:
```python
import chemlib

element = "C"
mm = chemlib.getMolarMass(element)
name = chemlib.getName(element)
an = chemlib.getAtomicNumber(element)
print "{0} has a molar mass of {1} and atomic number of {2}".format(name, mm, an)
```
```python
compound = "C6H12O6" # glucose if you didn't know already
glucose = chemlib.Compound(compound)
print compound.getMolarMass()
```
