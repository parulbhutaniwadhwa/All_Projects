import pandas as pd
import configparser
import os
import datetime
from pathlib import Path

p = Path(__file__).parents[2]

# Read config.ini file
config_obj = configparser.ConfigParser()
config_obj.read(str(p)+'/Config/Configconfigfile.ini')
nomoboReviewsData = config_obj["NomoboCustomerReviews"]

# set your parameters for the database connection URI using the keys from the configfile.ini
inputReviewsfile = nomoboReviewsData["inputFile"]
outputFile = nomoboReviewsData["outputFile"]

currDate = (datetime.datetime.now()).date()
newpath = outputFile+str(currDate)+'/'
print(newpath)
if not os.path.exists(newpath):
    os.makedirs(newpath)


df = pd.read_excel(inputReviewsfile)

df['Would you switch to NOMOBO from your current deodorant brand?'] = df['Would you switch to NOMOBO from your current deodorant brand?'].apply(lambda x: x.split('.')[0])

cols_YN = ['Using a product that decreases my body odor increases my confidence.','NOMOBO felt gentle on my skin.','NOMOBO stopped my underarm stink (when using the product).','NOMOBO decreased my body odor.',
       'I felt that my body odor was under control when using NOMOBO.','I liked the smell of NOMOBO.','Would you switch to NOMOBO from your current deodorant brand?','Do you have a podcast or YouTube channel?','Do you use a clinical-strength deodorant?','Do you consider yourself to have sensitive skin?']

cols_TF = ['NOMOBO left no residue on my skin.','I experienced adverse reactions to NOMOBO.','I stopped using deodorant while I was using NOMOBO.','NOMOBO left my skin feeling fresh.']


def replace_YN(cols, df):

  for col in cols:
    new_col = 'new_'+col
    df[new_col]=df[col].apply(lambda x: 0 if x == 'No' else 1)
    # df = df.drop([col],axis=1)
  return df

def replace_TF(cols,df_1):
  for col in cols:
    new_col = 'new_'+col
    df_1[new_col]=df_1[col].apply(lambda x: 1 if x==True else 0)
    #df = df.drop([col],axis=1)
  return df

df_1 = replace_YN(cols_YN,df)
df_2 = replace_TF(cols_TF,df_1)
df_2 = df_2.drop(cols_YN+cols_TF,axis=1)

df_2.to_csv(newpath+'NomoboReviewsDatacleaning.csv')