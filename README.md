1. (Exercise 7.2 from NLTK): Write a tag pattern to match noun phrases
containing plural head nouns, e.g. \many/JJ researchers/NNS", \two/CD
weeks/NNS", \both/DT new/JJ positions/NNS". Try to do this by generalizing
the tag pattern (discussed in the text) that handles singular noun
phrases. Reminder: Tag patterns are regular expression grammars that
use the tagset as categories to be matched. For example, the following
pattern says that a noun phrase might be made of an optional determiner
(as indicated by the DT followed by a question mark), any number of
adjectives (as indicated by the JJ followed by an asterisk), followed by a
noun (NN).
2. (Exercise 7.5 from NLTK) Write a tag pattern to cover noun phrases that
contain gerunds, e.g. \the/DT receiving/VBG end/NN", \assistant/NN
managing/VBG editor/NN". For each pattern, include an example phrase
that matches the pattern. If programming, add these patterns to the
grammar, one per line and test your work using some tagged sentences
of your own devising. Non-programming students should provide a set of
tagged sentences and mark by hand the noun phrases with gerunds that
match the new patterns; you can also use the online tagger demo to help
check your work.)
3. (Exercise 7.6 from NLTK) Write one or more tag patterns to handle coordinated
noun phrases, e.g. uly/NNP and/CC August/NNP,
all/DT your/PRP$ managers/NNS and/CC supervisors/NNS,
company/NN courts/NNS and/CC adjudicators/NNS. For each pattern
include an example that matches the pattern
4. Provide a text fragment of at least 120 words from an online source that
includes both noun phrases with gerunds and with coordination and show
the chunk boundaries. (Include both your chunk-marked text and a link
to the original source.)
