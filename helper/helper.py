
#open The Files



def ReadAFileAndDevideBySectence(filename : str):
    # read the file and split it into sections baseon the review
    with open(filename, 'r') as f:
        text = f.read()
    sections = text.split('[t]')
    
    # # remove and leading and traling whitespace
    # for section in sections:
    #     section.strip()
    return sections