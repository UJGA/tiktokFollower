from TikTokApi import TikTokApi
import json
from playsound import playsound

# api = TikTokApi()

# count = 1

# tiktoks = api.byUsername('blakeriding', count=count)

api = TikTokApi()

count = 1

tiktoks = api.byUsername('blakeriding', count=count)
    
for tiktok in tiktoks:
    # print(tiktok.keys())
    userInfo = tiktok['authorStats']
    myStringCount = userInfo['followerCount']
    myCount = int(myStringCount)

myCountTemp = myCount

while True:
    api = TikTokApi()

    count = 1

    tiktoks = api.byUsername('blakeriding', count=count)
    
    for tiktok in tiktoks:
        # print(tiktok.keys())
        userInfo = tiktok['authorStats']
        myStringCount = userInfo['followerCount']
        myCount = int(myStringCount)

        if myCount > myCountTemp :
            print("Its Higher")
            playsound('yousuck.mp3')

        myCountTemp = myCount

        print(myCount)




