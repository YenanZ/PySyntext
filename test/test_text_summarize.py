## test for text_summarize

import pytest
import pandas as pd

ex_passage = "This is the first sentence in this paragraph. This is the second sentence. This is the third."

def test_normal_function(x):
    out = text_summarize(x)
    assert out.word_count[0] == 17
    assert out.sentence_count[0] == 3
    assert out.most_common[0] == "This"
    assert set(out.least_common[0]) == set(["first", "in", "second", "third"])
    assert round(out.avg_word_len[0], 2) == 4.35
    assert round(out.avg_sentence_len[0], 2) == 5.67

test_normal_function(ex_passage)

def verify_output(x):
    out = text_summarize(x)
    assert type(out) == type(pd.DataFrame())
    assert type(out.word_count[0]) == int and out.word_count[0] >= 0
    assert type(out.sentence_count[0]) == int and out.word_count[0] >= 0
    assert type(out.most_common[0]) == list and all(isinstance(n, str) for n in most_common[0])
    assert type(out.least_common) == list and all(isinstance(n, str) for n in least_common[0])
    assert type(out.avg_word_len[0]) == float and out.avg_word_len[0] >= 0
    assert type(out.avg_sentence_len[0]) == float and out.avg_sentence_len[0] >= 0

verify_output(ex_passage)

def verify_input():
    # Test if input is string
    test = 100
    with pytest.raises(ValueError) as e:
        text_summarize(test)
    assert str(e.value) == "Input must be a string"

def divide(a, b):
    if b == 0:
        raise ValueError('Cannot divide by Zero')
    return a / b

def test_zero_division():
    with pytest.raises(ValueError) as e:
        divide(1, 0)
    assert str(e.value) == 'Cannot divide by Zero'

def test_word_count():
    # Test if special characters counts as words
    test = "this + that"
    assert text_summarize(test).word_count[0] == 3
    # Test if punctuation counts as words
    test = "this , that, and ; the other thing!"
    assert text_summarize(test).word_count[0] == 6
    # Test if hyphens count as one or two words
    test = "compound-word"
    assert text_summarize(test).word_count[0] == 1
    # Test blank
    test = " "
    assert text_summarize(test).word_count[0] == 0
    # Test if numbers count as words
    test = "60 and 9 people in MDS"
    assert text_summarize(test).word_count[0] == 6

def test_sentence_count():
    # Test blank
    test = " "
    assert text_summarize(test).sentence_count[0] == 6
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
    assert text_summarize(test).avg_word_len[0] == ['10']

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
    assert text_summarize(test).avg_word_len[0] == 4

def test_avg_sentence_len():
    # Test blank
    test = ""
    assert text_summarize(test).avg_sentence_len[0] == 0
    # Test if punctuation/special characters count
    test = "this + that! this and that? this and sometimes that."
    assert text_summarize(test).avg_sentence_len[0] == 3
    # Test if numbers count as words
    test = "10 people. 20 people. 30 people. "
    assert text_summarize(test).avg_word_len[0] == 2
