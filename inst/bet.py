import math
import numpy as np
import pandas as pd
from scipy import stats
from tqdm import tqdm
import warnings
warnings.filterwarnings('ignore')


def create_bet(df):

    """ BET function constructs the Basic Element Table for the Dataframe. BET is the key step for ARTML and
    it can be updated with the new data.
    BET function returns basic element table as Pandas Dataframe
    Notes:
    -----
    see 'Real Time Data Mining' by Prof. Sayad
    (https://www.researchgate.net/publication/265619432_Real_Time_Data_Mining)
    """
    col = df.columns.tolist()
    df_matrix = df.values
    l = len(col)

    idx = np.array([5,6,7,8,9,0,1,2,3,4,10,11])
    bet={}
    x = np.array([[np.zeros(12) for x in range(l)] for y in range(l)])
    for i in tqdm(range(l)):
        bet[i] = []

        for j in range(i,l):
            y= np.array(df_matrix[:,j])
            z= np.array(df_matrix[:,i])

            """
            This code makes calculations for all the basic elements in the table. They are appended to
            a lists of a dictionary.
            """
            
            x[i,j] = np.array([len(z), z.sum(), (z**2).sum(), (z**3).sum(), (z**4).sum(), 
                               len(y), y.sum(), (y**2).sum(), (y**3).sum(), (y**4).sum(), (z*y).sum(), ((z*y)**2).sum()])

            x[j,i] = x[i,j][idx]
      
        for j in range(l): 
           bet[i].append(x[j,i])

    result = pd.DataFrame(bet, index=col)
    result.columns = col
    return(result)