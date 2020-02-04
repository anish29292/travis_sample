import pandas as pd
import numpy as np

def create_empty_dataframe(new_column_list, num_rows):
   """
   Creates a new dataframe filled with zeroes from a specified
   list and number of rows.
    Args:
        new_col_list (object): List of column names.
        num_rows (int): Number of rows you want the new table to have.
    Returns:
        df: returns a pandas dataframe with specific column
            names and number of rows.
   """
   col_list = new_column_list
   num_cols = len(new_column_list)
   fill_with_zeroes = np.zeros(shape=(num_rows, num_cols))
   new_df = pd.DataFrame(fill_with_zeroes, columns=[col_list])

   return new_df
