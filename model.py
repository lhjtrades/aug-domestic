import csv
import os
import app

def WriteDictToCSV(csv_file,csv_columns,dict_data):
    with open(csv_file, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
            writer.writeheader()
            for data in dict_data:
                writer.writerow(data) 
    return            

# csv_columns = ['Username','Email']
# info = app.new_info
# dict_data = []
# for user in info:
#     new_user = {
#         'Username': user['username'],
#         'Email': user['email']
#     }
#     dict_data.append(new_user)

# currentPath = os.getcwd()
# csv_file = currentPath + "/csv/Names.csv"

# WriteDictToCSV(csv_file,csv_columns,dict_data)