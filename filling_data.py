import pandas as pd


file_data1 = pd.read_csv('CleanTestData.csv')
file_data2 = pd.read_csv('TestData1.csv')
df_3 = pd.concat([file_data2, file_data1], axis=1, join='inner')

value_list = []
uom_list = []
for index, series in df_3.iterrows():
    i = 1
    value_dict = {}
    uom_dict = {}
    while i < 51:
        dict_data = eval(series['SPECS'])
        if series['Attribute Name ' + str(i)] in dict_data:
            if '|' not in dict_data[series['Attribute Name ' + str(i)]]:
                attribute_value = 'Attribute Value ' + str(i)
                attribute_uom = 'Attribute UOM ' + str(i)
                value_dict[attribute_value] = dict_data[series['Attribute Name ' + str(i)]]
                uom_dict[attribute_uom] = ""
            else:
                attribute_value = 'Attribute Value ' + str(i)
                attribute_uom = 'Attribute UOM ' + str(i)
                str_value = dict_data[series['Attribute Name ' + str(i)]].strip('[]')
                value = [str_value.split('|')[0].strip(' ')]
                uom = [str_value.split('|')[1].strip(' ')]
                value_dict[attribute_value] = value
                uom_dict[attribute_uom] = uom
        else:
            attribute_value = 'Attribute Value ' + str(i)
            attribute_uom = 'Attribute UOM ' + str(i)
            value_dict[attribute_value] = ""
            uom_dict[attribute_uom] = ""
        i = i + 1
    value_list.append(value_dict)
    uom_list.append((uom_dict))


def merge_list_of_dictionaries(dict_list):
    new_dict = {}
    for d in dict_list:
        for d_key in d:
            if d_key not in new_dict:
                new_dict[d_key] = []
            new_dict[d_key].append(d[d_key])
    return new_dict


dict_data_of_attribute_values = merge_list_of_dictionaries(value_list)
dict_data_of_attribute_uoms = merge_list_of_dictionaries(uom_list)

k = 1
for key1, key2 in zip(dict_data_of_attribute_values, dict_data_of_attribute_uoms):
    df_3['Attribute Value ' + str(k)] = dict_data_of_attribute_values[key1]
    df_3['Attribute UOM ' + str(k)] = dict_data_of_attribute_uoms[key2]
    k = k + 1
df_3.to_csv('filled_data.csv', index=False)
