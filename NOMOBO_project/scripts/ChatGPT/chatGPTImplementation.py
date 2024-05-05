import os
import openai
import pandas as pd
import configparser
import datetime
from pathlib import Path

p = Path(__file__).parents[2]

# Read config.ini file
config_obj = configparser.ConfigParser()
config_obj.read(str(p)+"/Config/Configconfigfile.ini")
chatgptConfig = config_obj["chatgpt"]

# set your parameters for the database connection URI using the keys from the configfile.ini
api_Key = chatgptConfig["api_Key"]
inputFile = chatgptConfig["inputfile"]
outputFile = chatgptConfig["outputfile"]
compName = chatgptConfig["competitorname"]
task = chatgptConfig["chatgpttask"]

currDate = (datetime.datetime.now()).date()
newpath = inputFile+str(currDate)+'/'
print(newpath)
if not os.path.exists(newpath):
    os.makedirs(newpath)

reviews_df = pd.read_csv(newpath+compName+'_reviews.csv')
reviews = reviews_df['Reviews']

# openai.api_key = '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'
# openai.api_key = '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' - Brad's key
openai.api_key = api_Key
response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {
      "role": "system",
      "content": task
    },
    {
      "role": "user",
      "content": "'reviews -' {0}".format(reviews)
    }
  ],
)
data = (response['choices'])[0]['message']['content']
text_file = open(outputFile+compName+'_chatgpt_solution.txt', 'w')
text_file.write(data)
text_file.close()
