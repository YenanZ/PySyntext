## function TextGrams

"""

Created on 09 February, 2019


@author: Harjyot Kaur
         Yenan Zhang


Implementation of text_grams function

"""

# load packages
import pandas as pd
import string
import re
from nltk.corpus import stopwords
import collections as collect
#nltk.download("stopwords")
#nltk.download('averaged_perceptron_tagger')

def load_words(path):
    with open(path) as word_file:
        valid_words = set(word_file.read().split())
       
    return valid_words

def clean(text, remove_punctuation = True, remove_number = True):
    
    punct_wo_endings = string.punctuation.replace('.', '').replace('!', '').replace('?', '')
    
    remove_tickers=re.sub(r'\$\w*','',text)
    remove_newline=re.sub(r'\n','',remove_tickers)
    remove_links=re.sub(r'https?:\/\/.*\/\w*','',remove_newline)
    if remove_punctuation:
        remove_punctuation=remove_links.translate({ord(char): None for char in punct_wo_endings})
    else:
        remove_punctuation = remove_links
    if remove_number: 
        remove_numeric_words=re.sub(r'\b[0-9]+\b\s*', '',remove_punctuation)
    else:
        remove_numeric_words = remove_punctuation
    
    clean_text=remove_numeric_words
    
    return clean_text

def pre_processing(text, case_sensitive = False, stop_remove = True):
    
    if not case_sensitive:
        text = text.lower()
    if stop_remove:
        pattern = re.compile(r'\b(' + r'|'.join(stopwords.words('english')) + r')\b\s*')
    text = pattern.sub('', text)

    return text


def text_grams(text, k = 5, n = [2, 3], stop_remove = True, lemitize = False, remove_punctuation = True, \
               remove_number = True, case_sensitive = False):
    
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
    
    eng_words = load_words('words.txt')
    ngrams_list = []
    ngrams_dfs = []
    lbls = [str(num_grams) + "gram" for num_grams in n]

    clean_text = clean(text, remove_punctuation, remove_number)
    clean_text = pre_processing(clean_text, case_sensitive, stop_remove)
    
    split_sentences = list(filter(None, re.split("[,.!?:]+", clean_text)))
    #print(split_sentences)
    
    for num_grams in n:
        ngrams = collect.Counter()
        
        for sentence in split_sentences: 
            #print(sentence)
            split_words = sentence.split()
            #print(split_words)        
            list_of_grams = [split_words[i:i + num_grams] for i in range(len(split_words) - num_grams + 1)]
            #print(list_of_grams)
            
            ngrams.update([tuple(item) for item in list_of_grams])
            
        ngrams_list.append(ngrams.most_common(k))

    for list_of_top_grams in ngrams_list: 
        ngrams_dfs.append(pd.DataFrame.from_records([list(i) for i in list_of_top_grams], columns = [lbls[0], "Number of Instances"]))
        lbls.pop(0)
    
    for i in range(len(ngrams_dfs)-1):
        final_df = pd.concat([ngrams_dfs[0].reset_index(drop = True), ngrams_dfs[i+1]], axis = 1)
    

    return final_df

