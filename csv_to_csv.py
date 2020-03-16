from pandas import pandas
from pathlib import Path
import os

filepath = str(input("Enter input file path:"))
filepath2 = filepath.strip('\"')
filepath3 = Path(filepath2)

outpt = str(input("Enter output file path:"))
output = outpt.strip('/"')

df1 = pandas.read_csv(filepath3)
print(list(df1.columns))

#Make changes to datafile here

output_file = os.path.join(output,'output.csv')
df1.to_csv(output_file, sep = ":")
print("Data exported")

#"C:\Users\RMAda\PycharmProjects\SixNations Analysis\Week_4_Wales\Starter_Materials\6 Nations Data Science - England.csv"
#"C:\Users\RMAda\PycharmProjects\SixNations Analysis\Week_4_Wales"
