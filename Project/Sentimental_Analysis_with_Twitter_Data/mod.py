import kafka
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from kafka import KafkaProducer, KafkaConsumer
import time

access_token = "1299195246945861632-OENwZ5etR4lN4ms33fMFlZQWvgNf0E"
access_token_secret =  "f2O00XlINrnqNA3FsEQKuOZKAyptjI30mhP1nhlCHNmXw"
consumer_key =  "OsMIjZbTOyAHnlEqjV1KDSqk1"
consumer_secret =  "MGe0Rjv9xwrFlcErT4IY9wdae00bImNEPyH6Ff8ZPbhmJmvza1"

class StdOutListener(StreamListener):
    def on_data(self, data):
        producer.send("trump", data.encode('utf-8'))
        print (data)
        saveFile = open('COVID-19DB.csv', 'a')
        saveFile.write(data)
        saveFile.write('\n')
        saveFile.close()
        return True

    def on_error(self, status):
        print (status)

#kafka = KafkaConsumer("localhost:9092")
producer = KafkaProducer(bootstrap_servers='localhost:9092', api_version=(0,11))

l = StdOutListener()	
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
stream = Stream(auth, l)
stream.filter(track=['COVID-19 in India'])