import numpy as np
import iris
import iris.plot as iplt
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import numpy as np
import warnings
import pickle
import copy
import sys, os
import seaborn as sns
import pandas as pd
import scipy as sp


warnings.filterwarnings("ignore")
plt.ion()
plt.close('all')
nWTs     = 9    # number of weather types
brewer_cmap = plt.get_cmap('brewer_RdBu_11') 
RdBu = plt.get_cmap('brewer_RdBu_11') 
cw = plt.get_cmap('coolwarm') 

