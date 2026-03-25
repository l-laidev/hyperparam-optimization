import pandas as pd
import numpy as np

from sklearn import ensemble
from sklearn import metrics
from sklearn import model_selection
from sklearn import preprocessing
from sklearn import decomposition
from sklearn import pipeline

from skopt import space
from skopt import gp_minimize

from functools import partial


TRAIN_CSV = "../train.csv"

df = pd.read_csv(TRAIN_CSV)
X = df.drop("price_range", axis=1).values
y = df["price_range"].values
