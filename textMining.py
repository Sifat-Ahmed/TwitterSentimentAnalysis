import random, nltk
from nltk.corpus import movie_reviews

documents = [ (list(movie_reviews.words(fileid)) , category)
              for category in movie_reviews.categories()
              for fileid in movie_reviews.fileids(category) ]

random.shuffle(documents)
wordList = [word.lower() for word in movie_reviews.words()]
#print(wordList[:30])
wordList = nltk.FreqDist(wordList)

word_features = list(wordList.keys())[:15000]

def find_features(document):
    words = set(document)
    features = {}
    #features = (True for word in word_features if word in words )
    for w in word_features:
        features[w] = (w in words)
    return features

#print(find_features(movie_reviews.words('neg/cv000_29416.txt')))

featuresets = [(find_features(rev) , category) for (rev,category) in documents ]
print(len(featuresets))
cut_off = int(len(featuresets) * 5.8/6.0)

training_set = featuresets[:cut_off]
testing_set = featuresets[cut_off:]

classifier = nltk.NaiveBayesClassifier.train(training_set)
print('accuracy' , (nltk.classify.accuracy(classifier , testing_set))*100  , '%')
classifier.show_most_informative_features(10)
