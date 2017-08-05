import random as r
import requests as req
import sys
import time

def deduce_topic(frequencies, rand_num):
  for topic, _range in frequencies.items():
    if _range[0] <= rand_num <= _range[1]:
      return topic


hot_topics = [
  ["Donald Trump", 0.35],
  ["Hillary Clinton", 0.05],
  ["Donald Trump Jr", 0.15],
  ["John McCain", 0.15],
  ["Jeff Sessions", 0.10],
  ["ObamaCare", 0.20]]

total = 0
frequencies = {}
for topic, probability in hot_topics:
  frequencies[topic] = [total, total + probability]
  total += probability

if __name__ == "__main__":
  if sys.argv[1:]:
    end_point = sys.argv[1]
    while True:
      time.sleep(1)
      rand_num = r.random()
      body = { "topic": deduce_topic(frequencies, rand_num) }
      response = req.post(end_point, data=body)
      print(response.text)
  else:
    print("I need an endpoint to send hot topic feed")
    print("Try adding a command line parameter")
    