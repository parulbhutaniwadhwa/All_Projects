from textblob import TextBlob
import pandas as pd
import configparser
from pathlib import Path

p = Path(__file__).parents[2]
# Read config.ini file
config_obj = configparser.ConfigParser()
config_obj.read(str(p)+"/Config/Configconfigfile.ini")
nomoboReviewsData = config_obj["NomoboCustomerReviews"]

# set your parameters for the database connection URI using the keys from the configfile.ini
inputReviewsfile = nomoboReviewsData["inputFile"]
outputFile = nomoboReviewsData["outputFile"]

# Reading the data from CSV file
df = pd.read_excel(outputFile+'NomoboReviewsDatacleaning.xlsx')

# Create a function to get the subjectivity
def getSubjectivity (text):
    return TextBlob(text).sentiment.subjectivity

# Create a function to get the polarity
def getPolarity (text):
    return TextBlob(text). sentiment.polarity

df['Remarks']=df['Remarks'].fillna('-')

#Create two new columns
df ['Data_Subjectivity'] = df['Remarks'].apply(getSubjectivity)
df['Data_Polarity'] = df['Remarks'].apply(getPolarity)
df ['Experience_Subjectivity'] = df['Experience Rating'].apply(getSubjectivity)
df['Experience_Polarity'] = df['Experience Rating'].apply(getPolarity)

#Evaluating positive, negative and neutral sentimaental analysis and adding it into the dataframe
def getAnalysis (x):
    if x < 0:
        return 'Negative'
    elif x == 0:
        return 'Neutral'
    else:
        return 'Positive'

# Create a new Column with all conditions which we defined based on that give the output like negative, neutral and positive.
df['Data_Analysis'] = df['Data_Polarity'].apply(getAnalysis)
df['Data_Analysis_Experience'] = df['Experience_Polarity'].apply(getAnalysis)

for i in range(0,len(df)):

  if(df['Data_Analysis'][i] == 'Neutral') and (df['Data_Analysis_Experience'][i] == 'Neutral'):
    df['Sentiment Analysis'][i] = 'Neutral'
  elif (df['Data_Analysis'][i] == 'Positive') and (df['Data_Analysis_Experience'][i] == 'Neutral'):
    df['Sentiment Analysis'][i] = 'Positive'
  elif (df['Data_Analysis'][i] == 'Negative') and (df['Data_Analysis_Experience'][i] == 'Neutral'):
    df['Sentiment Analysis'][i] = 'Negative'
  elif (df['Data_Analysis'][i] == 'Neutral') and (df['Data_Analysis_Experience'][i] == 'Positive'):
    df['Sentiment Analysis'][i] = 'Positive'
  elif (df['Data_Analysis'][i] == 'Positive') and (df['Data_Analysis_Experience'][i] == 'Positive'):
    df['Sentiment Analysis'][i] = 'Positive'
  elif (df['Data_Analysis'][i] == 'Negative') and (df['Data_Analysis_Experience'][i] == 'Positive'):
    df['Sentiment Analysis'][i] = 'Positive'
  elif (df['Data_Analysis'][i] == 'Neutral') and (df['Data_Analysis_Experience'][i] == 'Negative'):
    df.loc[i,'Sentiment Analysis'] = 'Negative'
  elif (df['Data_Analysis'][i] == 'Positive') and (df['Data_Analysis_Experience'][i] == 'Negative'):
    df['Sentiment Analysis'][i] = 'Negative'
  elif (df['Data_Analysis'][i] == 'Negative') and (df['Data_Analysis_Experience'][i] == 'Negative'):
    df['Sentiment Analysis'][i] = 'Negative'
  else:
    df['Sentiment Analysis'][i] = "Can't Say"

df.to_excel(outputFile+'NomoboSentimentAnalysisFinal.xlsx')
