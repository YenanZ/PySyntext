## function text_summarize, as part of PySyntext

import pandas as pd
import re 
import nltk
nltk.download('punkt')
from nltk.tokenize import sent_tokenize
from collections import Counter

def text_summarize(passage):

    """
    Returns various summary information of a string.

    This function returns a DataFrame with total word count,
    total sentence count, most common and least common word, average
    word length, and average sentence length. Each information resides
    in a separate column.

    Parameters
    ----------
    text : String
        The string to be analyzed.
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
            The total number of words in `text`.
        sentence_count : Int
            the total number of sentences in `text`.
        most_common : List of String
            A list of the most common words in `text`. If this returns a
            list of length 1, there is only one most common word. If this
            returns a list of length > 1, there are multiple words that appear
            the most number of times in `text`.
        least_common : List of String
            A list of the least common words in `text`. If this returns a
            list of length 1, there is only one least common word. If this
            returns a list of length > 1, there are multiple words that appear
            the least number of times in `text`.
        avg_word_len : float
            The average word length in `text`.
        avg_sentence_len : float
            The average number of words in a sentence, in `text`.

    Examples
    --------
    >>> ex_passage = "This is the first sentence in this paragraph. \
                      This is the second sentence. This is the third."
    >>> PySyntext.text_summarize(ex_passage)

    # Example output, generate a dict then turn it into the output DataFrame
    answer = {
        'word_count' : 17,
        'sentence_count' : 3,
        'most_common' : [['This']],
        'least_common' : [['first', 'in', 'second', 'third']],
        'avg_word_len' : 4.35,
        'avg_sentence_len' : 5.67
    }
    pd.DataFrame.from_dict(answer)
    """
    
    split_passage=passage.split()
    
    # word count
    word_count=len(split_passage)
    
    # count number of sentences
    
    # method 1
    # sentence_count=len(re.findall(r'\.', passage )
    # method 2
    sentence_count= len(sent_tokenize(passage))
    
    # most common words
    counter = Counter(split_passage) 
    most_common = counter.most_common(1)[0][0]
    
    # least common 
    # please help 
    
    # average word length
    avg_word_len= sum(len(word) for word in split_passage) / len(split_passage)
    
    # average sentence length
    # please help 
    
    
    # I'm having some trouble making this into a dataframe, I'm returning a list for now
    keys = ['word_count', 'sentence_count', 'most_common', 'least_common', 'avg_word_len', 'avg_sentence_len']
    summary = {key: [None] for key in keys}
    summary = pd.DataFrame.from_dict(summary)
    
    # return list 
    return [word_count, sentence_count,most_common, avg_word_len]


# you can see the output

ex_passage = "This is the first sentence in this paragraph. \
                      This is the second sentence. This is the third."
text_summarize(ex_passage)