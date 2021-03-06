### Sentiment 

#### Outline

We looked to sentiment as an initial sentence measurement to expand on the data supplied by Kaggle. Generating the data and evaluating the resulting values entails the following steps, which later sections will cover in greater detail:

1. Retrieve Data, Install Packages
2. Format Data
3. Calculate Sentiment
4. Predict Toxicity

##### 1 - Retrive Data, Install Packages

If you have not already, get the train.csv and test.csv files for the Kaggle competition "Jigsaw Unintended Bias in Toxicity Classification" (https://www.kaggle.com/c/jigsaw-unintended-bias-in-toxicity-classification/data). Once you have the files, install the 
following python packages

```
$ sudo pip3 install vaderSentiment
$ sudo pip3 install keras
$ sudo pip3 install statistics
```

##### 2 - Format Data

Format data by executing the formatData.py script. By default, the script makes files over several steps and stores them in the "data" direcotry of this package, but you may specify another location. Here are the arguments

```
usage: formatData.py [-h] -train TRAIN -test TEST [-singQuote] [-wd WORKDIR]
```

TRAIN is a path to the Kaggle file train.csv, TEST is a path to the Kaggle file test.csv, singQuote is an option to include single quotes that occur in words (like "we're"), and the WORKDIR is a directory noted in the previous paragraph (default: package directory "data/")

##### 3 - Calculate Sentiment

##### 4 - Predict Toxicity

The script applySentiment.py takes the values calculated and stored in the "data/" directory (or a different directory if one was specified earlier), and applies those values to the test.csv file from Kaggle to generate a submission.csv file for the Kaggle compitition. The script takes the following arguments:

```
usage: applySentiment.py [-h] -test TEST [-wd WORDDIR] [-s0 S0] [-s1 S1]
                         [-s2 S2] -o O [-singQuote]
```

TEST is a path to the Kaggle file test.csv, WORKDIR is a directory noted in the previous sections (default: package directory "data/"), and the values s0, s1, and s2, are constants applied to the application of statistical data to generate predictions (default: .6, .3, and .15 respectively)



