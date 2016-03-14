import json
from csv import DictWriter
from collections import defaultdict
import pandas as pd
import matplotlib.pyplot as plt
import re


class comparador(object):
    def __init__(self, current_dict, past_dict):
        self.current_dict, self.past_dict = current_dict, past_dict
        self.set_current, self.set_past = set(current_dict.keys()), set(past_dict.keys())
        self.intersect = self.set_current.intersection(self.set_past)
    def added(self):
        return self.set_current - self.intersect
    def removed(self):
        return self.set_past - self.intersect
    def changed(self):
        return set(o for o in self.intersect if self.past_dict[o] != self.current_dict[o])
    def unchanged(self):
        return set(o for o in self.intersect if self.past_dict[o] == self.current_dict[o])


def merge_lists(l1, l2, key):
  merged = {}
  for item in l1+l2:
    if item[key] in merged:
      merged[item[key]].update(item)
    else:
      merged[item[key]] = item
  return [val for (_, val) in merged.items()]


def main():

    tweets_data_1 = []
    tweets_file_1 = open('twitter1.txt', "r")
    for line in tweets_file_1:
        try:
            tweet = json.loads(line)
            tweets_data_1.append(tweet)
        except:
            continue

    tweets_data_2 = []
    tweets_file_2 = open('twitter2.txt', "r")
    for line in tweets_file_2:
        try:
            tweet = json.loads(line)
            tweets_data_2.append(tweet)
        except:
            continue


    #d = comparador(tweets_file_2, tweets_file_1)

    tweets_data_3 = []

    result = merge_lists(tweets_data_1, tweets_data_2 , 'id')

    with open("new-file.txt", 'wb') as f:
        f.write("\n".join(map(lambda x: str(x), result)) + "\n")

if __name__ == '__main__':
    main()
