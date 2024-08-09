# utils.py

import pandas as pd

def adjust_item_costs(df):
    """
    Adjusts the cost of items based on the number of people sharing the item.
    """
    def adjust_cost(row):
        count = row[['nick', 'kevin', 'andy']].notna().sum()
        if count == 3:
            return row['Cost'] / 3
        elif count == 2:
            return row['Cost'] / 2
        else:
            return row['Cost']

    df['Adjusted Cost'] = df.apply(adjust_cost, axis=1)
    return df

def calculate_total_costs(df):
    """
    Calculates the total cost for each person.
    """
    total_costs = {
        'nick': 0,
        'kevin': 0,
        'andy': 0
    }

    for _, row in df.iterrows():
        if pd.notna(row['nick']):
            total_costs['nick'] += row['Adjusted Cost']
        if pd.notna(row['kevin']):
            total_costs['kevin'] += row['Adjusted Cost']
        if pd.notna(row['andy']):
            total_costs['andy'] += row['Adjusted Cost']

    return total_costs

def save_to_excel(df, file_path):
    """
    Saves the DataFrame to an Excel file.
    """
    df.to_excel(file_path, index=False)
