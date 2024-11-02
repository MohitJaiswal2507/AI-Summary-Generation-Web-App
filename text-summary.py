import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation

text = "The Mahabharata is an ancient Indian epic where the main story revolves around two branches of a family - the Pandavas and Kauravas - who, in the Kurukshetra War, battle for the throne of Hastinapura. Interwoven into this narrative are several smaller stories about people dead or living, and philosophical discourses."

stopwords = list(STOP_WORDS)
print(stopwords)