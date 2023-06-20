from flair.data import Sentence
from flair.nn import Classifier

# make a sentence
sentence = Sentence('I hate Berlin .')


# load the NER tagger
tagger = Classifier.load('sentiment')

# run NER over sentence
tagger.predict(sentence)

sentiment_value = sentence.labels[0].value

# print the sentence with all annotations
print(sentiment_value)