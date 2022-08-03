# Extending_VIzML

This repository provides taking the config files of each visualization and convert it to format to be able to train Bert transformer to take its embeding

# Data Description
We provide String of configirations 

## Accessing Data
would be in preProcess.py as String input 

## Map Understanding
To understand the structure of the sentences by looking to '**mapExplain.txt**'

## Preparing Data
To extract your dataset as text file (exists as text file with name "**text_dataset.txt**")

`python preProcess.py`


## Geting Bert unique Vocabulary
it is the text file ( **allVoc.txt** ) made by running 'uniqueVoc.py' then 'GenVoc.py' to add other possible vocabularies

`python uniqueVoc.py`

`python GenVoc.py`

## Preparing the tokenizer
To prepare Bert Tokenizer with the new vocabulary.(allVoc.txt)

`python tokenizer_init.py`

## Model Training
To train Bert model on the dataset and save it to **Bert-configs**

`python tokenizer_pipeline.py`

get the pretrained model without all these steps from this link :
  https://drive.google.com/file/d/1lhS0QVJY767hb1nHfHJn1UloHGtzeVNx/view?usp=sharing
