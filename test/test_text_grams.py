## test for TextGrams

import pytest
import pandas as pd
import os
import sys
import numpy
sys.path.insert(0, os.path.abspath(".."))
from PySyntext.text_grams import text_grams

# sample input
x = "Today is a sunny day. We should go to a beach on this sunny day"

# sample output
grams = {
    '2gram' : [("sunny", "day")],
    'Number of Instances' : 2,
}
sample_out = pd.DataFrame.from_dict(grams)
k=1
n=[2]

ex = "short sentence. short sentence."
ex_output = text_grams(ex, k=0)
ex_output

# test for functionality
def test_normal_function(x, k, n):
    x = "Today is a sunny day. We should go to a beach on this sunny day"
    k=1
    n=[2]
    ex_output = text_grams(x, k, n)
    assert ex_output["2gram"][0] ==  sample_out['2gram'][0]
    assert  len(ex_output['2gram'][0]) == n[0]
    assert  ex_output.shape[0] == sample_out.shape[0]
#test_normal_function(x, k, n)

# test datatype inside output dataframe
def verify_output(x, k, n):
    x = "Today is a sunny day. We should go to a beach on this sunny day"
    k=1
    n=[2]
    ex_output = text_grams(x, k, n)
    assert type(ex_output) == type(sample_out)
    assert type(ex_output['2gram'][0]) == tuple
    assert type(ex_output['Number of Instances'][0]) == numpy.int64
    
#verify_output(x, k, n)

# test sentence endings (?, !, .)
def verify_sentence_endings():
    ex = "Wherefore art thou Romeo! Wherefore art thou Romeo. Wherefore art thou Romeo?"
    ex_output = text_grams(ex)
    assert ex_output.shape[0] != 4 # If it split sentences properly, (Romeo, Wherefore) will not be a gram combination
#verify_sentence_endings()

# test stop remove
def verify_stop_remove():
    ex = "This is a sentence. This is also a sentence. This is also a sentence."
    ex_output = text_grams(ex, stop_remove = False)
    assert ex_output.shape[0] > 1 # If stopwords are removed, only (also, sentence) will be considered
#verify_stop_remove()

# test punctuation
def verify_remove_punctuation():
    ex = "This is / a sentence. This is / also a sentence. This is / also a sentence."
    ex_output = text_grams(ex, remove_punctuation = False)
    assert ex_output.shape[0] > 1 # If punctuation is removed, only (also, sentence) will be considered
#verify_remove_punctuation()

# test remove number
def verify_remove_number():
    ex = "This is 123 a sentence. This is 123 also a sentence. This is 123 also a sentence."
    ex_output = text_grams(ex, remove_number = False)
    assert ex_output.shape[0] > 1 # If numbers is removed, only (also, sentence) will be considered
#verify_remove_number()

# test case sensitive
def verify_case_sensitive():
    ex = "Hey Guys. Hey Guys. hey guys. hey guys."
    ex_output = text_grams(ex, case_sensitive = True)
    assert ex_output.shape[0] > 1 # If case_sensitive is true, only (hey, guys) will be considered
#verify_case_sensitive()


# test invalid values of k
def verify_k():
    ex = "Wherefore art thou Romeo! Wherefore art thou Romeo. Wherefore art thou Romeo?"
    ex_output1 = text_grams(ex, k = 0)    
    assert ex_output1.shape[0] == 0 # If k is 0, dataframe should be empty

    with pytest.raises(ValueError) as e:
        text_grams(ex, k = -1)
    assert str(e.value) == "k must be 0 or greater"
#verify_k()

# test invalid values of n
def verify_n():
    ex = "Wherefore art thou Romeo! Wherefore art thou Romeo. Wherefore art thou Romeo?"  
    with pytest.raises(ValueError) as e:
        text_grams(ex, n = [])  
    assert str(e.value) == "n must have at least one positive value"

    with pytest.raises(ValueError) as e:
        text_grams(ex, n = [-1])
    assert str(e.value) == "Values of n must be greater than 0"
#verify_n()

# test if sentence length is smaller than n
def verify_n_larger_than_sentence():
    ex = "short sentence. short sentence."
    ex_output = text_grams(ex, n = [3])
    assert ex_output.shape[0] == 0 # If n is larger than sentence length, dataframe should be empty
#verify_n_larger_than_sentence()

# test to verify if function raises for invalid input
def verify_input1():
    """
    Test if input string is valid (not numeric)
    """

    text = 100
    
    with pytest.raises(ValueError) as e:
        text_grams(text)
    assert str(e.value) == "Input must be a string"
#verify_input1()

# test to verify if function raises for invalid input
def verify_input2():

    """
    Test if input is not empty
    """

    text = " "

    with pytest.raises(ValueError) as e:
        text_grams(text)
    assert str(e.value) == "Input text is empty."
#verify_input2()