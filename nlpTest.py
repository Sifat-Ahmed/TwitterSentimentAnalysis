from nltk import word_tokenize, sent_tokenize, pos_tag
from nltk.stem import WordNetLemmatizer
import enchant , random, nltk
from nltk.corpus import movie_reviews
import mysql


dictionary = enchant.Dict('en-us')
lemmatizer = WordNetLemmatizer()
example = "Economics allows you to see the costs associated with any given action. By studying economics, you'll begin to understand how to allocate one of the most precious resources of all - your time."
punctuations = ['.', ',', '!', '?', '-', '@', ':', ';']

documents = [ (list(movie_reviews.words(fileid)) , category)
              for category in movie_reviews.categories()
              for fileid in movie_reviews.fileids(category)
            ]



words = list()
sentence = list()
tagged = list()
wordList = list()

sentences = sent_tokenize(example)

for eachSentence in sentences:
    sentence.append(word_tokenize(eachSentence))

for eachSentence in sentence:
    for word in eachSentence:
        if word not in punctuations:
            wordList.append(word.lower())
            tagged.append(pos_tag(word))


##for eachTaggedWord in tagged:
    ##print(eachTaggedWord)

random.shuffle(wordList)

for word in wordList:
    print(word)

##classifier = NaiveBayesClassifier.train(wordList)

wordList = nltk.FreqDist(wordList)

print(wordList.most_common())
print(wordList['of'])
