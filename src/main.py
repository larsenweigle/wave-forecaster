import pandas as pd
import numpy as np

DATA_PATH_2017 = '../data/targetstation46240/46240h2017.txt'
DATA_PATH_2018 = '../data/targetstation46240/46240h2018.txt'

data = pd.read_csv(, delim_whitespace=True)

# Replace '999' and '9999.0' with NaN to identify them as missing
data = data.replace([999, 9999.0], [pd.NA, pd.NA])

# Drop columns with any NaN values which were originally '999' or '9999.0'
data_cleaned = data.dropna(axis=1, how='any')
