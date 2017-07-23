from nltk import NaiveBayesClassifier as nlNB

from textblob.classifiers import NaiveBayesClassifier as tNB

training_data_set = [
    ('I love this movie. It was awesome.' , 'pos'),
    ('It was a good movie to watch. Recommend to others also.' , 'pos'),
    ('Full waste of money. It was not amazing at all.', 'neg'),
    ('The movie was not good.', 'neg'),
    ('I love this place. it\'s amazing here.', 'pos'),
    ('I am simply tired of this stuff.', 'neg'),
    ('She lied when I asked her about the story.', 'neg'),
    ('He was not crying. You were wrong' , 'pos'),
    ('It does not feel good at all' , 'neg'),
    ('You are nothing but a drug addict.' , 'neg'),
    ('I am not in a bad mood today.' , 'pos'),
    ('I am in a bad mood today.' , 'neg'),
    ('The weather is very bad' , 'neg'),
    ('Life is too good' , 'pos'),
    ('The vegetables were good as they were cooked perfectly' , 'pos')
    #('I am bored as the class is too much boring' , 'neg')
    #('Lying is bad. Do not lie' , 'pos'),
    #('Mr. Rahim was lying on that day.' , 'neg')
]

test_data_set = [
    ('The fried rice was good.', 'pos'),
    ('I am totally bored.', 'neg'),
    ('That day she was lying', 'neg'),
    ('He is my best friend', 'pos'),
    ('He was my best friend but not now.', 'neg')
]

textblob_naivebayes = tNB(training_data_set)
print(textblob_naivebayes.classify('The weather is not good at all') , "\n")
## OUTPUT ----> POS

#for data in test_data_set:
    #print(textblob_naivebayes.classify(data))

accuracy = textblob_naivebayes.accuracy(test_data_set)
print(accuracy)
