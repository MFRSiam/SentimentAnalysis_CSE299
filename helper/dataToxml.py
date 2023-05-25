from bs4 import BeautifulSoup
import lxml
import re

def dataToXml(rawData:list,prettyData:list):
    # Create a BeautifulSoup object with xml builder
    xmlBuilder = BeautifulSoup(features="xml")
    #xmlBuilder.prettify()
    # Create the root element <books>
    sentences = xmlBuilder.new_tag("sentences")

    for index,data in enumerate(rawData):
        sentiment_value =  re.search(r'\b\w+\[[+-]?\d+\]',  data)
        if sentiment_value:
            # Create a child element <book> with attributes
            sentence = xmlBuilder.new_tag("sentence")
            
            # Create sub-elements <title>, <author>, and <price> with text
            text = xmlBuilder.new_tag("text")
            text.string = prettyData[index]
            sentence.append(text)
            
            aspectCategories = xmlBuilder.new_tag("aspectCategories")
            
            
            sentiment_value_txt = re.findall(r'\b\w+\[[+-]?\d+\]', data)
            plain_aspects = [re.sub(r'\[.*?\]', '', item) for item in sentiment_value_txt]
            for i,asp_txt in enumerate(sentiment_value_txt):
                if "+" in asp_txt:
                    aspects = xmlBuilder.new_tag("aspectCategory")

                    aspects.attrs["polarity"] = "positive"
                    aspects.attrs["category"] = plain_aspects[i]
                    aspectCategories.append(aspects)

                elif "-" in asp_txt:
                    aspects = xmlBuilder.new_tag("aspectCategory")

                    aspects.attrs["polarity"] = "negative"
                    aspects.attrs["category"] = plain_aspects[i]
                    aspectCategories.append(aspects)

            sentence.append(aspectCategories)
            sentences.append(sentence)
            sentences.indent = 4
    
    
    
    
    
    
    xmlBuilder.append(sentences)
    # Write the XML file with prettify method
    with open("newData.xml", "w") as f:
        f.write(xmlBuilder.prettify())