import os
import time
import tweepy
def login_to_twitter(consumer_key, consumer_secret, access_token, access_token_secret): 
    auth = tweepy.OAuthHandler(consumer_key,  consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    ret = {}
    ret['api'] = api
    ret['auth'] = auth
    return  api
def post_tweets():
    consumer_key='JznliSRYryxpSNmqxoQ09d7FA'
    consumer_secret='9JsiHmrqxq3cNBelDJkjoQji4xO59wggJlVaKxDnCINwlyz9t'
    access_token='2280491725-J5VZ4XdKyBQ5orJFkpmQAAF5jE0RudaGjGJtH5'
    access_token_secret='XBSFOlxMDyApbEhRq7z9vvWZmnzNCLG9ccZRu8Rm6pcr' 
    api = login_to_twitter(consumer_key, consumer_secret, access_token, access_token_secret)
    #print("GG")
    
    cmd="fswebcam -F 3 --fps 20 -r 800x600 /home/ec2017b110/Desktop/img.jpg"
    os.system(cmd)
    img="/home/ec2017b110/Desktop/img.jpg"
    
    print("pic taken")
    ret = api.update_with_media(img,status="hey")
    time.sleep(5)
   
post_tweets()
    
