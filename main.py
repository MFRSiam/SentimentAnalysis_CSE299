import nltk
from helper.helper import *
from helper.dataToxml import *
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
# Delete The Empty Strings
data = list(filter(lambda string: string != "", data))

# Delete The Extra Spaces
data = [s.strip() for s in data]


temp_data = DevideBySentence(data)
# Convert a List of List into a singluar List
sentence_list = ConvertListOfReviewOfListOfSentenceToListOfSentence(temp_data)
raw_sentence_data = sentence_list[:]




# Remove Annotated Features in the data
sentence_data_with_annotation = Remove_Feature(sentence_list)

# Remove Annotations
sentence_data = Remove_Annotations(sentence_data_with_annotation)

sentence_data_for_xml_parse = sentence_data[:]

dataToXml(raw_sentence_data,sentence_data_for_xml_parse)

sentence_data = Remove_Excess_Punctuation(sentence_data)
# Extract Data In a Excell File
xlFile = xlsxwriter.Workbook("data.xlsx")
# Filter Out And SAVE The Processed Data
sentence_data = ExtractData(raw_sentence_data,sentence_data,xlFile)

sentence_data = [re.sub(r'\w*\d\w*', '', sentence) for sentence in sentence_data]



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

# Save The Data Without Stopwords
SimpleExtractData(data_without_stopwords,xlFile,name="Without Stopwords")

lemmatize_data = LemmatizeSentence(data_without_stopwords)

SimpleExtractData(lemmatize_data,xlFile,name="Lemmatize Data")


# For Debug 
# for i in data_without_stopwords:
#     print(i)


xlFile.close()