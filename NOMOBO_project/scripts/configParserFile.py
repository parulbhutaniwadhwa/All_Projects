import configparser
from pathlib import Path

p = Path(__file__).parents[1]

config = configparser.ConfigParser()

configFilePath = str(p)+'/Config/Configconfigfile.ini'
# Add the structure to the file we will create
config.add_section('NomoboCustomerReviews')
config.set('NomoboCustomerReviews', 'inputFile', 'C:/Users/parul/NewPycharmProjects/NOMOBO_project/inputFiles/CustomerReviews.xlsx')
config.set('NomoboCustomerReviews', 'outputFile', 'C:/Users/parul/NewPycharmProjects/NOMOBO_project/output/nomobo/')

config.add_section('youtube')
config.set('youtube','developerKey','AIzaSyAyq5KT6-atTmkdIaf8H6legZd_eg2i0FM')
config.set('youtube', 'competitorName', 'curie')
config.set('youtube', 'searchkw', 'curie deodorant')
config.set('youtube', 'outputFile', 'C:/Users/parul/NewPycharmProjects/NOMOBO_project/output/youtube/')

config.add_section('amazon')
config.set('amazon','api_Key','2a919faccc70b4f2fdd8e2498fe342d5')
config.set('amazon', 'asin_id', 'B07GB3NVN1')
config.set('amazon', 'starReviews', 'one')
config.set('amazon', 'starReviews_num', '1')
config.set('amazon', 'lookupPages', '2')
config.set('amazon', 'competitorName', 'Native')
config.set('amazon', 'outputFile', 'C:/Users/parul/NewPycharmProjects/NOMOBO_project/output/amazon/')

config.add_section('chatgpt')
config.set('chatgpt','api_Key','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')
config.set('chatgpt', 'inputFile', 'C:/Users/parul/NewPycharmProjects/NOMOBO_project/output/amazon/')
config.set('chatgpt', 'outputFile', 'C:/Users/parul/NewPycharmProjects/NOMOBO_project/output/chatGPT/')
config.set('chatgpt', 'competitorName', 'Native')
config.set('chatgpt', 'chatgptTask', 'You will be provided with a list of customer reviews and your task is to highlight trend points.')
# Write the new structure to the new file
with open(configFilePath, 'w') as configfile:
    config.write(configfile)