## function text_quality

"""

Created on 09 February, 2019


@author: Harjyot Kaur


Implementation of text_quality function in the PySyntext package.

"""

# load packages
import pandas as pd
import re
import string
import nltk.tag
from nltk import pos_tag
from nltk.corpus import stopwords



def load_words(path):
    
    """

    Loads words from a text file


    Parameters

    ----------

    path : str
        
        path of the text file


    Returns

    -------

    set

        A set of all words in the text file


    Examples
    --------
    >>> load_words('resources/words.txt')
    {Aar,
     Aara,
     Aarau,
    ....}
    """

    with open(path) as word_file:
        valid_words = set(word_file.read().lower().split())
        
    return valid_words



def clean(text):
    
    """

    Remove tickers, special characters, links and numerical strings


    Parameters

    ----------

    text : str
        
       User given input


    Returns

    -------

    str

        cleaned text


    Examples
    --------
    >>>text="RT $USD @Amila #Test\nTom\'s newly listed Co. &amp; Mary\'s unlisted Group to supply tech for nlTK.\nh.. $TSLA $AAPL https://  t.co/x34afsfQsh'"
    
    >>> clean(text)
    
    'RT  @Amila #Test\nTom's newly listed Co. &amp; Mary's unlisted Group to supply tech for nlTK.\nh..   https:// t.co/x34afsfQsh' 
    
    """
    # remove tickers
    remove_tickers=re.sub(r'\$\w*','',text)
    
    # remove new line symbol
    remove_newline=re.sub(r'\n','',remove_tickers)
    
    # remove links
    remove_links=re.sub(r'https?:\/\/.*\/\w*','',remove_newline)
    
    # remove special characters
    remove_punctuation=re.sub(r'['+string.punctuation+']+', ' ', remove_links)
    
    # remove numerical strings
    remove_numeric_words=re.sub(r'\b[0-9]+\b\s*', '',remove_punctuation)
    
    clean_text=remove_numeric_words
    
    return clean_text


def spell_check(word_list,text):
    
    """

    Check words spelt wrong (only for english)


    Parameters

    ----------
    word_list: set
        
        set of words in english dictionary
        
    text : str
        
       output string from function clean


    Returns

    -------

    list
    
        list of words spelt wrong
       
    int
        
        count of words spelt wrong
        
    double
    
        proportion of words spelt wrong in the entire text
    

    Examples
    --------
    >>> text="I thikn you should go for clas todat"
    >>> spell_check(eng_words,text)
    
    ({'clas', 'thikn', 'todat'}, 3, 0.08333333333333333)
    
    """
    # remove english words
    non_eng_words=set(text.split()).difference(word_list)
    
    if len(non_eng_words)!=0:
        # remove proper-nouns and prepositions
        tagged_sentence = nltk.tag.pos_tag(non_eng_words)

        tagged_non_nouns=list(filter(lambda tagged_sentence: tagged_sentence[1] != 'NNP' and 
                                tagged_sentence[1] != 'NNPS' and
                                 tagged_sentence[1] != 'PRP', tagged_sentence))

        removed_nouns=list(next(zip(*tagged_non_nouns)))

        # spelling errors
        spell_error=set(map(str.lower,removed_nouns)).difference(word_list)
        
        return {'spell_error': [spell_error], 
                'count_spell_error': len(spell_error), 
                'proportion_spell_error':len(spell_error)/len(text.split())}
    else:
        spell_error=set()
        
        return {'spell_error': [spell_error], 
                'count_spell_error': len(spell_error), 
                'proportion_spell_error':0.0}


def toxicity_check(word_list,text):
    
    """

    Check words that are profane


    Parameters

    ----------
    word_list: set
        
        set of words in english dictionary
        
    text : str
        
       output string from function pre-processing


    Returns

    -------

    list
    
        list of words that are profane
       
    int
        
        count of words that are profane
        
    double
    
        proportion of words that are profane in the entire text
    

    Examples
    --------
    >>> text="this is so shitty"
    >>> toxicity_check(toxic_words,text)
    
    ({'shitty'}, 1, 0.058823529411764705)
    
    """
    if len(text.split())!=0:
        toxic_words=set(text.split()).intersection(word_list)

        return {'toxic_words': [toxic_words], 
                'count_toxic_words': len(toxic_words), 
                'proportion_toxic_words':len(toxic_words)/len(text.split())}
    else:
        toxic_words=set()
        
        return {'toxic_words': [toxic_words], 
                'count_toxic_words': len(toxic_words), 
                'proportion_toxic_words': 0.0}
    
def text_quality(text):



    """

    Check quality of the string in terms of
    spelling errors and toxicity content.

    The function performs necessary cleaning
    on the input string.

    Comparison is done with pre-existing list of
    exhaustive english words to calculate the spelling errors in the string.
    Comparison is done with pre-existing list of
    exhaustive toxic-english words to calculate the toxicity in the string.


    Parameters

    ----------

    text : str

        input string ti be analyzed
        given by the user


    Returns

    -------

    dataframe

        First column contains proportion of spelling errors
        in the input contains and the second column stores
        toxicity in the the input string.


    Examples
    --------
    >>> text = "This str has words spelllll wrong.
    This string has a slag word shitty."
    >>> PySyntext.text_quality(text)

    # Example output, generate a dict then turn it into the output DataFrame
    quality = {

        'spell_error' : [0.15],

        'toxicity' :[0.08],

    }

    pd.DataFrame.from_dict(quality)
    """
    # load word sets
    eng_words=load_words('resources/words.txt')
    toxic_words = load_words('resources/en_profane_words.txt')
    
    # cleaning and calling spell_check,toxicity_check
    cleaned_text=clean(text)
    spelling_errors=spell_check(eng_words,cleaned_text)
    toxic_words=toxicity_check(toxic_words,cleaned_text)
  
    # compiling outputs
    quality = pd.DataFrame(dict(**spelling_errors,**toxic_words))

    return quality
