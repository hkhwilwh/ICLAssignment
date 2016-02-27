import nltk
import networkx as nx
from nltk.util import ngrams
def RankWords(filename):
    document = open(filename).read()
    words=nltk.tokenize.word_tokenize(document)
    g=nx.Graph()
    g.add_nodes_from(words)
    bg=ngrams(words,2)
    g.add_edges_from(bg)
    
    print("Words as nodes: \n",g.nodes())
    print("Edges between bigrams: \n", g.edges())

    
    
if __name__ == '__main__':
    RankWords("Test.txt")
