import json

with open('../Data/data_to_configs-20220602T064136Z-00123655/data_to_configs/configs.json') as f:
    words = json.load(f)
# [type,x-type,y-type,opacity,marker,line,mode,text,autobiny]
# print(type(words))
# dicts=  words[0]["config"]
dicts=set([])
list =[]


def extract(sentence):
    for key in sentence:
        if  isinstance(sentence[key], dict):
            extract(sentence[key])
        elif key !='color':
            dicts.add(str(sentence[key]))
        else:
            print(key," -> ",sentence[key])


def MakeVoc():
    global i
    for i in words:
        sentence = i["config"]
        for key in sentence:
            # word=key+":"+str(sentence[key])
            # if word not in list :
            #     list.append(word)
            # dicts.add(str(sentence[key]))

            if isinstance(sentence[key], dict):
                extract(sentence[key])
            else:
                dicts.add(str(sentence[key]))



MakeVoc()
# print(len(dicts))
# print(dicts)
s =""
for i in dicts:
    s+=i+'\n'
text_file = open("tstVoc.txt", "w")
text_file.write(s)
text_file.close()
# print("....")
# print(len(list))
# print(list)
