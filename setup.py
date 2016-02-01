import os
from setuptools import setup

setup(
	name = "pyChem",
	version = "1",
	description = "A lightweight library for chemistry",
	author = "James Gallagher",
	author_email = "jamesgallagher507@gmail.com",
	license = "MIT",

	packages = ["pyChem", os.path.join("pyChem", "part")]
	)
