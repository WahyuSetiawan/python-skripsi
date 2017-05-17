import tweepy
import datetime
import xlsxwriter
import sys

# credentials from https://apps.twitter.com/
consumerKey = "6inis336fYaeltR9HNx9Z53Nz"
consumerSecret = "pwc3WC6v66sEDKa1FX1yU60JKLqJBHQNyMzH9cb6qrVman6Ysg"
accessToken = "249136721-NoGGz9rSUemSKJtpSe8NI9pMcxlDZKfioLmk8iGC"
accessTokenSecret = "IcjwJ9vtRUH8egbUHRmQ2ZekkqqYNDU0nPld5dYfrF9qu"

auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
auth.set_access_token(accessToken, accessTokenSecret)

api = tweepy.API(auth)

username = sys.argv[1]
startDate = datetime.datetime(2017, 5, 1, 15, 39, 41)
endDate =   datetime.datetime(2017, 5, 6, 15, 39, 41)

tweets = []
tmpTweets = api.search(q=username, count =100)

for tweet in tmpTweets:
    if tweet.created_at < endDate and tweet.created_at > startDate:
        print("Last Tweet @", tweet.text, " - fetching some more")
        tweets.append(tweet)

"""
while (tmpTweets[-1].created_at > startDate):
    print("Last Tweet @", tmpTweets[-1].created_at, " - fetching some more")
    tmpTweets = api.search(username, max_id = tmpTweets[-1].id)
    for tweet in tmpTweets:
        if tweet.created_at < endDate and tweet.created_at > startDate:
            tweets.append(tweet)
"""
workbook = xlsxwriter.Workbook(username + ".xlsx")
worksheet = workbook.add_worksheet()
row = 0
for tweet in tweets:
    worksheet.write_string(row, 0, str(tweet.id))
    worksheet.write_string(row, 1, str(tweet.created_at))
    worksheet.write(row, 2, tweet.text)
    worksheet.write_string(row, 3, str(tweet.in_reply_to_status_id))
    row += 1

workbook.close()
print("Excel file ready")