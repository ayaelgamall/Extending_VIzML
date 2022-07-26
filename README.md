# Extending_VIzML

This repository provides taking the config files of each visualization and convert it to format to be able to train Bert transformer to take its embeding

# Data Description
We provide String of configirations 

## Accessing Data
would be in preProcess.py as String input could understand the structure of the sentences by looking to 'mapExplain.txt'

## Preparing Data
run 'preProcess.py' first to extract your dataset as text file (exists as text file with name "text_dataset.txt")

## Geting Bert unique Vocabulary
it is the text file (allVoc.txt) made by running 'uniqueVoc.py' then 'GenVoc.py' to add other possible vocabularies

## Preparing the tokenizer
run 'tokenizer_init.py' to prepare Bert Tokenizer with the new vocabulary.(allVoc.txt)

## Model Training
run 'tokenizer_pipeline.py' to train Bert model on the dataset and save it to 'Bert-configs'

get the pretrained model without all these steps from this link :
  https://drive.google.com/file/d/1lhS0QVJY767hb1nHfHJn1UloHGtzeVNx/view?usp=sharing
