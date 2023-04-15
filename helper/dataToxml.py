from bs4 import BeautifulSoup
import lxml
import re

def dataToXml(rawData:list):
    # Create a BeautifulSoup object with xml builder
    xmlBuilder = BeautifulSoup(features="xml")

    # Create the root element <books>
    sentences = xmlBuilder.new_tag("sentences")

    # Create a child element <book> with attributes
    sentence = xmlBuilder.new_tag("sentence")
    # Create sub-elements <title>, <author>, and <price> with text
    text = xmlBuilder.new_tag("text")
    text.string = rawData[0]
    aspectCategories = xmlBuilder.new_tag("aspectCategories")
    sentence.append(text)
    sentence.append(aspectCategories)
    
    sentences.append(sentence)
    
    
    xmlBuilder.append(sentences)
    # Write the XML file with prettify method
    with open("books.xml", "w") as f:
        f.write(xmlBuilder.prettify())