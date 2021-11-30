#%%
import pandas as pd
import numpy as np
from benfordslaw import benfordslaw
import sys
#%%


def cleanPopData(df):
    return np.apply_along_axis(np.vectorize(lambda x: int(x) if x.isnumeric() else 0), \
        -1, df[df.columns[4:]].to_numpy().flatten())



def benfordize(path, cleaner):
    df = pd.read_csv(path)
    bl = benfordslaw()
    data = cleanPopData(df)
    return bl.fit(data)['percentage_emp']

#%%
 
if __name__ == '__main__':
    path = sys.argv[1]
    cleaner = sys.argv[2]
    outpath = sys.argv[3]
    if path == 'USA':
        bl = benfordslaw()
        df = bl.import_example("USA")
        dist = bl.fit(df['votes'].loc[df['candidate']=='Donald Trump'].values)['percentage_emp']
    elif path == 'RUS':
        bl = benfordslaw()
        df = bl.import_example("RUS")
        dist = bl.fit(df['Putin Vladimir Vladimirovich'])['percentage_emp']
    else: dist = benfordize(path, cleaner)
    with open(outpath, "w") as f:
        f.write(" ".join([str(i) for i in dist[:, 1]]))
# %%
