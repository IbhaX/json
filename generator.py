from requests import get
from random import randint, choice
import json


def username_generator(length):
  url ="https://random-word-api.herokuapp.com/all"
  response = get(url)
  words = [i for i in response.json()]
  with open('usernames.json', 'a') as f:
    for i in words:
      f.write(i)
  



