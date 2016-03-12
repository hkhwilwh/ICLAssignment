from Bio import Medline 
from nltk.corpus import stopwords
from nltk.corpus import treebank
import nltk
import networkx as nx
import matplotlib.pyplot as plt
import string


from nltk.util import ngrams

stop = stopwords.words('english')
#this array to save the none noune and adjective word 
tagged_word =[]

for word, tag in treebank.tagged_words():
    if tag != "N" and tag!="ADJ":
        tagged_word.append(word)
        
        

with open("C:\\t\\result.txt") as handle:
    records = Medline.parse(handle)
    
    for record in records:
        g=nx.Graph()
        recordNoStop = ' '
        for wrd in record["AB"].split():
            if ((wrd not in stop) and (wrd not in tagged_word)):recordNoStop  = recordNoStop + wrd + ' '
        words=nltk.tokenize.word_tokenize(recordNoStop)
        
        #remove punctuation  
    for c in string.punctuation:
              if c in words: words.remove(c)
              
g.add_nodes_from(words)
bg=ngrams(words,2)
g.add_edges_from(bg)

print(nx.shortest_path(g))

        #print(nltk.pos_tag(words))

        ##nx.draw(g,with_labels=True,node_size=3000,font_size=8,font_color="navy",node_color="orange")
        ##plt.show()

        #recordNoStop = ' '
        #for wrd in record["AB"].split():
            #if wrd not in stop:recordNoStop  = recordNoStop + wrd + ' '
        #print(recordNoStop)

        #print(record["AB"])
        #print(record["OT"])



 

#print(txt)
    #words=nltk.tokenize.word_tokenize(txt)
    #print(nltk.pos_tag(words))
    #g=nx.Graph()
    #g.add_nodes_from(words)
    #bg=ngrams(words,2)
    #g.add_edges_from(bg)
    #print("Words as nodes: \n",g.nodes())
    #print("Edges between bigrams: \n", g.edges())
