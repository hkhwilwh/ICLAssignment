from apriori import *

data = ["ABCDEFGHIJKL","ZOPQABCDLMNOP","REWQZOPQAB"]

patterns = Apriori(data, 34)

print(patterns)