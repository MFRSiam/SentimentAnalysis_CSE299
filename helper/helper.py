
#open The Files

# For RegEX
import re
# For Excell File Management
import xlsxwriter


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
        sentence = x.split('##')
        sentence_data.append(sentence)
    return sentence_data

def ConvertListOfReviewOfListOfSentenceToListOfSentence(data:list):
    ret_data = [item for sublist in data for item in sublist]
    return ret_data


def Remove_Feature(sentences : list):
    cleaned_sentences = []
    for sentence in sentences:
        cleaned_sentence = re.sub(r'\b\w+\[[+-]?\d+\]', '', sentence)
        cleaned_sentences.append(cleaned_sentence)
    return cleaned_sentences

def Remove_Annotations(sentences: list):
    cleaned_sentences  = []
    pattern = r'\[(?:u|p|s|cc|cs)\]|\[/(?:u|p|s|cc|cs)\]'
    
    for sentence in sentences:
        cleaned_sentence = re.sub(pattern, '', sentence)
        cleaned_sentences.append(cleaned_sentence)
    return cleaned_sentences

def Remove_Excess_Punctuation(sentences:list):
    cleaned_sentence = [s.replace(',','').replace(':','') for s in sentences]
    without_empty = [s for s in sentences if s.strip()]
    return cleaned_sentence

def ExtractData(data:list, cleaned_data:list, xlFile:xlsxwriter.Workbook):
    xlSheet = xlFile.add_worksheet("Extracted Data")
    row = 0

    for i, sentence in enumerate(data):
        col = 0
        xlSheet.write(row,col,cleaned_data[i])
        col += 1
        sentiment_value =  re.search(r'\b\w+\[[+-]?\d+\]',  sentence)
        if sentiment_value:
            sentiment_value_txt = re.findall(r'\b\w+\[[+-]?\d+\]', sentence)
            separator = ", "
            result = separator.join(sentiment_value_txt)
            xlSheet.write(row+1,col,result)
            col += 1
        extra_annotation = re.search(r'\[(?:u|p|s|cc|cs)\]|\[/(?:u|p|s|cc|cs)\]',sentence)
        if extra_annotation:
            extra_annotation_txt = re.findall(r'\[(?:u|p|s|cc|cs)\]|\[/(?:u|p|s|cc|cs)\]',sentence)
            separator = ", "
            result = separator.join(extra_annotation_txt)
            xlSheet.write(row+1,col,result)
            col += 1
        row += 1
    
    

def SimpleExtractData(data:list,xlFile:xlsxwriter.Workbook,name:str):
    xlSheet = xlFile.add_worksheet(name)
    row = 0
    col = 0
    for sentence in data:
        xlSheet.write(row,col,sentence)
        row += 1
    