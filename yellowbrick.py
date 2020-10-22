# from the toward data science article : https://towardsdatascience.com/quick-and-easy-model-evaluation-with-yellowbrick-295cb0752bce

# example: Random forest to UCI wine dataset
#import basic packages
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# in jupyter notebook for inline plot display
%matplotlib inline

#Get the dataset from sklearn
from kleran.dataset import load_wine
date = load_wine()

# prepare features and target for use
X= data.data
X = pf.DAtaFrame(X)
X.columns  = [x.capitalize() for x in data.feature_names]

y = data.target
