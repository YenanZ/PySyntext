## function TextGrams

"""

Created on 09 February, 2019


@author: Harjyot Kaur
         Yenan Zhang


Implementation of text_grams function

"""

# load packages
import pandas as pd


def text_grams(text, k, n, stop_remove, lemitize, remove_punctuation,remove_number,case_sensitive,gibberish_remove):



    """
    Returns top k ngrams of the text

    Parameters
    ----------
    text : String
        The string to be analyzed.
        
    k : int
        top ngrams reguired
        
    n:  list
        number of combination of words with highest frequency
        
    stopwords_remove : Boolean
        Remove common stop words (ex. 'and', 'the', 'him') from `text`.
        
    lemmatize : Boolean
        If True, lemmatize every word in `text`.
        More info for how lemmatize works can be found in NLTK docs.
        
    remove_punctuation : Boolean
        If True, strip `text` of punctuation.
        
    remove_numbers : Boolean
        If True, strip `text` of numbers.
        
    case_sensitive : Boolean
        If True, text_summarize will be case sensitive (ex. "this" and
        "This" will be two separate words).
        
    gibberish_remove : Boolean
        Remove words that are not actually words in the English language
        (ex. any spelling mistakes, slang).

    Returns
    -------
    DataFrame
        word_count : Int
            The total number of words in `passage`.
        sentence_count : Int
            the total number of sentences in `passage`.
        most_common : List of String
            A list of the most common words in `passage`. If this returns a
            list of length 1, there is only one most common word. If this
            returns a list of length > 1, there are multiple words that appear
            the most number of times in `passage`.
        least_common : List of String
            A list of the least common words in `passage`. If this returns a
            list of length 1, there is only one least common word. If this
            returns a list of length > 1, there are multiple words that appear
            the least number of times in `passage`.
        avg_word_len : float
            The average word length in `passage`.
        avg_sentence_len : float
            The average number of words in a sentence, in `passage`.

    Examples
    --------
    >>> text = "It is a sunny day outside. We should go to a beach on this sunny day."
    >>> PySyntext.text_grams(text,1,(2))

    # Output
    bigrams
    [["sunny","day"]]
    """
    
    return ngrams
    

