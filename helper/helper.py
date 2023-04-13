
#open The Files

# For RegEX
import re
# For Excell File Management
import xlsxwriter
#for string Operations 
import string
# Import NLTK
import nltk
from nltk.stem import WordNetLemmatizer

def ReadAFileAndDevideByReview(filename : str):
    # read the file and split it into sections baseon the review
    with open(filename, 'r') as f:
        text = f.read()
    sections = text.split('[t]')
    
    # # remove and leading and traling whitespace
    # for section in sections:
    #     section.strip()
    return sections

def DevideBySentence(data : list):
    sentence_data = []
    
    for x in data:
        sentence = x.split('\n')
        sentence_data.append(sentence)
    return sentence_data

def ConvertListOfReviewOfListOfSentenceToListOfSentence(data:list):
    ret_data = [item for sublist in data for item in sublist]
    return ret_data


def Remove_Feature(sentences : list):
    cleaned_sentences = []
    for sentence in sentences:
        cleaned_sentence = re.sub(r'\b\w+\[[+-]?\d+\]', '', sentence)
        #cleaned_sentence = re.sub(r'[^\w\s]+|##', '', cleaned_sentence)
        cleaned_sentence = re.sub(r".*##", "", cleaned_sentence)
        cleaned_sentences.append(cleaned_sentence)
    return cleaned_sentences

def Remove_Annotations(sentences: list):
    cleaned_sentences  = []
    pattern = r'\[(?:u|p|s|cc|cs)\]|\[/(?:u|p|s|cc|cs)\]'
    
    for sentence in sentences:
        cleaned_sentence = re.sub(pattern, '', sentence)
        cleaned_sentence = cleaned_sentence.strip()
        cleaned_sentences.append(cleaned_sentence)
    return cleaned_sentences

def Remove_Excess_Punctuation(sentences:list):
    return [re.sub('[%s]' % re.escape(string.punctuation), '' , text) for text in sentences]

def ExtractData(data:list, cleaned_data:list, xlFile:xlsxwriter.Workbook):
    xlSheet = xlFile.add_worksheet("Extracted Data")
    row = 0
    ret_data = []
    for i, sentence in enumerate(data):
        col = 0
        sentiment_value =  re.search(r'\b\w+\[[+-]?\d+\]',  sentence)
        if sentiment_value:
            xlSheet.write(row,col,cleaned_data[i])
            col += 1
            ret_data.append(cleaned_data[i])
            sentiment_value_txt = re.findall(r'\b\w+\[[+-]?\d+\]', sentence)
            numbers = []
            for aspects in sentiment_value_txt:
                match = re.search(r'[\+\-]\d+', aspects)
                if match:
                    numbers.append(int(match.group()))
            plain_aspects = [re.sub(r'\[.*?\]', '', item) for item in sentiment_value_txt]
            total = sum(numbers)
            if total > 0:
                xlSheet.write(row,col,"positive")
                col+=1
            elif total < 0:
                xlSheet.write(row,col,"negative")
                col+=1
            else:
                xlSheet.write(row,col,"neutral")
                col+=1
            separator = ", "
            result = separator.join(plain_aspects)
            xlSheet.write(row,col,result)
            col += 1
            result = separator.join(sentiment_value_txt)
            xlSheet.write(row,col,result)
            col += 1
            extra_annotation = re.search(r'\[(?:u|p|s|cc|cs)\]|\[/(?:u|p|s|cc|cs)\]',sentence)
            if extra_annotation:
                extra_annotation_txt = re.findall(r'\[(?:u|p|s|cc|cs)\]|\[/(?:u|p|s|cc|cs)\]',sentence)
                separator = ", "
                result = separator.join(extra_annotation_txt)
                xlSheet.write(row,col,result)
                col += 1
            row += 1
    return ret_data

def SimpleExtractData(data:list,xlFile:xlsxwriter.Workbook,name:str):
    xlSheet = xlFile.add_worksheet(name)
    row = 0
    col = 0
    for sentence in data:
        xlSheet.write(row,col,sentence)
        row += 1


def LemmatizeSentence(data:list):
    return [__LemmatizeSTR(sentence) for sentence in data]

def __LemmatizeSTR(sentence:str):
    lemmatizer = WordNetLemmatizer()
    lemmatized_sentence = []
    for word, tag in nltk.pos_tag(nltk.word_tokenize(sentence)):
        if tag.startswith('NN'):
            lemmatized_sentence.append(lemmatizer.lemmatize(word, pos='n'))
        elif tag.startswith('VB'):
            lemmatized_sentence.append(lemmatizer.lemmatize(word, pos='v'))
        elif tag.startswith('JJ'):
            lemmatized_sentence.append(lemmatizer.lemmatize(word, pos='a'))
        elif tag.startswith('R'):
            lemmatized_sentence.append(lemmatizer.lemmatize(word, pos='r'))
        else:
            lemmatized_sentence.append(word)
    return ' '.join(lemmatized_sentence)
