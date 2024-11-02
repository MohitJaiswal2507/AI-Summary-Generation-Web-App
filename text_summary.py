import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from heapq import nlargest

text = """Marvel's The Avengers[5] (titled Marvel Avengers Assemble in the United Kingdom and Ireland[1][6] and commonly referred to as simply The Avengers) is a 2012 American superhero film based on the Marvel Comics superhero team of the same name. Produced by Marvel Studios and distributed by Walt Disney Studios Motion Pictures,[a] it is the sixth film in the Marvel Cinematic Universe (MCU). Written and directed by Joss Whedon, the film features an ensemble cast including Robert Downey Jr., Chris Evans, Mark Ruffalo, Chris Hemsworth, Scarlett Johansson, and Jeremy Renner as the Avengers, alongside Tom Hiddleston, Stellan Skarsgård, and Samuel L. Jackson. In the film, Nick Fury and the spy agency S.H.I.E.L.D. recruit Tony Stark, Steve Rogers, Bruce Banner, Thor, Natasha Romanoff, and Clint Barton to form a team capable of stopping Thor's brother Loki from subjugating Earth.

The film's development began when Marvel Studios received a loan from Merrill Lynch in April 2005. After the success of the film Iron Man in May 2008, Marvel announced that The Avengers would be released in July 2011 and would bring together Stark (Downey), Rogers (Evans), Banner (at the time portrayed by Edward Norton),[b] and Thor (Hemsworth) from Marvel's previous films. With the signing of Johansson as Romanoff in March 2009, Renner as Barton in June 2010, and Ruffalo replacing Norton as Banner in July 2010, the film was pushed back for a 2012 release. Whedon was brought on board in April 2010 and rewrote the original screenplay by Zak Penn. Production began in April 2011 in Albuquerque, New Mexico, before moving to Cleveland, Ohio in August and New York City in September. The film has more than 2,200 visual effects shots."""

def summarizer(rawdocs):
        
    stopwords = list(STOP_WORDS)
    # print(stopwords)

    nlp = spacy.load('en_core_web_sm')
    doc = nlp(rawdocs)
    # print(doc)

    tokens = [token.text for token in doc]
    # print(tokens)

    # punctuation = punctuation + '\n'
    # punctuation

    #CREATING A FREQUENCY DICTIONARY for checking freq of words
    word_freq = {}

    for word in doc:
        if word.text.lower() not in stopwords and word.text.lower() not in punctuation:
            if word.text not in word_freq.keys():
                word_freq[word.text] = 1
            else:
                word_freq[word.text] += 1

    # print(word_freq)

    max_freq = max(word_freq.values())

    for word in word_freq.keys():
        word_freq[word] = word_freq[word]/max_freq
        
    # print(word_freq)

    sent_tokens = [sent for sent in doc.sents]
    # print(sent_tokens)

    sent_scores = {}
    for sent in sent_tokens:
        for word in sent:
            if word.text in word_freq.keys():
                if sent not in sent_scores.keys():
                    sent_scores[sent] = word_freq[word.text]
                else:
                    sent_scores[sent] += word_freq[word.text]
                    
    # print(sent_scores)

    select_len = int(len(sent_tokens) * 0.3)
    # print(select_len)

    summary = nlargest(select_len , sent_scores , key=sent_scores.get)
    # print(summary)

    final_summary = [word.text for word in summary]
    summary = ' '.join(final_summary) 
    # print(text)
    # print(summary)
    # print("Lenght of original text = ",len(text.split(' ')))
    # print("Lenght of summary text = ",len(summary.split(' ')))
    
    return summary,doc , len(rawdocs.split(' ')) , len(summary.split(' '))