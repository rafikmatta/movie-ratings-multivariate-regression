from pandas import DataFrame, read_csv
import pandas as pd
import numpy as np

def split_mean_square_error(list_of_splits):
    result = 0
    Nm = 0
    num_of_splits = len(list_of_splits)

    # Nm is the values at all the node
    for i in range(0, num_of_splits):
        Nm = Nm + list_of_splits[i].shape[i]

    for i in range(0, num_of_splits):
        x = list_of_splits[i]
        gmj = sum(x)['rating'] / x.shape[0]
        index_list = x.index.tolist()
        for j in index_list:
            rt = x['rating'][j]
            difference = (rt - gmj) ** 2
            result = result + difference

    final_result = (1 / Nm) * result
    return (final_result)

def split_attribute(x):
    min_mse = 1000000000000000
    best_feature = 0
    number_of_attributes = len(list(x))
    size_of_x = x.shape[0]
    attributes = list(x)
    attribute_types = x.dtypes
    for i in range(0,number_of_attributes-1):
        #if categorical
        if attribute_types[i] == 'str':
            print("Categorical")
        #else is numeric
        else:
            x = x.sort_values(by=attributes[i])
            index_list = x.index.tolist()
            for j in range(0,size_of_x-2):
                x1 = x[0:(j+1)]
                x2 = x[(j+2):size_of_x]
                split_mse_val = split_mean_square_error([x1,x2])
                if(split_mse_val<=min_mse):
                    min_mse = split_mse_val
                    best_feature = attributes[i]
                    split_threshold_row = x['rating'][index_list[j]]
    return(best_feature,split_threshold_row)

d = {'col1': [1,2,3,4,5,6], 'rating': [1,2,3,4,5,6]}
df = pd.DataFrame(data=d)
split_attribute(df[4:6])