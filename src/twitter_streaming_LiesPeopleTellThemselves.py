#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy import API
import json

#Variables that contains the user credentials to access Twitter API
access_token = "1177825206-3F1lDtdIG2ZXWIElTaPom1TOIw50mxmibSvZ101"
access_token_secret = "zoOzBdLYdHG0pP30UZM1znSt5RAWAp7OYrSSeG2Xe3I8N"
consumer_key = "S3ZN012qzgK1IeR6yL5gnNFFX"
consumer_secret = "EfpDZrGtfv5Aw8y687hMoOYpv3TzFwHhVDot5FTkuuCHfOC7hb"

class FileWriteListener(StreamListener):

    def __init__(self):
        super(StreamListener, self).__init__()
        self.save_file = open('../data_LiesPeopleTellThemselves/tweets.json','w')
        self.tweets = []

    def on_data(self, tweet):
        self.tweets.append(json.loads(tweet))
        self.save_file.write(str(tweet))

    def on_error(self, status):
        print(status)
        return True


auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = API(auth)

twitter_stream = Stream(auth, FileWriteListener())
# Here you can filter the stream by:
#    - keywords (as shown)
#    - users
twitter_stream.filter(track=['#LiesPeopleTellThemselves'])
