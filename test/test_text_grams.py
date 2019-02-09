## test for TextGrams

import pytest
import pandas as pd
import os
import sys
import numpy
sys.path.insert(0, os.path.abspath(".."))
from PySyntext.text_grams import text_ngrams

# sample input
x = "Today is a sunny day. We should go to a beach on this sunny day"

# sample output
df = {
    'bigrams' : [['sunny','day']],
}
ex_output = pd.DataFrame.from_dict(df)
k=1
n=2

# test for functionality
def test_normal_function(x):
    ex_output = text_grams(x)
    assert ex_output.bigrams[0] ==  [["sunny","day"]]



# test datatype inside output dataframe
def verify_output(x):
    ex_output = text_grams(x)
    assert type(ex_output) == type(pd.DataFrame())
    assert type(ex_output.bigrams[0]) == list and and all(isinstance(n, str) for n in ex_output.bigrams[0])
    
    
# test output matches arguments passed
def verify_output_and_arguments(x):
    ex_output = text_grams(x)
    assert  len(ex_output.bigrams[0])==k
    assert  len(ex_output)==n


# test datatype inside output dataframe
def verify_output(x):
    ex_output = text_grams(x)
    assert type(ex_output) == type(pd.DataFrame())
    assert type(ex_output.bigrams[0]) == list and and all(isinstance(n, str) for n in ex_output.bigrams[0])
    


# test to verify if function raises for invalid input
def verify_input1():

    """
    Test if input string is valid (not numeric)
    """

    text = 100

    with pytest.raises(ValueError) as e:

        text_grams(text)

    assert str(e.value) == "Input must be a string"


# test to verify if function raises for invalid input
def verify_input2():

    """
    Test if input is not empty
    """

    text = " "

    with pytest.raises(ValueError) as e:

        text_grams(text)

    assert str(e.value) == "Input must be a string"

    
# test to verify if function raises for invalid input
def verify_input3():

     """
     Test if input string is valid (not special characters)
     """

    text = "!#$*()&^%$#@!{}{{{}}}"

    with pytest.raises(ValueError) as e:

        text_grams(text)

    assert str(e.value) == "Input has no text"





    

    
