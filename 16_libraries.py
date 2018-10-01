# Libraries contain code that is not loaded in the default 
# namespace. Some are part of the standard Python 
# distribution. To use them, we must import them, but only
# import what you need!

import math # many useful math functions

import random # functions for random numbers/operations

import re # regular expression library

import os # operating system functions

import json # javascript object notation library

# You can find all of them here: 
# https://docs.python.org/3/library/

# Anaconda contains many additional libraries that we will be
# using

# The natural language toolkit, contains many NLP functions
import nltk 

# Library for plotting information
import matplotlib 

# Library for data munging and visualization
import pandas 

# The NumbersPython library, useful for scientific computing
import numpy 

# You can find all of them here: 
# https://docs.anaconda.com/anaconda/packages/pkg-docs

# Aliases. Sometimes you will want to use an alias to import 
# a library

# Do this so you only have to type pd in your code, not pandas
import pandas as pd 

# Important individual module. Sometimes you don't need the 
# whole library:
from matplotlib import pyplot # Import only the pyplot module

# You can combine this:
from matplotlib import pyplot as plt

# Also:
import matplotlib.pyplot as plt