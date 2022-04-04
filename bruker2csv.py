import os
import nmrglue as ng
import numpy as np
import pandas as pd

# Define the path to the file you want to export below (ex: C/Bruker/TopSpin4.1.3/data/sample/pdata/1)
data_dir = os.path.normpath('INSERT DIRECTORY HERE')

dic, data = ng.bruker.read_pdata(data_dir)
udic = ng.bruker.guess_udic(dic, data)
uc = ng.fileiobase.uc_from_udic(udic)
ppm_scale = uc.ppm_scale()
norm_data = data/data.max()
df = pd.DataFrame()
df['ppm'] = ppm_scale
df['int'] = data
df['norm int'] = norm_data
df.to_csv('sample_name.csv', index=False)