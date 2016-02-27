import nltk
def RankWords(filename):
	document = open(filename).read()
	words=nltk.tokenize.word_tokenize(document)
	Print (words)

def main():
    RankWords("Test.txt")

    main()
