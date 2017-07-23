from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
from nltk import word_tokenize, sent_tokenize, pos_tag

ckey = 'Qn1Sny0x023q2cnr4dgpugpmQ'
csecret = 'j5U4Xqmfq3VW6jxm3yWyPu4SJxg3vh0arBS6Z2wpGypLhBH4Fj'
atoken = '193341077-2g0VnV7Poc3XBYXXoIKBdpCjYMjzjWDcHRrwrICH'
asecret = 'CWvAqsivt0CPiSw788pDKMWVqaY0nO5QSxL40un4k6uxE'


class listener(StreamListener):
    def on_data(self, data):
        try:
            tweet = data.split(',"text":"')[1].split('","source')[0]
            ## split data by
            sentences = sent_tokenize(tweet)
            print(sentences)
            print('\n')
            words = list()
            tagged = list()
            for sentence in sentences:
                words.append(word_tokenize(sentence))
            for word in words:
                print(word)
                print('\n')
                tagged.append(pos_tag(word))
            for eachTaggedWord in tagged:
                print(eachTaggedWord)
                print('\n')
        except BaseException as e:
            print('exception', str(e))

    def on_error(self, status):
        print(status)


auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())
twitterStream.filter(track=["Manchester United"])
