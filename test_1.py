import pandas as pd
import numpy as  np
import scipy as sp
from ggplot import *
import statsmodels.api as sm


df = pd.read_csv('/Users/mike/PycharmProject/stroop_data_py/stroopdata.csv')

print df.describe()