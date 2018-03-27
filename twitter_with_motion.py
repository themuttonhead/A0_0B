from gpiozero import MotionSensor
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
    consumer_key='x3m3PkACEdHniZPL8dAJ5mDz'
    consumer_secret='5tmu1NMV9SjZJjcDfE1dbd5q5IPxq2ioSX2jmSrt1Inc031F2'
    access_token='968403555492167680-hQ2rGpiINbCKDTk9gSFdgn43lp8wT9'
    access_token_secret='4V1cBDQrNat4FndawyN1GobFZ9YlQiHzmyUvrbbObdKr' 
    api = login_to_twitter(consumer_key, consumer_secret, access_token, access_token_secret)
    PIR=MotionSensor(4)
    if PIR.motion_detected:
        time.sleep(2)
        print("motion")
        cmd="fswebcam -F 3 --fps 20 -r 800x600 /home/pi/img.jpg"
        os.system(cmd)
        img="/home/pi/img.jpg"
        print("pic taken")

    else:
        print("no")
      
    ret = api.update_with_media(img,status="hey")
    time.sleep(5)
   
post_tweets()
