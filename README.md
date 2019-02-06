# TextSummarizer
A python package to summarize text columns in a dataframe. 

Team Members

|Name | Github |
|---|---|
| Harjyot Kaur |  |
| Alexander Pak | pak-alex |
| Yenan Zhang |  |


### Summary

There are many packages that cover summary statistics for numerical data. However, when it comes to text data, there is a lack of selection for packages of similar functionality. Our group would like to tackle this problem by creating `textPy`. This package will allow users to input passages and receive summary information and sentiment analysis on the text, giving the user valuable information on how best to proceed with their data. 

Sample functionality included in this package for a given text passage:

* Most common word
* Most frequent n-gram
* Sentiment (Positive, Negative, Neutral)
* Number of spelling mistakes
* ...etc. 

#### Function 1: textsummarize

|Input| Output|
|---|---|
| Dataframe | Dataframe |
| List | Lists |


#### Function 2: textavg

|Input| Output|
|---|---|
| Dataframe | Dataframe |
| List | Float |

#### Function 3: textngrams

|Input| Output|
|---|---|
| Dataframe | Dataframe |
| List | Dictionary |

### Python Ecosystem

There are several popular Natural Language Processing packages that exist in the Python landscape. [NLTK](https://www.nltk.org/) and [spaCy](https://spacy.io/) are the most popular packages for dedicated natural language processing. [sci-kit learn](https://scikit-learn.org/stable/), another popular machine learning package, provides the framework for general machine learning models, and includes functions for text analysis. 

Although these packages provide the framework for tokenizing and fitting models to text data, it is difficult to create a quick-and-dirty summary of your data using these packages. By using textPy, summary and sentiment of text data is quickly achievable, allowing users to determine the worth of their dataset. 