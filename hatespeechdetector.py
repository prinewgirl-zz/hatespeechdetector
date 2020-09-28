#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import argparse
import configparser
import os
from lib import TwitterModule
from lib import HandleExceptions
from tweepy import error
import sys

config = configparser.ConfigParser()
config.read(os.path.join(os.getcwd(),"parameters.ini"))
consumer_key = config.get("Geral","CONSUMER_KEY")
consumer_secret = config.get("Geral","CONSUMER_SECRET")
acess_token = config.get("Geral","ACESS_TOKEN")
acess_token_secret = config.get("Geral","ACESS_TOKEN_SECRET")
user = config.get("Geral","USERNAME")

parser = argparse.ArgumentParser()
parser.add_argument('--add', help='Adiciona uma hashtag',
                                        metavar='<hashtag>',default=None)
parser.add_argument('--remove', help='Remove uma hashtag',
                                        metavar='<hashtag>',default=None)
parser.add_argument('--filter', help='Filtra uma hashtag especificando  a \
                    hashtag e o tempo',
                                        metavar='<arg>',default=None, nargs=2)
args = parser.parse_args()


def filter(text, time):
    ''' Input:
        some pattern
        Output:
        Stream of tweets matching a pattern
   '''
    try:
        bot.stream(text, time)
    except KeyboardInterrupt:
        sys.exit()

try:    

    bot = TwitterModule.ManageTwitter(consumer_key,consumer_secret,\
                                          acess_token, acess_token_secret)
    bot.verify()
    
 
    if args.filter is not None:
        filter(args.filtra[0], int(args.filter[1]))

except HandleExceptions.LengthError as tamexce:
    sys.stderr.write(tamexce)
    sys.exit()
except HandleExceptions.HashtagNotFound as hashnot:
    sys.stderr.write(hashnot)
    sys.exit()
except error.TweepError as error:
    print("Tweep API Problem")
    sys.stderr.write(error)
    sys.exit()
except KeyboardInterrupt:
    sys.exit()
