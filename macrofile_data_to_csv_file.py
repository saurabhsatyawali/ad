import pandas as pd

df1 = pd.read_excel('files/Master Taxonomy_Attribution_20220908_Reference.xlsx')
df2 = pd.read_csv('files/input_1.csv')
category_namelist = []
values_list = []
i = 0
for index, series in df2.iterrows():

    if series['Category Code'] in list(df1['CODE']):
        cat_name = df1['CATEGORY_NAME'][i]
        values = df1['VALUES'][i]

        category_namelist.append(cat_name)
        values_list.append(values)
    else:

        cat_name = ""
        category_namelist.append(cat_name)
        values = ""
        values_list.append(values)

    i = i + 1

df2['CATEGORY_NAME'] = category_namelist
attribue_name_list = []

for attribute_names in values_list:
    split_list = attribute_names.split('|')
    j = 1
    k = 0
    attribue_name_dict = {}
    while j < 51:
        if k < len(split_list):
            attribue_name_dict['ATTRIBUTE_NAME_' + str(j)] = split_list[k]
        else:
            attribue_name_dict['ATTRIBUTE_NAME_' + str(j)] = ""

        j = j + 1
        k = k + 1

    attribue_name_list.append(attribue_name_dict)



def merge_list_of_dictionaries(dict_list):
    new_dict = {}
    for d in dict_list:
        for d_key in d:
            if d_key not in new_dict:
                new_dict[d_key] = []
            new_dict[d_key].append(d[d_key])
    return new_dict


attribue_name_dict_data = merge_list_of_dictionaries(attribue_name_list)

for seq, key in zip(range(1, 51), attribue_name_dict_data):
    df2['ATTRIBUTE_NAME_' + str(seq)] = attribue_name_dict_data[key]
    df2['ATTRIBUTE_VALUE_' + str(seq)] = ""
    df2['ATTRIBUTE_UOM_' + str(seq)] = ""
    df2['Attribute_Suggestion_' + str(seq)] = ""
df2.to_csv('files/output.csv', index=False)
