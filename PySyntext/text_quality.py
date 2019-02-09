## function text_quality

"""

Created on 08 February, 2019


@author: Harjyot Kaur


Implementation of text_quality function in the PySyntext package.

"""

# load packages
import pandas as pd


def text_quality(string):



    """
    
    Check quality of the string in terms of
    spelling errors and toxicity content. 
    
    The function performs necessary cleaning 
    on the input string. 
    
    Comparison is done with pre-existing list of
    exhaustive english words to calculate the spelling errors in the string.
    Comparison is done with pre-existing list of
    exhaustive toxic-english words to calculate the toxicity in the string.
    
   
    Parameters

    ----------

    string : str

        input string ti be analyzed
        given by the user


    Returns

    -------

    dataframe

        First column contains proportion of spelling errors 
        in the input contains and the second column stores 
        toxicity in the the input string.

    """



    output = pd.DataFrame()

    return output
