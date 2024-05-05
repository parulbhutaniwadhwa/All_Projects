import requests
from bs4 import BeautifulSoup
import pandas as pd
from urllib.parse import urlencode
import configparser
import os
import datetime
from pathlib import Path

p = Path(__file__).parents[2]

# Read config.ini file
config_obj = configparser.ConfigParser()
config_obj.read(str(p)+"/Config/Configconfigfile.ini")
amazonConfig = config_obj["amazon"]

# set your parameters for the database connection URI using the keys from the configfile.ini
api_Key = amazonConfig["api_Key"]
asin_id = amazonConfig["asin_id"]
outputFile = amazonConfig["outputfile"]
stars = amazonConfig["starreviews"]
stars_num = int(amazonConfig["starreviews_num"])
pages = int(amazonConfig["lookuppages"])
compName = amazonConfig["competitorname"]

currDate = (datetime.datetime.now()).date()
newpath = outputFile+str(currDate)+'/'
print(newpath)
if not os.path.exists(newpath):
    os.makedirs(newpath)


names = []
reviews = []
stars = []
data_string = ""
for num in range(1, pages):
    print(num)
    list_of_urls = ['https://www.amazon.com/product-reviews/'+asin_id+'/ref=cm_cr_arp_d_paging_btm_next_' + str(num) + '?pageNumber=' + str(num) + '&filterByStar='+str(stars)]
    #   'https://www.amazon.com/product-reviews/B07GB3NVN1/ref=cm_cr_arp_d_paging_btm_next_' + str(num) + '?pageNumber=' + str(num) + '&filterByStar=two_star']

    for url in list_of_urls:
        params = {'api_key': api_Key, 'url': url}
        response = requests.get('http://api.scraperapi.com/', params=urlencode(params))
        soup = BeautifulSoup(response.text, 'html.parser')

        for item in soup.find_all("span", class_="a-profile-name"):
            data_string = data_string + item.get_text()
            names.append(data_string)
            data_string = ""

        for item in soup.find_all("span", {"data-hook": "review-body"}):
            data_string = data_string + item.get_text()
            reviews.append(data_string)
            data_string = ""

        for item in soup.find_all("span", class_="a-icon-alt"):
            data_string = data_string + item.get_text()
            stars.append(data_string)
            data_string = ""
reviews_dict = {'Reviewer Name': names, 'Reviews': reviews, "Star Rating": stars}
print(len(names), len(reviews))
df = pd.DataFrame.from_dict(reviews_dict, orient='index')

df.dropna(axis=1, inplace=True)
prod_reviews = df.T
prod_reviews['Reviews'] = prod_reviews['Reviews'].str.replace('\n','')
prod_reviews.head(5)
prod_reviews['Star Rating'] = prod_reviews['Star Rating'].apply(lambda x: float(x.split(' ')[0]))
index_list = list(prod_reviews[prod_reviews['Star Rating'] > stars_num].index)
prod_reviews = prod_reviews.drop(index_list)
prod_reviews['Reviews'] = prod_reviews['Reviews'].str.replace('[^a-zA-Z0-9]',' ',regex=True)

prod_reviews.to_csv(newpath+compName+'_reviews.csv', index=False, header=True)
print(newpath+compName+'_reviews.csv')