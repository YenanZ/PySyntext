## function text_summarize, as part of PySyntext

def text_summarize(passage):

    """
    Returns various summary information of a string.

    This function returns a DataFrame with total word count,
    total sentence count, most common and least common word, average
    word length, and average sentence length. Each information resides
    in a separate column.

    Parameters
    ----------
    passage : String
        The string to be analyzed.
    stopwords_remove : Boolean
        Remove common stop words (ex. 'and', 'the', 'him') from `passage`.
    lemmatize : Boolean
        If True, lemmatize every word in `passage`.
        More info for how lemmatize works can be found in NLTK docs.
    remove_punctuation : Boolean
        If True, strip `passage` of punctuation.
    remove_numbers : Boolean
        If True, strip `passage` of numbers.
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
    >>> ex_passage = "This is the first sentence in this paragraph. \
                      This is the second sentence. This is the third."
    >>> PySyntext.text_summarize(ex_passage)

    # Example output, generate a dict then turn it into the output DataFrame
    answer = {
        'word_count' : 17,
        'sentence_count' : 3,
        'most_common' : 'This',
        'least_common' : [['first', 'in', 'second', 'third']],
        'avg_word_len' : 4.35,
        'avg_sentence_len' : 5.67
    }
    pd.DataFrame.from_dict(answer)
    """

    summary = pd.DataFrame()
    return summary
