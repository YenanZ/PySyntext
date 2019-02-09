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
df = pd.DataFrame(columns=['spell_error','toxicity'])
df  = df.append([{"spell_error": 0.15,"toxicity": 0.08}])




def test_output_type():

    """
    Test that output is of type DataFrame
    """

    assert(type(text_quality(text=x)) == type(pd.DataFrame()))


def test_output_float():

    """
    Test that output contains floats
    """

    output = text_quality(text=x)

    assert isinstance(output.spell_error[0], numpy.float64) | isinstance(output.spell_error[0], float)
    assert isinstance(output.toxicity[0], numpy.float64) | isinstance(output.spell_error[0], float)


def test_output_positive():

    """
    Test that output contains non-negatives
    (since the spelling errors and toxicity by definition of
    this function cannot be negative)
    """

    output = text_quality(text=x)

    assert output.spell_error[0]>=0
    assert output.toxicity[0]>=0




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


def verify_input3():

     """
     Test if input string is valid (not special characters)
     """

    text = "!#$*()&^%$#@!{}{{{}}}"

    with pytest.raises(ValueError) as e:

        text_quality(text)

    assert str(e.value) == "Input has no text"



def test_output_spell_error():

    """
    Test that spell error gives expected output
    """

    output = text_quality(text=x)

    assert output.spell_error[0]>=0.14 and output.spell_error[0]<=0.16


def test_output_toxicity():

    """
    Test that toxicity gives expected output
    """

    output = text_quality(text=x)

    assert output.toxicity[0]>=0.06 and output.toxicity[0]<=0.09
