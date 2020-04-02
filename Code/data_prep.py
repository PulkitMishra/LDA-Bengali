import os
import json

def get_tok(file):
    f = open(file, "r")
    list = []
    for line in f:
        words = line.split()
        if words and (words[-1][0] == "N" or words[-1][0] == "V"):
            list.append(words[0])
    return list

def get_all():
    mega = []
    basepath = 'testdata/new/'
    for entry in os.listdir(basepath):
        if os.path.isfile(os.path.join(basepath, entry)):
            mega.append(get_tok(os.path.join(basepath, entry)))
    with open('data_NandV.txt', 'w') as outfile:
        json.dump({"name": mega},outfile)

get_all()
