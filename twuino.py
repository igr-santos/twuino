#!/usr/bin/env python
# coding: utf-8
# import time
from decouple import config
from tweepy import OAuthHandler, StreamListener, Stream


class StdOutListener(StreamListener):

    def on_status(self, status):
        print 'Tweet text:' + status.text
        return True

    def on_error(self, status_code):
        return True

    def on_timeout(self):
        return True


if __name__ == '__main__':
    listener = StdOutListener()
    auth = OAuthHandler(config('CONSUMER_KEY'), config('CONSUMER_SECRET'))
    auth.set_access_token(config('ACCESS_TOKEN'),
                          config('ACCESS_TOKEN_SECRET'))

    stream = Stream(auth, listener)
    stream.filter(track=['#twuino', '#pythonmg'])
