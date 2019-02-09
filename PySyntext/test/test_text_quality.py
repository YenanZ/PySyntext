## test for text_quality

"""

Created on February, 2019



@author: Harjyot Kaur


This script tests the text_quality function of the PySyntext package.



text_quality function of the PySyntext package, checks the 
quality of the string in terms of spelling errors and toxicity content.
It takes in a string as input and returns a dataframe.
    
The function performs necessary cleaning 
on the input string. 

"""

import pytest
import pandas as pd
import numpy as np
from PySyntext.text_quality import text_quality



# sample input
x = "This str has words spelllll wrong. This string has a slag word shitty."

# sample output
df = pd.DataFrame(columns=['spell_error','toxicity'])
df  = df.append([{"spell_error": 0.15,"toxicity": 0.08}])




def test_output_type():
    
    """
    Test that output is of type list
    """

    assert(type(text_quality(string=x)) == type(pd.DataFrame()))

    
def test_output_float():

    """
    Test that output contains floats only
    """

    output = text_quality(string=x)
    
    assert isinstance(output.spell_error[0], numpy.float64) | isinstance(output.spell_error[0], float)
    assert isinstance(output.toxicity[0], numpy.float64) | isinstance(output.spell_error[0], float)


def test_output_positive():

    """
    Test that output contains non-negative floats
    (since the spelling errors and toxicity by definition of
    this function cannot be negative)

    """

    output = text_quality(string=x)
    
    assert output.spell_error[0]>=0
    assert output.toxicity[0]>=0


def test_input_data_type1():

    """
    Test for error if input type is not a string
    """

    try:
        text_quality(string=123)

    except:
        assert True

    else:
        assert False



def test_input_data_type2():

    """
    Test for error if input string is empty
    """
    
    try:
        text_quality(string="")

    except:
        assert True

    else:
        assert False



def test_input_data_type3():

    """
    Test for error if input string has only punctuations
    """

    try:
        text_quality(string="\!@#$%^&*{}{{{{}}}}")

    except:
        assert True

    else:
        assert False
        

def test_output_spell_error():

    """
    Test that spell error gives expected output
    """

    output = text_quality(string=x)
    
    assert output.spell_error[0]>=0.14 and output.spell_error[0]<=0.16
    

def test_output_toxicity():

    """
    Test that toxicity gives expected output
    """

    output = text_quality(string=x)
    
    assert output.toxicity[0]>=0.06 and output.toxicity[0]<=0.09