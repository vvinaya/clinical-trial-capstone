import pandas as pd

def load_data(filename):
    return pd.read_csv(filename)

def clean_data(input_df):
    # ADD ANY OTHER DATA CLEANING TASKS TO THIS METHOD
    
    input_df.drug_names = input_df.drug_names.fillna('Not specified')
    
def bools_to_int64(input_df):
    bool_cols = [key for key in dict(input_df.dtypes) if dict(input_df.dtypes)[key] == 'bool']
    input_df[bool_cols] = (input_df[bool_cols]).astype('int64')
    
def retrieve_unique_treatments(input_df):
    drug_list = []
    for group in input_df.drug_names.values:
        for drug in group.split(', '): drug_list.append(drug)
    
    # TODO: REMOVE DUPLICATE TREATMENTS DUE TO SPELLING/HYPHENS
    
    return list(set(drug_list))

if __name__ == '__main__':
    
    decision_df = load_data('data/chemo_decisions.csv')
    clean_data(decision_df)
    unique_treatments = retrieve_unique_treatments(decision_df)
    print(unique_treatments)