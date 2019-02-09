## function text_quality

"""

Created on 09 February, 2019


@author: Harjyot Kaur


Implementation of text_quality function in the PySyntext package.

"""

# load packages
import pandas as pd


def text_quality(string):



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

    """

    Examples
    --------
    >>> text = """This str has words spelllll wrong.
    This string has a slag word shitty."""
    >>> PySyntext.text_quality(text)

    # Example output, generate a dict then turn it into the output DataFrame
    quality = {

        'spell_error' : [0.15],

        'toxicity' :[0.08],

    }

    pd.DataFrame.from_dict(quality)
    """


    quality = pd.DataFrame()

    return quality
