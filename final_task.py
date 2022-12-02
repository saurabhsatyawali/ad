import pandas as pd

file_data = pd.read_csv('TestData1.csv')
# file_data=pd.read_excel('TestData1.xlsx')
column_name=list(file_data.columns)
if 'Category Code' in column_name and 'Attribute_Suggestion_1' in column_name:
    list1 = []
    for index, series in file_data.iterrows():
        i = 1
        empty_dict = {}
        while i < 51:
            name1 = str(series['Attribute Name ' + str(i)])
            value1 = str(series['Attribute_Suggestion_' + str(i)])
            if name1 == 'nan':
                break
            if name1 != 'nan' and value1 != 'nan':
                empty_dict[name1] = value1
            i = i + 1
        list1.append(empty_dict)
    file_data['SPECS'] = list1
    column_list = ['row_id', 'Category Code', 'SPECS']


elif 'Category Code' in column_name and 'Attribute_Suggestion_1' not in column_name:
    list1 = []
    for index, series in file_data.iterrows():
        i = 1
        empty_dict = {}
        while i < 51:
            name1 = str(series['Attribute Name ' + str(i)])
            value1 = str(series['Attribute Value ' + str(i)])
            uom1 = str(series['Attribute UOM ' + str(i)])
            if name1 == 'nan':
                break
            if name1 != 'nan' and value1 != 'nan':
                if uom1 != 'nan':
                    empty_dict[name1] = value1 + "|" + uom1
                else:
                    empty_dict[name1] = value1
            i = i + 1
        list1.append(empty_dict)
    file_data['SPECS'] = list1
    column_list = ['row_id', 'Category Code', 'SPECS']

elif 'CATEGORY_CODE' in column_name and 'Attribute_Suggestion_1' in column_name:
    list1 = []
    for index, series in file_data.iterrows():
        i = 1
        empty_dict = {}
        while i < 51:
            name1 = str(series['ATTRIBUTE_NAME_' + str(i)])
            value1 = str(series['Attribute_Suggestion_' + str(i)])
            if name1 == 'nan':
                break
            if name1 != 'nan' and value1 != 'nan':
                empty_dict[name1] = value1
            i = i + 1
        list1.append(empty_dict)
    file_data['SPECS'] = list1
    column_list = ['row_id', 'CATEGORY_CODE', 'SPECS']

elif 'CATEGORY_CODE' in column_name and 'Attribute_Suggestion_1' not in column_name:
    list1 = []
    for index, series in file_data.iterrows():
        i = 1
        empty_dict = {}
        while i < 51:
            name1 = str(series['ATTRIBUTE_NAME_' + str(i)])
            value1 = str(series['ATTRIBUTE_VALUE_' + str(i)])
            uom1 = str(series['ATTRIBUTE_UOM_' + str(i)])
            if name1 == 'nan':
                break
            if name1 != 'nan' and value1 != 'nan':
                if uom1 != 'nan':
                    empty_dict[name1] = value1 + "|" + uom1
                else:
                    empty_dict[name1] = value1
            i = i + 1
        list1.append(empty_dict)
    file_data['SPECS'] = list1
    column_list = ['row_id', 'CATEGORY_CODE', 'SPECS']


file_data.to_csv('CleanTestData.csv', index=False, columns=column_list)