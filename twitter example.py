#Twittwer_status_updater	
import tweepy
import time
def login_to_twitter(consumer_key, consumer_secret, access_token, access_token_secret): 
    auth = tweepy.OAuthHandler(consumer_key,  consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    ret = {}
    ret['api'] = api
    ret['auth'] = auth
    return  api
def post_tweets():
    consumer_key='JznligRYryxpSNmqxoQ09d7FA'
    consumer_secret='9JssHmrqxq3cNBelDJkjoQji4xO59w3ggJlVaKxDnCINwlyz9t'
    access_token='2280491525-J5VZ4XdKyBQ5orJFkpmQAAF5CjE0RudaGjGJtH5'
    access_token_secret='XcSFOlxMDyApbEhRq7z9vvWZmnzNCLbG9ccZRu8Rm6pcr' 
    message = "ok" 
    api = login_to_twitter(consumer_key, consumer_secret, access_token, access_token_secret)
    ret = api.update_status(status=message)
    time.sleep(2)
a=0
while(a<2):
    if __name__ == '__main__':
        post_tweets()
    a+=1
        


   
