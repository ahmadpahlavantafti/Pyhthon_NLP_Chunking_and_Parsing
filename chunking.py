#CS 723: NLP
#HW 1 - Part 2 - Chunking and Partial Parsing
# Student: Ahmad Pahlavan Tafti


import nltk
import re
import pprint
from nltk import word_tokenize, pos_tag

#Problem 1: Exercise 7.2 NLTK

textchunk = [("many", "JJ"), ("researchers", "NNS"), ("two", "CD"), ("weeks", "NNS"), ("both","DT"), ("new", "JJ"), ("positions", "NNS")]
corpus = nltk.RegexpParser("NP:{<DT>?<CD>?<JJ>*<NNS>}")
corpus.parse(textchunk).draw()




#Problem 2: Exercise 7.5 NLTK

textchunk = [("the", "DT"), ("receiving", "VBG"), ("end","NN"), ("assistant", "NN"), ("managing","VBG"), ("editor", "NN")]
corpus = nltk.RegexpParser("Gerunds: {<DT>?<NN>?<VBG><NN>}")
corpus.parse(textchunk).draw()



#Problem 3: Exercise 7.6 NLTK

textchunk = [("July","NNP"), ("and","CC"), ("August","NNP"), ("all", "DT"), ("your", "PRP$"), ("managers", "NNS"), ("and", "CC"), ("supervisors", "NNS"), ("company","NN"), ("courts","NNS"), ("and","CC"), ("adjudicators","NNS")]
corpus = nltk.RegexpParser(" Coordinated noun: {<NNP><CC><NNP>|<DT><PRP\$><NNS><CC><NNS>|<NN><NNS><CC><NNS>}")
corpus.parse(textchunk).draw()






#Problem 4:

#source: http://www.bbc.com/news/science-environment-34378953
#Gerunds

sentences='UK scientists have successfully germinated seeds from the critically endangered Japanese Birch, a species that has just 21 known trees remaining. The seeds were collected last year during an expedition to a remote location in mountains near Tokyo. Experts suggest that the remaining wild population of Betula chichibuensis is too small to sustain itself unaided. The young trees will be shared with other arboretums in an effort to help conserve the threatened species. The International Union for the Conservation of Nature (IUCN) forecasts a bleak outlook for the tree species in the wild. The species is also self-incompatible, requiring two individuals to be close enough to cross-pollinate one another, making seed production uncertain in small subpopulations. During September and October, a team led by researchers from the University of Oxford Botanic Gardens, in conjunction with the University of Tokyo, embarked on an expedition to collect seed samples from the threatened birch trees. It is found in a very, very remote location and it is not an easy place to get to. It has got very, very low viability so we were very lucky that we were able to collect a lot of seeds as birch seeds shatter and shed everywhere, so once it has done that you will never find it.'
grammar= r"""
Gerunds: {<DT>?<NN>?<VBG><NN>}
Coordinated noun: {<NNP><CC><NNP>|<DT><PRP\$><NNS><CC><NNS>|<NN><NNS><CC><NNS>}
"""
cp=nltk.RegexpParser(grammar)
tree = cp.parse(pos_tag(word_tokenize(sentences)))
for subtree in tree.subtrees():
		if subtree.label()=='Gerunds': print(subtree)
tree.draw()




#Problem 4:

#source: http://www.bbc.com/news/science-environment-34378953
#Coordinated noun

sentences='UK scientists have successfully germinated seeds from the critically endangered Japanese Birch, a species that has just 21 known trees remaining. The seeds were collected last year during an expedition to a remote location in mountains near Tokyo. Experts suggest that the remaining wild population of Betula chichibuensis is too small to sustain itself unaided. The young trees will be shared with other arboretums in an effort to help conserve the threatened species. The International Union for the Conservation of Nature (IUCN) forecasts a bleak outlook for the tree species in the wild. The species is also self-incompatible, requiring two individuals to be close enough to cross-pollinate one another, making seed production uncertain in small subpopulations. During September and October, a team led by researchers from the University of Oxford Botanic Gardens, in conjunction with the University of Tokyo, embarked on an expedition to collect seed samples from the threatened birch trees. It is found in a very, very remote location and it is not an easy place to get to. It has got very, very low viability so we were very lucky that we were able to collect a lot of seeds as birch seeds shatter and shed everywhere, so once it has done that you will never find it.'
grammar= r"""
Gerunds: {<DT>?<NN>?<VBG><NN>}
Coordinated noun: {<NNP><CC><NNP>|<DT><PRP\$><NNS><CC><NNS>|<NN><NNS><CC><NNS>}
"""
cp=nltk.RegexpParser(grammar)
tree = cp.parse(pos_tag(word_tokenize(sentences)))
for subtree in tree.subtrees():
		if subtree.label()=='Coordinated noun': print(subtree)
tree.draw()
