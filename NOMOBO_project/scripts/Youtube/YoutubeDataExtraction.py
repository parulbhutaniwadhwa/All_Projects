import pandas as pd
import csv
import configparser
import unidecode  #function unidecode() takes Unicode data and tries to represent it in ASCII characters
from googleapiclient.discovery import build
import os
import datetime
from pathlib import Path

p = Path(__file__).parents[2]

# Read config.ini file
config_obj = configparser.ConfigParser()
config_obj.read(str(p)+"/Config/Configconfigfile.ini")
ytConfig = config_obj["youtube"]

# set your parameters for connection using the keys from the configfile.ini
developerKey = ytConfig["developerKey"]
compName = ytConfig["competitorName"]
outputFile = ytConfig["outputFile"]
searchkw = ytConfig["searchkw"]

currDate = (datetime.datetime.now()).date()
newpath = outputFile+str(currDate)+'/'
print(newpath)
if not os.path.exists(newpath):
    os.makedirs(newpath)


# Set DEVELOPER KEY to the API key value obtained from the APIs & auth > Registered applications section.
# Please make sure the YouTube Data API is turned on.
#   https://cloud.google.com/console

DEVELOPER_KEY = developerKey
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"


def youtube_search():
    # Construct a Resource for interacting with an API.
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)
    # Call the search.list method to retrieve results matching the specified query term.
    # more detail refer: https://developers.google.com/youtube/v3/docs/search
    #search_response = youtube.search().list(q="laptop", part="id,snippet", maxResults=50).execute()
    search_response = youtube.search().list(q=searchkw, part="id,snippet", maxResults=50).execute()

    videos = []
    channels = []
    playlists = []

    # create a CSV output for video list
    csvFile = open(newpath+compName+'_ytVideos.csv','w', newline='')
    csvWriter = csv.writer(csvFile)
    csvWriter.writerow(["publishDate","title","description","videoId","viewCount","likeCount","dislikeCount","commentCount","favoriteCount"])

    # Add each result to the appropriate list, and then display the lists of
    # matching videos, channels, and playlists.
    for search_result in search_response.get("items", []):
        if search_result["id"]["kind"] == "youtube#video":
            title = search_result["snippet"]["title"]
            title = unidecode.unidecode(title)  # Dongho 08/10/16
            videoId = search_result["id"]["videoId"]
            video_response = youtube.videos().list(id=videoId,part="statistics").execute()
            for video_result in video_response.get("items",[]):
                viewCount = video_result["statistics"]["viewCount"]
                if 'likeCount' not in video_result["statistics"]:
                    likeCount = 0
                else:
                    likeCount = video_result["statistics"]["likeCount"]
                if 'dislikeCount' not in video_result["statistics"]:
                    dislikeCount = 0
                else:
                    dislikeCount = video_result["statistics"]["dislikeCount"]
                if 'commentCount' not in video_result["statistics"]:
                    commentCount = 0
                else:
                    commentCount = video_result["statistics"]["commentCount"]
                if 'favoriteCount' not in video_result["statistics"]:
                    favoriteCount = 0
                else:
                    favoriteCount = video_result["statistics"]["favoriteCount"]
            description = search_result["snippet"]["description"]
            description = unidecode.unidecode(description)
            publishDate = search_result['snippet']['publishedAt']

            csvWriter.writerow([publishDate, title,description,videoId,viewCount,likeCount,dislikeCount,commentCount,favoriteCount])

    csvFile.close()

youtube_search()

df = pd.read_csv(newpath+compName+'_ytVideos.csv')
# Getting all Description inn a list
description_list = df['description'].tolist()

# Remove nan values from list
description_list = [x for x in description_list if str(x) != 'nan']


# api_key = 'AIzaSyAyq5KT6-atTmkdIaf8H6legZd_eg2i0FM'
api_key = developerKey
# Enter video id
# video_id = "wmiL7dRz784"

csvFile = open(newpath+compName+'_YTcomments.csv','w', newline='')
csvWriter = csv.writer(csvFile)
csvWriter.writerow(["publishDate","comment","reply"])


def video_comments(video_id):
    # empty list for storing reply
    replies = []

    # creating youtube resource object
    youtube = build('youtube', 'v3', developerKey=api_key)

    # retrieve youtube video results
    video_response=youtube.commentThreads().list(part='snippet,replies',videoId=video_id).execute()
    #print(video_response['items'][0]['snippet']['topLevelComment']['snippet']['publishedAt'])#['textDisplay'])

    # iterate video response
    #while video_response:

    # extracting required info
    # from each result object
    for item in video_response['items']:

        # Extracting comments
        comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
        publishDate = video_response['items'][0]['snippet']['topLevelComment']['snippet']['publishedAt']
        # counting number of reply of comment
        replycount = item['snippet']['totalReplyCount']

        # if reply is there
        if replycount > 0:

            # iterate through all reply
            for reply in item['replies']['comments']:

                # Extract reply
                reply = reply['snippet']['textDisplay']

                # Store reply is list
                replies.append(reply)

        # print comment with list of reply
        #print(comment, replies, end = '\n\n')
        csvWriter.writerow([publishDate, comment, replies])


        # empty reply list
        replies = []


# Call function

new_df = pd.read_csv(newpath+compName+'_ytVideos.csv')
for id in new_df['videoId']:
    try:
        video_comments(id)
    except:
        pass
csvFile.close()