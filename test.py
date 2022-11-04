import numpy as np
import pandas as pd
import xlsxwriter as xw

df = pd.read_csv('./pairs-label-training.csv')
arr = np.zeros(2001)
for i in range(0, len(df.index)):
    arr[df.iat[i, 0]] += 1
    arr[df.iat[i, 1]] += 1

# export the numpy array to a file in the same directory
np.savetxt('train-data-for-participant.csv', arr, delimiter=',')
# export the numpy array to an excel file in the same directory
writer = pd.ExcelWriter('train-data-for-participant.xlsx', engine='xlsxwriter')
df = pd.DataFrame(arr)
df.to_excel(writer, sheet_name='Sheet1')
writer.save()



for i in range(0, len(arr)):
    print(i, arr[i])
