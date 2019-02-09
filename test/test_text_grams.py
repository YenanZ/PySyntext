## test for TextGrams

import pytest
import pandas as pd
import os
import sys
import numpy
sys.path.insert(0, os.path.abspath(".."))
from PySyntext.text_grams import text_ngrams

ex_passage = "Today is a beautiful day which is perfect for going to the beach, the weather is nice and the sky is blue."

def test_output(x):
    ex_output=text_grams(x)
    assert type(ex_output) == type(pd.DataFrame())
    assert type(ex_output[,1])==type(list())
    

    
