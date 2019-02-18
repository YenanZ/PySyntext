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
import numpy
import pandas as pd
import sys
import os
sys.path.insert(0, os.path.abspath(".."))
from PySyntext.text_quality import text_quality



# sample input
x = "This str has words spelllll wrong. This string has a slag word shitty."

# sample output
df = pd.DataFrame({'spell_error': [{'spelllll'}],
                   'count_spell_error': 1,
                   'proportion_spell_error': 0.07692307692307693,
                   'toxic_words': [{'shitty'}],
                   'count_toxic_words': 1,
                   'proportion_toxic_words': 0.07692307692307693})



def test_output_type():

    """
    Test that output is of type DataFrame
    """

    assert(type(text_quality(text=x)) == type(pd.DataFrame()))



def verify_input1():

    """
    Test if input string is valid (not numeric)
    """

    text = 100

    with pytest.raises(ValueError) as e:

        text_quality(text)

    assert str(e.value) == "Input must be a string"



def verify_input2():

    """
    Test if input is not empty
    """

    text = " "

    with pytest.raises(ValueError) as e:

        text_quality(text)

    assert str(e.value) == "Input must be a string"

