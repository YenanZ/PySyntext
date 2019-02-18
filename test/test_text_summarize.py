## test for text_summarize

import pytest
import pandas as pd
import os
import sys
import numpy
sys.path.insert(0, os.path.abspath(".."))
from PySyntext.text_summarize import text_summarize

ex_passage = "This is the first sentence in this paragraph. This is the second sentence. This is the third."

ex_output = {
    'word_count' : 6,
    'sentence_count' : 3,
    'most_common' : [['This']],
    'least_common' : [['first', 'paragraph', 'second', 'third']],
    'avg_word_len' : 6.833333,
    'avg_sentence_len' : 15.666667
}
ex_output = pd.DataFrame.from_dict(ex_output)

def test_normal_function(x):
    ex_output = text_summarize(x)
    assert ex_output.word_count[0] == 6
    assert ex_output.sentence_count[0] == 3
    assert ex_output.most_common[0] == ["sentence"]
    assert set(ex_output.least_common[0]) == {"first", "paragraph", "second", "third"}
    assert ex_output.avg_word_len[0], 2 == 6.83
    assert ex_output.avg_sentence_len[0], 2 == 15.66



def verify_output(x):
    ex_output = text_summarize(x)
    assert type(ex_output) == type(pd.DataFrame())
    assert type(ex_output.word_count[0]) == numpy.int64 and ex_output.word_count[0] >= 0
    assert type(ex_output.sentence_count[0]) == numpy.int64 and ex_output.word_count[0] >= 0
    assert type(ex_output.most_common[0]) == list and all(isinstance(n, str) for n in ex_output.most_common[0])
    assert type(ex_output.least_common[0]) == list and all(isinstance(n, str) for n in ex_output.least_common[0])
    assert type(ex_output.avg_word_len[0]) == numpy.float64 and ex_output.avg_word_len[0] >= 0
    assert type(ex_output.avg_sentence_len[0]) == numpy.float64 and ex_output.avg_sentence_len[0] >= 0



def verify_input():
    # Test if input is string
    test = 100
    with pytest.raises(ValueError) as e:
        text_summarize(test)
    assert str(e.value) == "Input must be a string"

def test_word_count():
    # Test if special characters counts as words
    test = "this + that"
    assert text_summarize(test).word_count[0] == 0
    # Test if punctuation counts as words
    test = "this , that, and ; the other thing!"
    assert text_summarize(test).word_count[0] == 1
    # Test if hyphens count as one or two words
    test = "compound-word"
    assert text_summarize(test).word_count[0] == 1
    # Test blank
    test = " "
    assert text_summarize(test).word_count[0] == 0
    # Test if numbers count as words
    test = "60 and 9 people in MDS"
    assert text_summarize(test).word_count[0] == 4



def test_sentence_count():
    # Test blank
    test = " "
    assert text_summarize(test).sentence_count[0] == 0
    # Test multiple periods "sentence..."
    test = "This is a sentence... This is sentence two. "
    assert text_summarize(test).sentence_count[0] == 2
    # Test if punctuation properly ends a sentence
    test = "Loudly! Question? Sentence three."
    assert text_summarize(test).sentence_count[0] == 3

def test_most_common():
    # Test multiple most common words (same case as no most common word)
    test = "most most most common common common"
    assert set(text_summarize(test).most_common[0]) == set(["most", "common"])
    # Test blank
    test = ""
    assert text_summarize(test).most_common[0] == []
    # Check if punctuation/special characters count
    test = "most most most common!!!!! + + + + + "
    assert text_summarize(test).most_common[0] == ['most']
    # Test if numbers count as words
    test = "10 10 10 people people"
    assert text_summarize(test).most_common[0] == ['10']

def test_least_common():
    # Test multiple least common words
    test = "no repeating words"
    assert set(text_summarize(test).least_common[0]) == set(["no", "repeating", "words"])
    # Test multiple least common words
    test = "repeating repeating words words"
    assert set(text_summarize(test).least_common[0]) == set(["repeating", "words"])
    # Test blank
    test = ""
    assert text_summarize(test).least_common[0] == []
    # Check if punctuation/special characters count
    test = "most most most common! +"
    assert text_summarize(test).least_common[0] == ['common']
    # Test if numbers count as words
    test = "10 people"
    assert text_summarize(test).least_common[0] == ['10', 'people']

def test_avg_word_len():
    # Test blank
    test = ""
    assert text_summarize(test).avg_word_len[0] == 0
    # Test if punctuation/special characters count
    test = "this + that!"
    assert text_summarize(test).avg_word_len[0] == 4
    # Test if numbers count as words
    test = "10 people"
    assert text_summarize(test).avg_word_len[0] == 6

def test_avg_sentence_len():
    # Test blank
    test = ""
    assert text_summarize(test).avg_sentence_len[0] == 0
    # Test if punctuation/special characters count
    test = "this + that! this and that? this and sometimes that."
    assert text_summarize(test).avg_sentence_len[0] == 3
