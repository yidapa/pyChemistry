import sys
import os
from inspect import stack

sys.path.append(os.path.join(os.path.dirname(stack()[0][1]), "part"))

from Ptable import *
from Element import Element
from Compound import Compound