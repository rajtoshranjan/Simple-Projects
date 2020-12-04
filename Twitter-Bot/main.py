import tweepy
import time

api_key = ""
api_secret_key = ""

access_token = ""
access_token_secret = ""

auth = tweepy.OAuthHandler(api_key, api_secret_key)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

def TweetFun():
	f_read = open('previous_tweet_id.txt', 'r')
	last_tweet_id = int(f_read.read().split()[0])
	f_read.close()

	print(last_tweet_id)

	mentions = api.mentions_timeline(last_tweet_id, tweet_mode = 'extended')
	# print(mentions)
	for mention in mentions:
		user = mention.user.screen_name
		if user == "RajtoshR":
			text = str(mention.full_text).replace('@codingunda', '#CodinGunda')
			api.update_status(text)
			print("Tweeted "+ str(mention.id) + ":- " +mention.full_text)
			f_write = open('previous_tweet_id.txt', 'w')
			f_write.write(str(mention.id))

if __name__ == "__main__":
	while True:
		TweetFun()
		time.sleep(10)

