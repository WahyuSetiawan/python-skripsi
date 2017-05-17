"""percobaan pertama untuk grabing data dari timeline pribadi"""

import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
import time

consumer_key = "6inis336fYaeltR9HNx9Z53Nz"
consumer_secret = "pwc3WC6v66sEDKa1FX1yU60JKLqJBHQNyMzH9cb6qrVman6Ysg"
token_access = "249136721-NoGGz9rSUemSKJtpSe8NI9pMcxlDZKfioLmk8iGC"
token_secret = "IcjwJ9vtRUH8egbUHRmQ2ZekkqqYNDU0nPld5dYfrF9qu"

auth = OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(token_access,token_secret)

api = tweepy.API(auth)

"""for status in tweepy.Cursor(api.user_timeline).items():
	print(status._json)"""
	
class MyListener(StreamListener):
	def __init__(self, time_limit = 60):
		self.start_time = time.time()
		self.limit = time_limit
		super(MyListener, self).__init__()
		
	def on_data(self, data):
		try:
			if(time.time() - self.start_time) < self.limit:			
				with open('python.json', 'a') as f:
					f.write(data)
					return True
			else:
				return False
		except BaseException as e:
			print("Error on_data: %s" % str(e))
		return True
	def on_error(self, status):
		print(status)
		return True
	
twitter_stream = Stream(auth, MyListener(time_limit = 20))
twitter_stream.filter(track=['gunung', 'pantai'], languages=["en"], locations = [-7.6411, 100.179, -8.185174,110.802])