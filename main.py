from helper.helper import *

# Read The Data
data_1 = ReadAFileAndDevideBySectence("data/Apex AD2600 Progressive-scan DVD player.txt")
data_2 = ReadAFileAndDevideBySectence("data/Canon G3.txt")
data_3 = ReadAFileAndDevideBySectence("data/Creative Labs Nomad Jukebox Zen Xtra 40GB.txt")
data_4 = ReadAFileAndDevideBySectence("data/Nikon coolpix 4300.txt")
data_5 = ReadAFileAndDevideBySectence("data/Nokia 6610.txt")


# Join Them Togeather
data = data_1 + data_2 + data_3 + data_4 + data_5

print(len(data))

