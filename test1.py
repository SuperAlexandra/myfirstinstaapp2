print("ddd")


"""
class Person:
    sex=""
    age=0
    name=""
    def present(self):
        print("May name is {} and i am {} years old and i am a {}".format(self.name,self.age,self.sex))

    def setSex(self, sex):
        if sex!="male" and sex!="Female":
            raise Exception("not big valid")
        else:
            self.sex=sex


"
person=Person()
person.setSex("male")
person.age=13
person.name="John"
person.present()


x1 = input("What s your name?")
x2 = input("And yours?")

w1 = input("%s chose your weapon:" %x1)
w2 = input("%s, and yours:" %x2)

def compare(w1,w2):
 if w1 == "rock":
    if w2 == "scissors":
        return(x1)
    elif w2 == "paper":
        return (x2)
 elif w1 == "scissors":
        if w2 == "rock":
          return(x2)
        elif w2 == "paper":
         return(x1)
 elif w1 == "paper":
     if w2 == "rock":
        return(x1)
     elif w2 == "scissors":
        return(x2)
 else:
     print("Please chose valid weapons")

print(compare(w1,w2), "wins")


import random

def guess():
 a = random.randint(1,10)
 x1 = input("Try a number: ")
 if x1 != int:
  x1 = input("Must be a number: ")
 while int(x1) != a:
    if int(x1) < a:
        x1 = input("try higher: ")
    elif int(x1) > a:
      x1 = input("try lower: ")

 else:
    return("nailed it")

print(guess())



def convert(c,d):
 if d == "C":
  c = c*1.8+32
  return c, "F"
 elif d == "F":
  c = (c-32)/1.8
  return c, "C"
 else:
  return("Not a valid input")

#a = input("Chose one option: \n 1.Convert from C in F \n 2.Covert from F in C \n")
a = input("Put in value you want to transform: ")
b = int(a[0:-1])
d = a[-1].upper()

#c = input("Temperature in Celsius: ")
print("Temperature:", convert(b,d))

"""
python -m

pip install InstagramAPI

import pprint
from time import sleep
from InstagramAPI import InstagramAPI
import pandas as pd

def get_my_profile_details():
    api.login()
    api.getSelfUsernameInfo()
    result = api.LastJson
    username = result['user']['username']
    full_name = result['user']['full_name']
    profile_pic_url = result['user']['profile_pic_url']
    followers = result['user']['follower_count']
    following = result['user']['following_count']
    media_count = result['user']['media_count']
    df_profile = pd.DataFrame(
        {'username':username,
        'full name': full_name,
        'profile picture URL':profile_pic_url,
        'followers':followers,
        'following':following,
        'media count': media_count,
        }, index=[0])
    df_profile.to_csv('profile.csv', sep='\t', encoding='utf-8')

def get_my_feed():
    image_urls = []
    api.login()
    api.getSelfUserFeed()
    result = api.LastJson
    # formatted_json_str = pprint.pformat(result)
    # print(formatted_json_str)
    if 'items' in result.keys():
        for item in result['items'][0:5]:
            if 'image_versions2' in item.keys():
                image_url = item['image_versions2']['candidates'][1]['url']
                image_urls.append(image_url)

    df_feed = pd.DataFrame({
                'image URL':image_urls
            })
    df_feed.to_csv('feed.csv', sep='\t', encoding='utf-8')

get_my_profile_details()