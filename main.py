from pandas import read_excel
from pandas import DataFrame
import os
import numpy as np

path = os.path.join(os.getcwd(), "Files")
files = os.listdir(os.path.join(os.getcwd(), "Files"))

filenames = []
file_extensions = []
datas = []


for file in files:
    filename, file_extension = os.path.splitext(os.path.join(path, file))
    filenames.append(filename)
    file_extensions.append(file_extension)

for file in files:
    datas.append(read_excel(os.path.join(path, file), sheet_name=0, decimal=","))

for i, data in enumerate(datas):
    DataFrame.to_csv(data, filenames[i] + ".csv")
