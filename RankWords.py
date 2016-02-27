import nltk
def RankWords(filename):
    document = open(filename).read()
    words=nltk.tokenize.word_tokenize(document)
    print (words)
    
    
if __name__ == '__main__':
    RankWords("Test.txt")
