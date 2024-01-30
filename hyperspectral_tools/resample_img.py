# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/resample.ipynb.

# %% auto 0
__all__ = ['Resample']

# %% ../nbs/resample.ipynb 3
import numpy as np
import pandas as pd
from spectral import *

# %% ../nbs/resample.ipynb 4
class Resample():

  def __init__(self,
               path_to_spectrum : str , #Path to a CSV file containing spectral bands as float values stored as strings. Ensure that only columns with spectral data have digit-only names strings.

               ):
          
          #read the dataframe
          init_df = pd.read_csv(path_to_spectrum)
          # filter to get only spectral data and change columns type to numeric
          df = init_df.loc[:, init_df.columns[init_df.columns.str.isdigit()]]
          df.columns=pd.to_numeric(df.columns)
          self.df = df
          #save the non spectral data
          self.non_spectral_data =init_df.loc[:, init_df.columns[~init_df.columns.str.isdigit()]]

  

  
