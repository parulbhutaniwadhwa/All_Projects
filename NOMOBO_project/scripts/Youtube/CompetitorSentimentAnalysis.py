from textblob import TextBlob
import pandas as pd
import datetime
import configparser
import os
from pathlib import Path

p = Path(__file__).parents[2]

# Read config.ini file
config_obj = configparser.ConfigParser()
config_obj.read(str(p)+"/Config/Configconfigfile.ini")
ytConfig = config_obj["youtube"]

# set your parameters for the database connection URI using the keys from the configfile.ini
developerKey = ytConfig["developerKey"]
compName = ytConfig["competitorName"]
outputFile = ytConfig["outputFile"]
searchkw = ytConfig["searchkw"]

currDate = (datetime.datetime.now()).date()
newpath = outputFile+str(currDate)+'/'
print(newpath)
if not os.path.exists(newpath):
    os.makedirs(newpath)

# Reading the data from CSV file
df = pd.read_csv(newpath+compName+'_YTcomments.csv', encoding_errors= 'replace')

# Create a function to get the subjectivity
def getSubjectivity (text):
    return TextBlob(text).sentiment.subjectivity

# Create a function to get the polarity
def getPolarity (text):
    return TextBlob(text). sentiment.polarity

# Create two new columns
df ['comment_Subjectivity'] = df['comment'].apply(getSubjectivity)
df['comment_Polarity'] = df['comment'].apply(getPolarity)

def getAnalysis (x):
    if x < 0:
        return 'Negative'
    elif x == 0:
        return 'Neutral'
    else:
        return 'Positive'

# Create a new Column with all conditions which we defined based on that give the output like negative, neutral and positive.
df['Data_Analysis'] = df['comment_Polarity'].apply(getAnalysis)


df['publishDate'] = df['publishDate'].apply(lambda x: datetime.datetime.strptime((x.split('T'))[0],'%Y-%m-%d').date())

df['Year'] = df['publishDate'].apply(lambda x: x.year)
df['Month'] = df['publishDate'].apply(lambda x: x.month)


df.to_csv(newpath+compName+'_sentimentAnalysis.csv')

'''
df1 = pd.read_csv('curie_final_dataset.csv')
df1['comp_name'] = 'Curie'
df2 = pd.read_csv('lume_final_dataset.csv')
df2['comp_name'] = 'Lume'
df3 = pd.read_csv('native_final_dataset.csv')
df3['comp_name'] = 'Native'

fin_df = df1.append(df2)
fin_df = fin_df.append(df3)
fin_df.to_csv('allCompetitorsData.csv')
'''