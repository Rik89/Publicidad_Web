from operator import itemgetter
import sys

# datos provenientes de entrada
for line in sys.stdin:
    line = line.strip()

    # Analiza la entrada que recibimos del mapper.py
    word, count = line.split('\t', 1)

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
    tweets_file_1 = open('p1.txt', "r")
    for line in tweets_file_1:
        try:
            tweet = json.loads(line)
            tweets_data_1.append(tweet)
        except:
            continue

    tweets_data_2 = []
    tweets_file_2 = open('p2.txt', "r")
    for line in tweets_file_2:
        try:
            tweet = json.loads(line)
            tweets_data_2.append(tweet)
        except:
            continue
    # Hadoop ordena la salida de mapa por la llave en este caso
    # la palabra antes de pasar al reductor
   
        #d = comparador(tweets_file_2, tweets_file_1)

    tweets_data_3 = []

    result = merge_lists(tweets_data_1, tweets_data_2 , 'id')

    with open("new-file.txt", 'wb') as f:
        f.write("\n".join(map(lambda x: str(x), result)) + "\n")

if __name__ == '__main__':
    main()
