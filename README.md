# PySyntext
A python package to summarize text columns in a dataframe

Team Members

|Name | Github |
|---|---|
| Harjyot Kaur |[harjyotkaur](https://github.com/HarjyotKaur)  |
| Alexander Pak | [pak-alex](https://github.com/pak-alex) |
| Yenan Zhang |[YenanZ](https://github.com/YenanZ)  |


### Function 1: TextSummarize

`TextSummarize` function of class `PySyntext` takes in `string` as an input and produces `DataFrame` as an output containing a quantitative summary of the input. The quantitative summary needs:

- Number of Words
- Number of Sentences
- Most Common Word/Words
- Least Common Word/Words
- Average Word Length
- Average Sentence Length

| Name | Type |
|---|---|
| Input | String |
| Output | Dataframe |

#### Output: Dataframe

|Column| Type|
|---|---|
| word_count | int |
| sentence_count | int |
| most_common | int |
| least_common | int |
| avg_word_len | int |
| avg_sentence_len| int |

The function takes in the following arguments:

| Name | Type | Default|
|---|---|---|
| stopwords_remove | boolean | True |
| lemitize | boolean | False |
| encoding | string | ‘utf-8’|
| remove_punctuation | boolean | True |
| remove_numbers |  boolean | True |
| case_sensitive |  boolean | False |
| gibberish_remove |  boolean | True  |
| split_by | char | *space*  |

### Function 2: TextGrams

`TextGrams` function of class `PySyntext` takes in `string` as an input and produces `DataFrame` as an output containing lists of top 5 ngrams. The top `k` ngrams and `n` are user based inputs with default values (k=5 and n=(2,3))

| Name | Type |
|---|---|
| Input | String |
| Output | Dataframe |

#### Output: Dataframe

|Column| Type|
|---|---|
| ngrams | list |
*Number of rows are dependent on the input  `n` of the user*
*Size of the list is dependent on the input `k` of the user*

The function takes in the following arguments:

| Name | Type | Default|
|---|---|---|
| k | int | 5 |
| n | int,list | (2,3) |
| stopwords_remove | boolean | True |
| lemitize | boolean | False |
| encoding | string | ‘utf-8’|
| remove_punctuation | boolean | True |
| remove_numbers |  boolean | True |
| case_sensitive |  boolean | False |
| gibberish_remove |  boolean | True  |
| split_by | char | *space*  |

### Function 3: TextQuality

`extQuality` function of class `PySyntext` takes in `string` as an input and produces `DataFrame` as an output a qualitative summary of the input. The qualitative summary would include the following:

- Spelling Mistakes: Words spelt wrong/Total words
- Overall Sentiment: "Positive" or "Negative"

| Name | Type |
|---|---|
| Input | String |
| Output | Dataframe |

#### Output: Dataframe

|Column| Type|
|---|---|
| spell_mistake | float |
| sentiment | string |

The function takes in the following arguments:

| Name | Type | Default|
|---|---|---|
| encoding | string | ‘utf-8’|
| split_by | char | *space*  |

### Function 4: TextTags

`TextTags` function of class `PySyntext` takes in `string` as an input and produces `DataFrame` as an output containing a summary of parts of speech tags.

| Name | Type |
|---|---|
| Input | String |
| Output | Dataframe |

#### Output: Dataframe

|Column| Type|
|---|---|
| nouns | int |
| verbs | int |
| adjectives | int |

The function takes in the following arguments:

| Name | Type | Default|
|---|---|---|
| encoding | string | ‘utf-8’|
| split_by | char | *space*  |
