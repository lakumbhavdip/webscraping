# import pandas as pd

# file_paths = ['C:/Users/HP/Desktop/appname.xlsx', 'C:/Users/HP/Desktop/developername.xlsx', 'C:/Users/HP/Desktop/appname.xlsx/appemail.xlsx', 'C:/Users/HP/Desktop/reviews.xlsx', 'C:/Users/HP/Desktop/charge.xlsx']
# column_names = ['Email-Phone', 'Appname', 'Developername', 'AppEmail', 'Review', 'Charge']

# dfs = []
# for file_path in file_paths:
#     data = pd.read_excel(file_path)
#     dfs.append(data)
# merged_data = pd.concat(dfs, ignore_index=True)
# merged_data.columns = column_names
# merged_data.to_excel('merged_file.xlsx', index=False)

import pandas as pd

file_paths = [
    'D:/wanbuffer/django/emailphone.xlsx',
    'D:/wanbuffer/django/appname.xlsx',
    'D:/wanbuffer/django/developername.xlsx',
    'D:/wanbuffer/django/appemail.xlsx',
    'D:/wanbuffer/django/reviews.xlsx',
    'D:/wanbuffer/django/charge.xlsx'
]
column_names = ['Email-Phone', 'Appname', 'Developername', 'AppEmail', 'Review', 'Charge']

dfs = []
for file_path in file_paths:
    data = pd.read_excel(file_path)
    dfs.append(data)

merged_data = pd.concat(dfs, axis=1)
merged_data.columns = column_names

merged_data.to_excel('merged_file.xlsx', index=False)
