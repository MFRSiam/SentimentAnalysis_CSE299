import nltk
from helper.helper import *
from nltk.corpus import stopwords

# Read The Data
data_1 = ReadAFileAndDevideByReview("data/Apex AD2600 Progressive-scan DVD player.txt")
data_2 = ReadAFileAndDevideByReview("data/Canon G3.txt")
data_3 = ReadAFileAndDevideByReview("data/Creative Labs Nomad Jukebox Zen Xtra 40GB.txt")
data_4 = ReadAFileAndDevideByReview("data/Nikon coolpix 4300.txt")
data_5 = ReadAFileAndDevideByReview("data/Nokia 6610.txt")


# Join Them Togeather
data = data_1 + data_2 + data_3 + data_4 + data_5

# print(len(data))

temp_data = DevideBySentence(data)
# Convert a List of List into a singluar List
sentence_data = ConvertListOfReviewOfListOfSentenceToListOfSentence(temp_data)
# Remove Annotated Features in the data
sentence_data = Remove_Feature(sentence_data)
# Remove Annotations
sentence_data = Remove_Annotations(sentence_data)

# print(sentence_data)


# Cleaning The Data: 1: Get the stopwords From The NLTK Server
nltk.download('stopwords')
# 2: Set a Variable For Stop words
stop_words = set(stopwords.words('english'))

# 3: Remove The Stopwords
data_without_stopwords = []
for sentence in sentence_data:
    # split the sentence into words
    words = sentence.split()
    # remove the stopwords
    filtered_words = [word for word in words if word.lower() not in stop_words]
    # join the words back into a sentence
    filtered_sentence = ' '.join(filtered_words)
    data_without_stopwords.append(filtered_sentence)

for i in data_without_stopwords:
    print(i)