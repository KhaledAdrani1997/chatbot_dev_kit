import yaml
import json

path = 'data/yml/ai.yml'

#with open('data.txt', 'w') as my_data_file:
    #write data to the file
# After leaving the above block of code, the file is closed

f = open(path,'r')
string = f.read()
f.close()

data = yaml.load(string)

with open('data/raw/ai.json', 'w') as outfile:
    json.dump(data, outfile)

print(json)

