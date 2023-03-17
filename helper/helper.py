
#open The Files

import re
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

def ExtractData(data:list):
    xlFile = xlsxwriter.Workbook("data.xlsx")
    xlSheet = xlFile.add_worksheet("Extracted Data")
    row = 0

    for sentence in data:
        col = 0
        xlSheet.write(row,col,sentence)
        col += 1
        sentiment_value =  re.search(r'\b\w+\[[+-]?\d+\]',  sentence)
        if sentiment_value:
            sentiment_value_txt = re.findall(r'\b\w+\[[+-]?\d+\]', sentence)
            for val in sentiment_value_txt:
                xlSheet.write(row,col,val)
                col += 1
        
        
        row += 1
    
    xlFile.close()
    